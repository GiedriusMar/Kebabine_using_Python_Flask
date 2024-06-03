# Kebabine using Python Flask

## Introduction
Welcome to my **Kebabine** project! 
This repository is a demonstration of a web application developed using Python and Flask. As I am student learning Python and Flask, this project is designed to help you understand the basics of web development with Python and Flask technologies. 
The application simulates a simple kebab shop where users can browse the menu, place orders, etc.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Explanation of Directories and Files](#explanation-of-directories-and-files)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **User Authentication**: Log in to access personalized features (to add or delete products from DB).
- **Menu Management**: View a list of available products with details, product pictures and prices.
- **Upload new product via HTML form**: Add new item to the database including product picture.
- **Delete product**: Delete product from database just from HTML Admin page.

## Project Structure

```
PYTHON PROJECT/
│
├── .venv/
│
├── database/
│   └── kebabine_db.sqlite
│
├── kebabine/
│   ├── static/
│   │   ├── images/
│   │   │   ├── kebab-shop-bg.jpg
│   │   │   └── logo-white.png
│   │   └── product_images/
│   │       ├── kebab1.jpeg
│   │       ├── kebab_01.jpg
│   │       ├── kebab_02.jpg
│   │       ├── kebab_03.jpg
│   │       ├── kebab_05.jpg
│   │       ├── kebab_06.jpg
│   │       ├── kebab_07.jpg
│   │       └── kebab_08.jpg
│   │
│   ├── templates/
│   │   ├── add_product.html
│   │   ├── base.html
│   │   ├── contacts.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── product.html
│   │   └── products.html
│   │
│   ├── __init__.py
│   ├── email_settings.py
│   ├── models.py
│   └── routes.py
│
├── .env
├── manage.py
└── run.py

```
## Explanation of Directories and Files

- **.venv/**: Virtual environment directory.
- **database/**: Contains the SQLite database file.
  - `kebabine_db.sqlite`: The SQLite database file.
- **kebabine/**: Main application directory.
  - **static/**: Contains static files such as images and CSS.
    - **images/**: General images for the site.
      - `kebab-shop-bg.jpg`: Background image for the site.
      - `logo-white.png`: Site logo.
    - **product_images/**: Images of the products.
      - `kebab1.jpeg`, `kebab_01.jpg`, ..., `kebab_08.jpg`: Product images.
  - **templates/**: HTML templates for the site.
    - `add_product.html`: Template for adding a product.
    - `base.html`: Base template used by other templates.
    - `contacts.html`: Contacts page template.
    - `index.html`: Home page template.
    - `login.html`: Login page template.
    - `product.html`: Single product page template.
    - `products.html`: Products listing page template.
  - `__init__.py`: Initializes the Flask app.
  - `email_settings.py`: Configuration for email settings.
  - `models.py`: Database models.
  - `routes.py`: Application routes.
- **.env**: Environment variables file.
- **manage.py**: Management script for database migrations.
- **run.py**: Script to run the Flask app.

## Contributing

We welcome contributions to improve this project! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Create a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions, feel free to reach out:

- **Giedrius Mar** - [GitHub](https://github.com/GiedriusMar)

P.S. Feel free to customize the sections further based on any specific details or additional functionalities you want to highlight in the repository.

Happy coding!
