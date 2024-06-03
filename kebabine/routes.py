from flask import render_template, request, redirect, url_for, flash
from kebabine import app, db, bcrypt
from kebabine.models import Product, User
from flask_login import login_user, login_required, logout_user, current_user
import os


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    all_products = Product.query.all()
    return render_template("products.html", products=all_products)


@app.route("/contacts")
def contacts():
    return render_template("contacts.html")


@app.route("/add_product", methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        product = request.form['product']
        price = float(request.form['price'])
        ingredients = request.form.get('ingredients')
        extra = request.form['extra']
        image = request.files['image']

        if image and image.filename != '':
            image_filename = image.filename
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            image.save(image_path)
        else:
            image_filename = 'default.jpg'

        new_product = Product(product=product, price=price, ingredients=ingredients, extra=extra,
                              image_filename=image_filename)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('products'))

    return render_template('add_product.html')


@app.route("/products/<int:id>")
def product(id):
    one_product = Product.query.get(id)
    return render_template("product.html", product=one_product)


@app.route("/products/<int:id>/delete")
def delete_product(id):
    one_product = Product.query.get(id)
    db.session.delete(one_product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('products'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(name=username).first()
        if user and (user.password == password):
            flash('You have successfully logged in!', "success")
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

