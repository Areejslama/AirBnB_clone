#!/usr/bin/python3
"""Represent a base class"""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """Define a class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs.pop("__class__", None)
        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, obj)
            else:
                setattr(self, key, value)
        else:
                self.id = str(uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict
    def __str__(self):
        return "{} {} {}".format(type(self).__name__, self.id, self.__dict__)
