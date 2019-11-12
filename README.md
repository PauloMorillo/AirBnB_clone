<p>
<img width="260" height="90" src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUXW7JF5MT%2F20191111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20191111T223735Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=362946d518481bf449fd72f50f681272882ab7a419ff1dca01f0729650faad74" align="right">
</p>
# Airbnb clone

Airbnb is a web platform to rent house, rooms and more. This is the first step to clone it. In this step we did a console to manage the objects created by the classes to do easier the way to add, del, destroy and update objects. Also we use a file JSON to store and persist objects. and obviusly we created our data model.

## Command interpreter

Like we did before this command interpreter is a console to manage the objects created by our classes (Create, update, destroy)

To start the console use you have to stay in the path (Airbnb_clone/) where the file console.py is and execute it.

```bash

./console.py

```

## How to use the console
To use the console you can do it with interactive mode or non interactive mode like we show you there.

Interactive mode:

```bash
$ ./console.py
```
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF all create destroy help  quit show update

(hbnb)
(hbnb)
(hbnb) quit
$
```

Non Interactive mode:

```bash
$ echo "help" | ./console.py
```
```bash
(hbnb)

Documented commands (type help <topic>):
========================================
EOF all create destroy help  quit show update
(hbnb)
$
```

As you can see in the examples we typed the command help and It shows the available commands

Interpreter or Console commands:

- create  It can create an instance of existent class
- all  It prints all instances based or not on the class name
- destroy  Deletes an instance based on the class name and ID
- show  Prints the string representation of an instance based on the class name and id
- update  Updates an instance based on the class name and id
- quit  Exit the program console
- help  Show all commands

# Examples of each command

first we run the program console.py

```bash
./console.py
```

Create an object in console

```bash
(hbnb) create BaseModel
206cfdf0-f5f1-4200-b64f-a94421dd1a3f
```

Show the object already created

```bash
(hbnb) show BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f
[BaseModel] (206cfdf0-f5f1-4200-b64f-a94421dd1a3f) {'id': '206cfdf0-f5f1-4200-b64f-a94421dd1a3f', 'created_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42546), 'updated_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42597)}
```

All the objects created
```bash
(hbnb) all
[[BaseModel] (206cfdf0-f5f1-4200-b64f-a94421dd1a3f) {'id': '206cfdf0-f5f1-4200-b64f-a94421dd1a3f', 'created_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42546), 'updated_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42597)}]
(hbnb) all BaseModel
[[BaseModel] (206cfdf0-f5f1-4200-b64f-a94421dd1a3f) {'id': '206cfdf0-f5f1-4200-b64f-a94421dd1a3f', 'created_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42546), 'updated_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42597)}]
```

Update attributes from an instance
```bash
(hbnb) update BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f first_name "Betty"
(hbnb) show BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f
[BaseModel] (206cfdf0-f5f1-4200-b64f-a94421dd1a3f) {'id': '206cfdf0-f5f1-4200-b64f-a94421dd1a3f', 'created_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42546), 'updated_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42597), 'first_name': 'Betty'}
(hbnb) update BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f first_name "Paulo"
(hbnb) show BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f
[BaseModel] (206cfdf0-f5f1-4200-b64f-a94421dd1a3f) {'id': '206cfdf0-f5f1-4200-b64f-a94421dd1a3f', 'created_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42546), 'updated_at': datetime.datetime(2019, 11, 12, 13, 47, 50, 42597), 'first_name': '"Paulo"'}
```

Destroy an object
```bash
(hbnb) destroy BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f
(hbnb) show BaseModel 206cfdf0-f5f1-4200-b64f-a94421dd1a3f
** no instance found **
(hbnb)
```

## Authors
[Daniel Rodriguez](https://github.com/dr2d4)
[Paulo Morillo](https://github.com/PauloMorillo)

## License
[MIT](https://choosealicense.com/licenses/mit/)