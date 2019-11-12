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
import os


class FileStorage:
    """Class to serializes instances to a JSON and desearialize"""
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """return the dictionary onbjects"""
        return FileStorage.__objects

    def new(self, obj):
        """assign objects private attribute"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes objects private attribute to a JSON file"""
        tmp = {}
        for obj in FileStorage.__objects:
            tmp.update({obj: FileStorage.__objects[obj].to_dict()})

        with open(self.__file_path, "w") as f:
            f.write(json.dumps(tmp))

    def reload(self):
        """Deserializes the JSON file to objects private attribute"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path) as f:
                FileStorage.__objects = json.load(f)

            for key, value in FileStorage.__objects.items():
                base = eval(value["__class__"])

                FileStorage.__objects[key] = base(**value)
