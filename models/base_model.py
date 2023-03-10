#!/usr/bin/python3
""" Base Model module """
import uuid
from datetime import datetime
import models

class BaseModel:
    """ Base Model Class """
    def __init__(self, *args, **kwargs):
        """ Initialize Base Model Object """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(value, fmt))
                    else:
                        setattr(self, key, value)
        
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ string representation of Base Model object """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Update attriubte updated_at """
        self.updated_at = datetime.now()
        models.storage.save

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
        `__dict__` of the instance. """
        my_dict = self.__dict__.copy()
        my_dict.update({"updated_at": self.updated_at.isoformat()})
        my_dict.update({"created_at": self.created_at.isoformat()})
        my_dict.update({"__class__": type(self).__name__})
        return my_dict