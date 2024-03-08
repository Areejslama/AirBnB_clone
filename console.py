#!/usr/bin/python3
"""Represent a command interpreter"""
import cmd
import shlex
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from state import State
from city import City
from amenity import Amenity
from place import Place
from review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    my_classes = ['BaseModel', 'user']

    def do_EOF(self, arg):
        """Define EOF command"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Define behavior for empty line"""
        pass

    def do_create(self, line):
        my_instance = self.parseline(line)[0]
        if my_instance is None:
            print("Class name missing")
        elif my_instance not in self.my_classes:
            print("Class doesn't exist")
        else:
            new_instance = eval(my_instance)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
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
        my_instance = self.parseline(line)[0]
        my_arg = self.parseline(line)[1]
        if my_instance is None:
            print('** Class name missing **')
        elif my_instance not in self.my_classes:
            print("** class doesn't exist **")
        elif my_arg == '':
            print('** instance id missing **')
        else:
                val = my_instance + "." + my_arg
                my_data = models.storage.all().get(val)
                if my_data is None:
                    print('** No instance found **')
                else:
                    del models.storage.all()[val]
                    models.storage.save()

    def do_all(self, line):
        my_instance = self.parseline(line)[0]
        my_obj = models.storage.all()
        if not my_instance:
            print([str(my_obj[obj]) for obj in my_obj])
        elif my_instance in self.my_classes:
            my_key = my_obj.keys()
            print([str(my_obj[key]) for key in my_key if key.startswith(my_instance)])
        else:
            print("** Class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        arg = shlex.split(line)
        args_s = len(arg)
        if args_s == 0:
            print('** class name missing **')
        elif arg[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif args_s == 1:
            print('** instance id missing **')
        else:
            keys = arg[0] + '.' + arg[1]
            my_data = models.storage.all().get(keys)
            if my_data is None:
                print('** no instance found **')
            elif args_s == 2:
                print('** attribute name missing **')
            elif args_s == 3:
                print('** value missing **')
            else:
                arg[3] = self.value_of_parameter(arg[3])
                setattr(my_data, arg[2], arg[3])
                setattr(my_data, 'updated_at', datetime.now())
                models.storage.save()

    def value_of_parameter(self, v):
        """Checks a parameter value for an update."""
        if v.isdigit():
            return int(v)
        elif v.replace('.', '', 1).isdigit():
            return float(v)
        return v

    def get_obj(self, an_instance=''):
        """Gets the elements created by the console."""
        obj = models.storage.all()

        if an_instance:
            return [str(value) for key, value in obj.items() if key.startswith(an_instance)]

        return [str(value) for key, value in obj.items()]

if __name__ == "__main__":
    HBNBCommand().cmdloop()
