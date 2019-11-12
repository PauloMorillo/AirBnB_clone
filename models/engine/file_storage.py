#!/usr/bin/python3
"""module with filestorage class"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
import json


class FileStorage:
    """Class to serializes instances to a JSON and desearialize"""

    def __init__(self):
        """all begins here"""
        self.__file_path = "file.json"
        self.__objects = dict()

    def all(self):
        """return the dictionary onbjects"""
        return self.__objects

    def new(self, obj):
        """assign objects private attribute"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes objects private attribute to a JSON file"""
        tmp = {}
        for obj in self.__objects:
            tmp.update({obj: self.__objects[obj].to_dict()})

        with open(self.__file_path, "w") as f:
            f.write(json.dumps(tmp))

    def reload(self):
        """Deserializes the JSON file to objects private attribute"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.load(f)

            for key, value in self.__objects.items():
                base = eval(value["__class__"])

                self.__objects[key] = base(**value)
        except Exception as e:
            pass
