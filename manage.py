from kebabine import db
from kebabine.models import Product
# db.create_all()

product = Product(
    product='Chicken Kebab in Lavash',
    price=7.00,
    ingredients='Lavash, Chicken meat, Chinese cabbage, Tomatoes, Cucumbers, Pickles',
    extra='Garlic sauce',
)

product_1 = Product(
    product='Lamb Kebab in Lavash',
    price=9.50,
    ingredients='Lavash, Lamb meat, Chinese cabbage, Tomatoes, Cucumbers, Pickles',
    extra='Mix Sauce',
)
product_2 = Product(
    product='Beef Kebab in Lavash (spicy)',
    price=9.80,
    ingredients='Lavash, Beef, Chinese cabbage, Tomatoes, Cucumbers, Onions',
    extra='Spicy sauce',
)

product_3 = Product(
    product='Beef Kebab in plate',
    price=8.80,
    ingredients='Beef, Chinese cabbage, Tomatoes, Cucumbers, Onions',
    extra='Garlic sauce',
)


db.session.add_all([product, product_1, product_2, product_3])
db.session.commit()

