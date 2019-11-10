#!/usr/bin/python3
"""
Implement a console for AirBnB Project.
"""
from models.base_model import BaseModel
import models
import cmd


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
		pass

	def do_create(self, args):
		"""
		Create new instance with args[0]
		:param args: list of arguments
		"""
		obj = eval(args.split()[0])()

		print(obj.id)
		obj.save()


	def do_show(self, args):
		objects = models.storage.all()
		args = args.split()

		if len(args) == 0:
			print("** class name missing **")
			return
		elif len(args) == 1:
			print("** instance id missing **")
			return

		class_name = args[0]
		inst_id = args[1]

		try:
			eval(class_name)
		except:
			print("** class doesn't exist **")
			return

		inst_id = "{}.{}".format(class_name, inst_id)
		try:
			print(objects[inst_id])
		except:
			print("** no instance found **")


	def do_destroy(self, args):
		objects = models.storage.all()
		args = args.split()

		if len(args) == 0:
			print("** class name missing **")
			return
		elif len(args) == 1:
			print("** instance id missing **")
			return

		class_name = args[0]
		inst_id = args[1]

		try:
			eval(class_name)
		except:
			print("** class doesn't exist **")
			return

		inst_id = "{}.{}".format(class_name, inst_id)
		try:
			objects.pop(inst_id)
			models.storage.save()
		except Exception as e:
			print("** no instance found **")


	def do_all(self, args):
		objects = models.storage.all()
		print([value for value in objects.values()])


	def do_update(self, args):
		pass


if __name__ == '__main__':
	HBNBCommand().cmdloop()
