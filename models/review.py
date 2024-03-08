#!/usr/bin/python3
"""represent a class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """define a class"""
    place_id = ''
    user_id = ''
    text = ''
