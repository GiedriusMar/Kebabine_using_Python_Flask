Welcome to the **Kebabine** project! This repository contains a web application built with Python and Flask. The application simulates a kebab shop, providing functionalities such as menu display, order processing, and more.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- Display a menu of available kebabs
- Process customer orders
- Track order status
- Manage menu items (add, edit, delete)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/GiedriusMar/Kebabine_using_Python_Flask.git
   cd Kebabine_using_Python_Flask
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set up the environment variables**
   Create a `.env` file in the root directory and add the following configurations:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

2. **Initialize the database**
   Ensure you have SQLite installed, then run:
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

3. **Run the application**
   ```bash
   flask run
   ```
   Open your browser and navigate to `http://127.0.0.1:5000` to see the application in action.

## Project Structure

```
Kebabine_using_Python_Flask/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── menu.html
│   │   └── order.html
│   └── static/
│       ├── css/
│       └── js/
├── migrations/
├── tests/
│   ├── test_basic.py
├── .env
├── .gitignore
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

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

Happy coding!
```

Feel free to customize the sections further based on any specific details or additional functionalities you want to highlight in the repository.
