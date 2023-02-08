# AirBnB_clone


# About
This project is the first step in the AirBnB project for the Holberton School Higher Level Programming course. This project entails building a custom command line interpreter. 

# Console
The console is the command line interface which allows the user to make allowed classes, delete classes, and add attributes to those classes. This console is available in both interactive and non-interactive mode.


# How to use the console
## Interactive Mode

First launch the console:

```
/holbertonschool-AirBnb_clone$ ./console.py
```

Once launced you will be presented with a new (hbnb) prompt ready to accept commands.
When executed the user is presented with the prompt "hbnb" which means it is ready to accept commands.

Example:<br>
```
(hbnb) create BaseModel
```

## Non-Interacive Mode<br>

To use non-interactive mode use 'echo' to use the commands and pipe them to console.py

Example:<br>
```
AirBnb_clone$ echo "create BaseModel" | ./console.py
```

# Commands

## help -- shows help
### Usage:
Find a list of documented commands:<br>
> help

Find help about a specific command<br>
> help 'command'

Example:<br>
```
(hbnb) help create
```

## create -- create an allowed class
### Usage:
> create 'class name'<br>

Example:<br>
```
(hbnb) create BaseModel
```

## destroy -- delete a specific instance of a class from id
### Usage:
> destroy 'class name' 'ID'<br>


## show -- print a string representation of an object
### Usage:
> show 'class name' 'ID'<br>

## all -- print a string representation of all objects or all objects of a specific class
### Usage:
To show all objects:<br>
> all

To show objects of a specific class<br>
> all 'class name'

## update -- update an instance
### Usage:
> update 'class name' 'ID' 'attribute' '"attribute value"'


## quit -- quit the console
### Usage:
> quit

Example:<br>
```
(hbnb) quit
```

## EOF -- quit the console
### Usage:
Press Ctrl + D on keyboard<br>
<br>

# Classes
## List of allowed classes
```
Amenity
BaseModel
City
Place
Review
State
User
```
<br>

##  Authors:

> Taylor Joyner: [Github](https://github.com/TJonCanon)

> Jacob Marshall: [Github](https://github.com/JacobM311)