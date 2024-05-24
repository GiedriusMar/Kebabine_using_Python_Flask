from flask import render_template, request, redirect, url_for
from kebabine import app, db
from kebabine.models import Product

names = ['Jonas', 'Antanas', 'Petras', 'Viktoras']


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
def add_product():
    if request.method == 'POST':
        product = request.form['product']
        price = float(request.form['price'])
        ingredients = request.form.get('ingredients')
        extra = request.form['extra']
        new_product = Product(product=product, price=price, ingredients=ingredients, extra=extra)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('add_product.html')


@app.route("/products/<int:id>")
def product(id):
    one_product = Product.query.get(id)
    return render_template("product.html", product=one_product)


@app.route("/products/<int:id>/delete")
def delete_product(id):
    print('Delete')
    one_product = Product.query.get(id)
    db.session.delete(one_product)
    db.session.commit()
    return redirect(url_for('products'))

