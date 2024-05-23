from kebabine import db
from kebabine.models import Product
# db.create_all()
product = Product(
    product='Pikantiškas kebabas su vištiena',
    price=8.00,
    ingredients='Lavašas, vištiena, salotos, padažas',
    extra='Čili padažas',
)

product = Product(
    product='Kebabas su aviena',
    price=7.50,
    ingredients='Lavašas, aviena, salotos, padažas',
    extra='Spec. padažas',
)

db.session.add_all([product, product, product, product])
db.session.commit()

