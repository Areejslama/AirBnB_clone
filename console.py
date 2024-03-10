#!/usr/bin/python3
"""Represent a command interpreter"""
import cmd
import shlex
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    my_classes = ['BaseModel', 'user',  'State',  'City',
            'Amenity', 'Place', 'Review']

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

    def do_count(self, arg):
        """count the number of instances of class"""
        arg1 = parseline(arg)
        cou= 0
        for objs in storage.all().values():
            if arg1[0] == objs.__class__.__name__:
                cou += 1
                print(cou)

    def do_update(self, line):
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

    def do_default(self, line):
        """looks for entered commands"""
        if '.' in l:
            split = re.split(r'\.|\(|\)', l)
            c_name = split[0]
            m_name = split[1]

        if c_name in self.my_classes:
            if m_name == 'all':
                print(self.get_obj(c_name))
            elif m_name == 'count':
                print(len(self.get_obj(c_name)))
            elif m_name == 'show':
                c_id = split[2][1:-1]
                self.do_show(c_name + ' ' + c_id)
            elif m_name == 'destroy':
                c_id = split[2][1:-1]
                self.do_destroy(c_name + ' ' + c_id)
    def do_count(self, arg):
        """ Count instance of class"""
        arg_sp = shlex.split(arg)
        cou = 0
        for obj in storage.all().values():
            if args_split[0] == obj.__class__.__name__:
                cou += 1
        print(cou)

    if __name__ == "__main__":
        HBNBCommand().cmdloop()
