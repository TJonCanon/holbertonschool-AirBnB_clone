#!/usr/bin/python3
""" File Storage Module """
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
valid_classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Review": Review}
class FileStorage:
    """ File Storage Class """

    __file_path = "my_file.json"
    __objects = {}

    def all(self):
        """ Return dictionary of all obj """
        return self.__objects

    def new(self, obj):
        """ create new obj in storage """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        """ save al obj in __objects at __file_path """
        with open(self.__file_path, "w") as file_path:
            json.dump(
                {
                    k: (v.to_dict() if not isinstance(v, dict) else v)
                    for (k, v) in self.__objects.items()
                }, file_path)

    def reload(self):
        """ reload data from __file_path, recreate into __objects """
        if exists(self.__file_path):
             with open(self.__file_path, "r") as file_path:
                 fulldict = json.load(file_path)
                 for obj_key in fulldict.keys():
                     class_name = obj_key.split('.')
                     self.new(valid_classes[class_name[0](**fulldict[obj_key])])
