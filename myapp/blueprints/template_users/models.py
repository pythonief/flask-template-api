"""
Template models file for a blueprint.
Hints:
    - The dataclass import utilitie is the built-in functionality from python to replace 
    the Flask-Marshmallow extension. It needs you declare metadata attributes before initialization
    and the decorator @dataclass before the class declaration
"""

# Import utilities
from dataclasses import dataclass

# Import extensions
from myapp.extensions import db

"""
MODEL CLASSES DB
"""

MAX_STRING_LENGHT = 80

@dataclass
class User(db.Model):
    # Meta attributes for dataclass decorator
    id: int
    username: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(MAX_STRING_LENGHT),
                         unique=True, nullable=False)
    email = db.Column(db.String(MAX_STRING_LENGHT),
                      unique=True, nullable=False)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
