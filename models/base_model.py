#!/usr/bin/python3
""" Base Model module """
import uuid
import datetime
class BaseModel():
    """ Base Model Class """
    def __init__(self):
        """ Initialize Base Model Object """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

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