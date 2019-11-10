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
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes objects private attribute to a JSON file"""
        for key in self.__objects:
            self.__objects[key] = self.__objects[key].to_dict()

        with open(self.__file_path, "w") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """Deserializes the JSON file to objects private attribute"""
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())
                print(self.__objects)
        except:
            pass
