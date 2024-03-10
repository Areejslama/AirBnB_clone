#!/usr/bin/python3
"""Console Module"""


from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
import models
from models.place import Place
from models.review import Review
import cmd
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """command processor class."""
    prompt = '(hbnb) '
    my_classes = ['BaseModel', 'User', 'State', 'City',
                       'Amenity', 'Place', 'Review']

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """handle empty lines"""
        print()
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel.
        """
        my_command = self.parseline(line)[0]
        if not my_command:
            print('** class name missing **')
        elif my_command not in self.my_classes:
            print("** class doesn't exist **")
        else:
            new_i = eval(my_command)()
            new_i.save()
            print(new_i.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        my_command = self.parseline(line)[0]
        args = self.parseline(line)[1]
        if not my_command:
            print('** class name missing **')
        elif my_command not in self.my_classes:
            print("** class doesn't exist **")
        elif args == '':
            print('** instance id missing **')
        else:
            my_data = models.storage.all().get(my_command + '.' + args)
            if my_data is None:
                print('** no instance found **')
            else:
                print(my_data)

    def do_destroy(self, line):
        """Deletes an instance"""
        my_command = self.parseline(line)[0]
        args = self.parseline(line)[1]
        if my_command is None:
            print('** class name missing **')
        elif my_command not in self.my_classes:
            print("** class doesn't exist **")
        elif args == '':
            print('** instance id missing **')
        else:
            key = my_command + '.' + args
            my_data = models.storage.all().get(key)
            if my_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation"""
        my_command = self.parseline(line)[0]
        my_objs = models.storage.all()
        if my_command is None:
            print([str(objs[obj]) for obj in objs])
        elif my_command in self.my_classes:
            keys = my_objs.keys()
            print([str(my_objs[key]) for key in keys if key.startswith(my_command)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance"""
        arg = shlex.split(line)
        arg_s = len(arg)
        if arg_s == 0:
            print('** class name missing **')
        elif arg[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif arg_s == 1:
            print('** instance id missing **')
        else:
            key = arg[0] + '.' + arg[1]
            my_data = models.storage.all().get(key)
            if my_data is None:
                print('** no instance found **')
            elif arg_s == 2:
                print('** attribute name missing **')
            elif arg_s == 3:
                print('** value missing **')
            else:
                arg[3] = self.parameter_value(arg[3])
                setattr(my_data, arg[2], arg[3])
                setattr(my_data, 'updated_at', datetime.now())
                models.storage.save()

    def parameter_value(self, val):
        """Checks a parameter value for an update"""
        if val.isdigit():
            return int(val)
        elif val.replace('.', '', 1).isdigit():
            return float(val)

        return val

    def get_objs(self, an_instance=''):
        """Gets the elements created by the console"""
        objs = models.storage.all()

        if an_instance:
            keys = objs.keys()
            return [str(val) for key, val in objs.items()
                    if key.startswith(an_instance)]

        return [str(val) for key, val in objs.items()]

    def default(self, line):
    """
    handle entered commands
    """
    if '.' in line:
        sp = re.split(r'\.|\(|\)', line)
        cls_name = sp[0]
        m_name = sp[1]

        if cls_name in self.my_classes:
            if m_name == 'all':
                print(self.get_objs(cls_name))
            elif m_name == 'count':
                print(len(self.get_objs(cls_name)))
            elif m_name == 'show':
                c_id = sp[2][1:-1]
                self.do_show(cls_name + ' ' + c_id)
            elif m_name == 'destroy':
                c_id = sp[2][1:-1]
                self.do_destroy(cls_name + ' ' + c_id)
            else:
                print("** class doesn't exist **")
    else:
        print("Command not recognized. Type 'help' for a list of available commands.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
