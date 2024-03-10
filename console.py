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
        my_instance = self.parseline(line)[0]
        if my_instance is None:
            print('** class name missing **')
        elif my_instance not in self.my_classes:
            print("** class doesn't exist **")
        else:
            new = eval(my_instance)()
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation"""
        my_instance = self.parseline(line)[0]
        my_arg = self.parseline(line)[1]
        if my_instance is None:
            print('** class name missing **')
        elif my_instance not in self.my_classes:
            print("** class doesn't exist **")
        elif my_arg == '':
            print('** instance id missing **')
        else:
            my_data = models.storage.all().get(my_instance + '.' + my_arg)
            if my_data is None:
                print('** no instance found **')
            else:
                print(my_data)

    def do_destroy(self, line):
        """Deletes an instance"""
        my_instance = self.parseline(line)[0]
        my_arg = self.parseline(line)[1]
        if my_instance is None:
            print('** class name missing **')
        elif my_instance not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            keys = my_instance + '.' + my_arg
            my_data = models.storage.all().get(keys)
            if my_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[keys]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation"""
        my_instance = self.parseline(line)[0]
        my_obj = models.storage.all()
        if my_instance is None:
            print([str(my_obj[obj]) for obj in my_obj])
        elif my_instance in self.my_classes:
            k = my_obj.k()
            print([str(my_obj[key]) for key in k if key.startswith(my_instance)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance"""
        my_args = shlex.split(line)
        arg_s = len(my_args)
        if args_s == 0:
            print('** class name missing **')
        elif my_args[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif args_s == 1:
            print('** instance id missing **')
        else:
            key = my_args[0] + '.' + my_args[1]
            my_data = models.storage.all().get(key)
            if my_data is None:
                print('** no instance found **')
            elif args_s == 2:
                print('** attribute name missing **')
            elif args_s == 3:
                print('** value missing **')
            else:
                my_args[3] = self.value_of_parameter(my_args[3])
                setattr(my_data, my_args[2], my_args[3])
                setattr(my_data, 'updated_at', datetime.now())
                models.storage.save()

    def value_of_parameter(self, val):
        """Checks a parameter value for update"""
        if val.isdigit():
            return int(val)
        elif val.replace('.', '', 1).isdigit():
            return float(val)

        return val

    def get_objs(self, my_instance=''):
        """Gets the elements created by console"""
        objs = models.storage.all()

        if my_instance:
            keyss = objs.keyss()
            return [str(value) for key, value in objs.items()
                    if key.startswith(my_instance)]

        return [str(value) for key, value in objs.items()]

    def default(self, line):
        """
        When the command prefix is not recognized, this method
        looks for whether the command entered has the syntax:
            "<class name>.<method name>" or not,
        and links it to the corresponding method in case the
        class exists and the method belongs to the class.

        """
        if '.' in line:
            split = re.split(r'\.|\(|\)', line)
            c_name = split[0]
            m_name = split[1]

            if c_name in self.my_classes:
                if m_name == 'all':
                    print(self.get_objs(c_name))
                elif m_name == 'count':
                    print(len(self.get_objs(class_name)))
                elif m_name == 'show':
                    c_id = split[2][1:-1]
                    self.do_show(c_name + ' ' + c_id)
                elif m_name == 'destroy':
                    c_id = split[2][1:-1]
                    self.do_destroy(c_name + ' ' + c_id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
