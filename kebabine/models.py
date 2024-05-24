import os
from datetime import datetime

from kebabine import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False, default='Kebab')
    price = db.Column(db.Float, nullable=False, default=10.0)
    ingredients = db.Column(db.String(250), nullable=True, default='Lamb')
    extra = db.Column(db.String(150), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now(), nullable=True)

    def __init__(self, product, price, ingredients, extra):
        self.product = product
        self.price = price
        self.ingredients = ingredients
        self.extra = extra

    def __repr__(self):
        return f'{self.product} - {self.price}'