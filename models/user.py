#!/usr/bin/python3
"""represent user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """define user class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
