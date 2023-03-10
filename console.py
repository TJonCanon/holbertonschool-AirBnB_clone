#!/usr/bin/python3
""" Console Module """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models import storage
valid_classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                 "State": State, "City": City, "Amenity": Amenity,
                 "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Console Class """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit Command to exit the program """
        return True

    def do_EOF(self, arg): 
        """ Handles EOF command """
        return True

    def emptyline(self):
        """ does nothing on enter """
        return False

    def check_class(self, value):
        """ Check if:
        a) a class name is given
        b) class name exists in valid_classes dictionary
        """
        if value == "" or value is None:
            print("** class name missing **")
            return False

        parsed_val = value.split(' ')
        if parsed_val[0] not in valid_classes.keys():
            print("** class doesn't exist **")
            return False

        return True

    def valid_instance(self, value):
        """ Check if:
        a) instance name is given
        b) instance name exists in valid_instances dictionary
        """
        if len(value) < 2:
            print("** instance id missing **")
            return False

        key = "{}.{}".format(value[0], value[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return False

        return key

    def do_create(self, arg):
        """ Create new instance of object """
        if self.check_class(arg):
                new = valid_classes[arg]()
                new.save()
                print(new.id)

    def do_show(self, arg):
        """ Prints string representation of instance based on class and id """
        if self.check_class(arg):
            word = arg.split(' ')
            if self.valid_instance(word):
                key = "{}.{}".format(word[0], word[1])
                print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on class name and id """
        if self.check_class(arg):
            word = arg.split(' ')
            valid_key = self.valid_instance(word)
            if valid_key:
                del storage.all()[valid_key]
                storage.save()

    def do_all(self, arg):
        """ print all instances """
        if arg != "":
            word = arg.split(' ')
            if word[0] not in valid_classes.keys():
                print("** class doesn't exist **")
            else:
                n = [
                    str(obj) for key, obj in storage.all().items()
                    if type(obj).__name__ == word[0]
                ]
                print(n)
        else:
            n = [str(obj) for key, obj in storage.all().items()]
            print(n)

    def do_update(self, arg):
        """
        update an instance based on class name and id
        by add/update attributes
        """
        if self.check_class(arg):
            word = arg.split(' ')
            valid_key = self.valid_instance(word)
            if valid_key:
                if len(word) < 3:
                    print("** attribute name missing **")
                    return False
                if len(word) < 4:
                    print("** value missing **")
                    return False
                
                if valid_key in storage.all().keys():
                     setattr(storage.all()[valid_key], word[2], word[3].strip('\'"'))

if __name__ == '__main__':
    HBNBCommand().cmdloop()