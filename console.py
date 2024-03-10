#!/usr/bin/python3
"""Represent a command interpreter"""
import cmd
import shlex
from datetime import datetime
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    my_classes = ['BaseModel', 'User', 'State', 'City',
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
        """Create new instance of BaseModel"""
        if line is None:
            print("** class name missing **")
        elif line not in self.my_classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Show string representation of an instance"""
        args = shlex.split(line)
        if args is None:
            print("** class name missing **")
        elif args[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, line):
        """Delete an instance"""
        args = shlex.split(line)
        if args is None:
            print("** class name missing **")
        elif args[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """Prints string representation of all instances"""
        args = shlex.split(line)
        if args and args[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            if args:
                objs = [str(obj) for key, obj in objects.items() if key.startswith(args[0])]
            else:
                objs = [str(obj) for obj in objects.values()]
            print(objs)

    def do_update(self, line):
        """Update an instance attribute"""
        args = shlex.split(line)
        if args is None:
            print("** class name missing **")
        elif args[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            obj = models.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                setattr(obj, args[2], self.value_of_parameter(args[3]))
                setattr(obj, 'updated_at', datetime.now())
                models.storage.save()

    def value_of_parameter(self, v):
        """Checks a parameter value for an update."""
        if v.isdigit():
            return int(v)
        elif v.replace('.', '', 1).isdigit():
            return float(v)
        elif v.startswith('"') and v.endswith('"'):
            return v[1:-1]
        return v

    if __name__ == "__main__":
        HBNBCommand().cmdloop()
