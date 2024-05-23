from flask import render_template, request, redirect, url_for
from kebabine import app, db
from kebabine.models import Product

names = ['Jonas', 'Antanas', 'Petras', 'Viktoras']


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    all_products = Product.query.all()
    return render_template("products.html", products=all_products)

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

# @app.route("/product")
# def product():
#     return render_template("product.html")

@app.route("/products/1")
def product(id=1):
    one_product = Product.query.get(id)
    all_products = Product.query.all()
    return render_template("products.html", products=all_products, product=one_product)


@app.route("/products/<int:id>/delete")
def delete_product(id):
    print('Delete')
    one_product = Product.query.get(id)
    db.session.delete(one_product)
    db.session.commit()
    return redirect(url_for('products'))

