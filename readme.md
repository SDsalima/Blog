# Flask User API for Blog Post Project

A simple Flask application demonstrating JWT authentication, SQLAlchemy with MySQL, and database migrations.  
Includes basic `User`, `Post`, and `Comment` models with secure password handling.

---

## 📦 Dependencies

This project uses the following Python packages:

- **Flask** – lightweight web framework
- **Flask-JWT-Extended** – JWT authentication and route protection
- **Werkzeug** – password hashing and security utilities
- **Flask-SQLAlchemy** – ORM for database models
- **MySQL** – relational database backend
- **Flask-Migrate** – database migrations powered by Alembic
- **Flask-Marshmallow** – integrates Marshmallow with Flask, enabling easy serialization of SQLAlchemy models to JSON and validation of incoming request data. It simplifies handling query objects and ensures clean API responses.
- **Email-Validator** – validates and formats email addresses, ensuring they are syntactically correct and the domain exists. Useful for user registration and login forms.
- **Marshmallow-SQLAlchemy** – automatically detects fields from SQLAlchemy models to generate schemas for serialization and deserialization.
---

## ⚙️ Installation

Clone the repository and install dependencies with Pipenv:

```bash
pipenv install
---
Or export to requirements.txt if needed:
pipenv lock -r > requirements.txt
pip install -r requirements.txt
---
set up the enverenment variable in config.py:
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/dbname"
JWT_SECRET_KEY = "your-secret-key"

#DataBase Managment
-- Initialize migrations:
flask db init
-- Generate a migration scripts:
flask db migrate -m "Initial migration"
-- Apply migrations:
flask db upgrade

## Custom CLI commends

flask db_create   # create all tables
flask db_drop     # drop all tables
