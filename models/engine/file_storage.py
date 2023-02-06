#!/usr/bin/python3
""" File Storage Module """
import json
from os.path import exists

class FileStorage:
    """ File Storage Class """

    __file_path = "my_file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        with open(self.__file_path, "w") as file_path:
            json.dump(
                {
                    k: (v.to_dict() if not isinstance(v, dict) else v)
                    for (k, v) in self.__objects.items()
                }, file_path)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, "r") as file_path:
                self.__objects = json.load(file_path)