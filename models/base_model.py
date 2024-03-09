#!/usr/bin/python3
"""Represent a base class"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """Define a basemodel of classes"""
    def __init__(self, *args, **kwargs):
        """initialize args and kwargs"""
        if kwargs:
            kwargs.pop("__class__", None)
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, obj)
                else:
                    setattr(self, key, value)
        else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)

    def save(self):
        """method to update an instance"""
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        """method to return a dictionary"""
        my_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value
        return my_dict
    def __str__(self):
        """method to return a string representaion of methods"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
