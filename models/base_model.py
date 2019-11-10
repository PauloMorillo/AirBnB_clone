#!/usr/bin/python3
"""This module has the main class called basemodel"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModell class"""
    def __init__(self, *args, **kwargs):
        """Here begins the class"""
        if kwargs:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Method to print class, id, and json"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Function to save the new update"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys and values of the instance"""
        jsdic = dict()
        for key in self.__dict__:
            if key == "created_at" or key == "updated_at":
                value = self.__dict__[key].isoformat()
            else:
                value = self.__dict__[key]
            jsdic[key] = value
        jsdic["__class__"] = self.__class__.__name__
        return jsdic
