#!/usr/bin/python3
""" Base Model module """
import uuid
from datetime import datetime
class BaseModel():
    """ Base Model Class """
    def __init__(self, *args, **kwargs):
        """ Initialize Base Model Object """
        if kwargs:
             fmt = "%Y-%m-%dT%H:%M:%S.%f"
             for key, value in kwargs.items():
                 if key is not "__class__":
                     self.__dict__.update({key: value})
                 if key in ["created_at", "updated_at"]:
                     self.__dict__.update({key: datetime.strptime(value, fmt)})
        
        else:
            self.id = str(uuid.uuid4())
            self.updated_at = self.created_at = datetime.now()

    def __str__(self):
        """ string representation of Base Model object """
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Update attriubte updated_at """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
        `__dict__` of the instance. """
        myDict = self.__dict__.copy()
        myDict['__class__'] = self.__class__.__name__
        myDict['created_at'] = self.created_at.isoformat()
        myDict['updated_at'] = self.updated_at.isoformat()
        return myDict