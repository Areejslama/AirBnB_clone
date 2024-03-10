#!/usr/bin/python3
"""represent Console Module"""

import cmd
from datetime import datetime
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """processor class"""
    prompt = "(hbnb) "
    my_classes = ['BaseModel', 'City', 'State', 'User',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """handle empty lines"""
        print()
        pass

    def do_create(self, line):
        """Creates an instance of Base"""
        cls_name = self.parseline(line)[0]
        if class_name is None:
            print('** class name missing **')
            return
        elif cls_name not in self.my_classes:
            print("** class doesn't exist **")
            return

        try:
            my_instance = getattr(models, cls_name)()
            my_instance.save()
            print(my_instance.id)
        except Exception as e:
            print(f"Error creating instance: {str(e)}")

    def do_show(self, line):
        """Prints the string representation"""
        cls_name = self.parseline(line)[:2]
        inst_id = self.parseline(line)[:2]
        if cls_name is None:
            print('** class name missing **')
            return
        elif cls_name not in self.my_classes:
            print("** class doesn't exist **")
            return
        elif inst_id is None:
            print('** instance id missing **')
            return

        obj = f"{cls_name}.{instance_id}"
        m_instance = models.storage.all().get(obj)
        if m_instance is None:
            print('** no instance found **')
        else:
            print(m_instance)

    def do_destroy(self, line):
        """Deletes an instance"""
        cls_name =  self.parseline(line)[:2]
        inst_id = self.parseline(line)[:2]
        if cls_name is None:
            print('** class name missing **')
            return
        elif cls_name not in self.my_classes:
            print("** class doesn't exist **")
            return
        elif inst_id is None:
            print('** instance id missing **')
            return

        obj = f"{cls_name}.{inst_id}"
        a_instances = models.storage.all()
        if obj not in a_instances:
            print('** no instance found **')
            return

        del a_instances[obj]
        models.storage.save()

    def do_all(self, line):
        """Prints all string representation"""
        clsname = self.parseline(line)[0]
        if class_name is None:
            print([str(obj) for obj in models.storage.all().values()])
        elif cls_name in self.my_classes:
            inst = [str(obj) for obj in models.storage.all().values() if type(obj).__name__ == class_name]
            print(inst)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance"""
        my_args = shlex.split(line)
        if len(my_args) < 1:
            print('** class name missing **')
            return
        elif my_args[0] not in self.my_classes:
            print("** class doesn't exist **")
            return
        elif len(my_args) < 2:
            print('** instance id missing **')
            return

        obj = f"{my_args[0]}.{my_args[1]}"
        a_instances = models.storage.all()
        if obj not in all_instances:
            print('** no instance found **')
            return

        inst = a_instances[obj]
        if len(my_args) < 3:
            print('** attribute name missing **')
            return
        elif len(my_args) < 4:
            print('** value missing **')
            return

        setattr(inst, my_args[2], self.value_of_parameter(my_args[3]))
        setattr(inst, 'updated_at', datetime.now())
        models.storage.save()

    def value_of_parameter(self, val):
        """Checks a parameter value for update"""
        try:
            return int(val)
        except ValueError:
            try:
                return float(val)
            except ValueError:
                return val

    def get_objs(self, class_name=''):
        """Gets the elements created by console"""
        a_instances = models.storage.all()
        if class_name is None:
            return [str(obj) for obj in a_instances.values()]
        else:
            return [str(obj) for obj in a_instances.values() if type(obj).__name__ == class_name]

    def default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
            "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.
        """
        if '.' in line:
            spl = line.split('.')
            c_name = split[0]
            m_name = split[1].split('(')[0]
            arg = split[1].split('(')[1].split(')')[0]

            if c_name in self.my_classes:
                if m_name == 'all':
                    print(self.get_objs(class_name))
                elif m_name == 'count':
                    print(len(self.get_objs(class_name)))
                elif m_name == 'show':
                     self.do_show(f"{class_name} {arg}")
                elif m_name == 'destroy':
                    self.do_destroy(f"{class_name} {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
