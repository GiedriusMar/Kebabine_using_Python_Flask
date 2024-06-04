# Kebabine using Python Flask

## Introduction
Welcome to my **Kebabine** project! 
This repository is a demonstration of a web application developed using Python 3.12 and Flask 3.0.3. 
As I am just begginer student learning Python and Flask, this project is designed to help you understand the basics of web development using Python and Flask technologies. 
The application simulates a simple "Kebab shop" website where users can browse the menu. Authorised person (Admin) after logging-in can upload new product (direct from website application), delete product, etc.

##
This `README.md` file provides an overview of your project, instructions for setting up a virtual environment, and how to get started with running the application. Adjust the sections as needed for your specific project requirements.


## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Explanation of Directories and Files](#explanation-of-directories-and-files)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Setting Up Virtual Environment](#setting-up-virtual-environment)
  - [Windows](#windows)
  - [Linux/Mac](#linuxmac)
- [Running the Application](#running-the-application)
- [License](#license)
- [Contact](#contact)


## Features
- **Menu Management**: View a list of available products with details, product pictures and prices.
- **User Authentication**: Log in to access personalized features (to add or delete products from DB).
- **Upload new product via HTML form**: Add new item (upload product) to database, including product picture - direct from website HTML application.
- **Delete product**: Delete product from database - direct from website HTML application.


## Project Structure

```
PYTHON PROJECT/
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
├── requirements.txt
└── run.py

```

## Explanation of Directories and Files

- **database/**: Contains the SQLite database file.
  - `kebabine_db.sqlite`: The SQLite database file (please create one by yourself).
- **kebabine/**: Main application directory (Python Package).
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
- **.env**: Environment variables file. [Please create one by yourself using your own credentials](#structure-of-env-file).
- **manage.py**: Management script for database migrations and manual data uploading to database.
- **requirements.txt**: List of required Python libraries for the project.
- **run.py**: Script to run the Flask app.


## Technologies Used
- **Python 3.12**
- **Flask 3.0.3**
- **HTML 5 / CSS 3**


## Getting Started

To run this project on your local machine, follow the steps below:

1. Clone the repository:
    ```bash
    git clone https://github.com/GiedriusMar/Kebabine_using_Python_Flask.git
    cd Kebabine_using_Python_Flask
    ```

2. Set up a virtual environment:
    See [Setting Up Virtual Environment](#setting-up-virtual-environment) for detailed instructions.

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables by creating a `.env` file in the root directory and adding the necessary configurations.

5. Initialize the database:
    ```bash
    python manage.py init_db
    ```

6. Run the application:
    ```bash
    python run.py
    ```

7. Open your browser and go to `http://127.0.0.1:5000/` to see the application running.


## Setting Up Virtual Environment

### Windows

1. Open Command Prompt.
2. Navigate to your project directory.
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    ```bash
    venv\Scripts\activate
    ```

### Linux/Mac

1. Open Terminal.
2. Navigate to your project directory.
3. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    ```
4. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```


## Running the Application

After setting up the virtual environment and installing the dependencies, you can run the application using:

```bash
python run.py
```
Then, navigate to `http://127.0.0.1:8000/` in your web browser to access the application.


## Structure of .env file
DATABASE_URL = 'link to your local database'

USER_NAME = 'your username'
USER_EMAIL = 'your email'
USER_PASSWORD = 'your password'

SECRET_KEY = 'your secret key'


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## Contact

If you have any questions, feel free to reach out:

- **Giedrius Mar** - [GitHub](https://github.com/GiedriusMar)

Happy coding!
