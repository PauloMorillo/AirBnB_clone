#!/usr/bin/python3
"""module with filestorage class"""
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
        key = self.__class__.__name__ + self.id
        self.__objects[key] = self.__dict__

    def save(self):
        """Serializes objects private attribute to a JSON file"""
        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the JSON file to objects private attribute"""
        
