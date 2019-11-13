#!/usr/bin/python3
"""
Implement a console for AirBnB Project.
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from datetime import datetime
from models.city import City
from models.user import User
from models import storage
import cmd


def get_objects_by_class(args):
    """
    Get all objects and validate params / if class exist
    :param args:
    :return:
    """
    objects = storage.all()
    args = args.split()

    if len(args) == 0:
        print("** class name missing **")
        return None, None
    elif len(args) == 1:
        print("** instance id missing **")
        return None, None

    class_name = args[0]
    inst_id = args[1]

    try:
        eval(class_name)
    except NameError:
        print("** class doesn't exist **")
        return None, None

    return objects, "{}.{}".format(class_name, inst_id)


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter for AirBnB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """exit — cause the shell to exit
        :param args: list of arguments
        :return: Always True
        """
        return True

    def do_EOF(self, args):
        """EOF — cause the shell to exit
        :param args: list of arguments
        :return: Always True
        """
        return True

    def emptyline(self):
        """
        Ignore empty line
        """
        pass

    def do_create(self, args):
        """
        Create new instance with args[0]
        :param args: list of arguments
        """
        if len(args.split()) == 0:
            print("** class name missing **")
            return

        try:
            obj = eval(args.split()[0])()
        except Exception as e:
            print("** class doesn't exist **")
            return

        print(obj.id)
        obj.save()

    def do_show(self, args):
        """
        Show object by id
        :param args:
        """
        objects, inst_id = get_objects_by_class(args)

        if inst_id:
            try:
                print(objects[inst_id])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """
            Destroy object by Id
        :param args:
        """
        objects, inst_id = get_objects_by_class(args)

        if inst_id:
            try:
                objects.pop(inst_id)
                storage.save()
            except Exception as e:
                print("** no instance found **")

    def do_all(self, args):
        """
        Show all objects
        :param args:
        :return:
        """
        objects = storage.all()

        try:
            if args:
                eval(args)
        except Exception as e:
            print("** class doesn't exist **")
            return

        listobj = []
        for key in objects:
            listobj = [str(objects[key])] + listobj
        print(listobj)

    def do_update(self, args):
        """
        Update attributes of a object
        :param args:
        :return:
        """
        objects, inst_id = get_objects_by_class(args)
        args = args.split()

        if objects and inst_id:
            if len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return

            if objects and inst_id:
                value = args[3].strip('"')
                value = value.strip("'")

                if args[2] not in ["created_at", "updated_at"]:
                    setattr(objects[inst_id], args[2], value)
                    objects[inst_id].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
