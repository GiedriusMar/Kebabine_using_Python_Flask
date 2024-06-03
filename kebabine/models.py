from datetime import datetime
from kebabine import db, app
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_login import UserMixin


class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False, default='Kebab')
    price = db.Column(db.Float, nullable=False, default=10.0)
    ingredients = db.Column(db.String(250), nullable=True, default='Lamb')
    extra = db.Column(db.String(150), nullable=False)
    image_filename = db.Column(db.String(100), nullable=False, default='default.jpg')
    created_date = db.Column(db.DateTime, default=datetime.now(), nullable=True)

#  Made corrections on def __init__
    def __init__(self, product, price, ingredients, extra, image_filename):
        self.product = product
        self.price = price
        self.ingredients = ingredients
        self.extra = extra
        self.image_filename = image_filename


    def __repr__(self):
        return f'{self.product} - {self.price}'


class User(db.Model, UserMixin):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(50), unique=True, nullable=False)
    email = db.Column("email", db.String(120), unique=True, nullable=False)
    password = db.Column("password", db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return f'{self.name}, {self.email}'

    def get_id(self):
        return self.user_id

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.user_id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

