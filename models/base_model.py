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
        print(self.created_at)
    def __str__(self):
        return ("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        tdn = self.__dict__
        format_time = {
            "updated_at": tdn['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f"), # replace .strftime with isoformat()
            "created_at": tdn['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f") # replace .strftime with isoformat()
        }
        tdn.update(format_time)
        tdn.update({"__class__": type(self).__name__})
        return tdn
