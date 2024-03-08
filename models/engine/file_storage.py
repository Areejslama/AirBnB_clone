#!/usr/bin/python3
"""represente storage class"""

from json import load
from json import dump
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Define a class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return all objects in the storage"""
        return FileStorage.__objects
    def new(self, obj):
        """Add a new object to the storage"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        """Save objects to file"""
        e_dict = {}
        for key, value in FileStorage.__objects.items():
            e_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            dump(e_dict, f)
    def reload(self):
        """Reload objects from file"""
        from models.base_model import BaseModel
        my_classes = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__file_path, encoding="UTF-8") as f:
                des =  load(f)
                if des:
                    for obj_id, obj_dict in des.items():
                        clsname = obj_dict.get('__class__')
                        if clsname and clsname in my_classes:
                            class_obj = my_classes[clsname]
                            self.new(class_obj(**obj_dict))
        except FileNotFoundError:
            pass
