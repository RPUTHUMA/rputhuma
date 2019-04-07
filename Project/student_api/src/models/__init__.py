# src/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# initialize our db

db = SQLAlchemy()

from .ClassModel import ClassModel
from .StudentModel import StudentModel
