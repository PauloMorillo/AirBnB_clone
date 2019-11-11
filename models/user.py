#!/usr/bin/python3
"""
    User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
       User class
    """
    first_name = ""
    last_name = ""
    password = ""
    email = ""
