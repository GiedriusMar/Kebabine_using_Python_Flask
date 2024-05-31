from dotenv import load_dotenv
import os
from flask import Flask, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user
from flask_mail import Mail
from kebabine.email_settings import EmailUser
from flask_bcrypt import Bcrypt
from os.path import join, dirname, realpath


load_dotenv()


USER = EmailUser(
    name=os.getenv('USER_NAME'),
    email=os.getenv('USER_EMAIL'),
    password=os.getenv('USER_PASSWORD'),
)

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/product_images/')


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = os.getenv('SECRET_KEY')
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
db.create_all()

from kebabine.models import User


mail = Mail(app)
login_manager = LoginManager(app)
login_manager.login_view = 'product'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    db.create_all()
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    flash('You have to login:')
    return redirect(url_for('login'))


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.email == USER.email


from kebabine.models import *
from kebabine import routes


admin = Admin(app)
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Product, db.session))


# Migrate(app, db)

