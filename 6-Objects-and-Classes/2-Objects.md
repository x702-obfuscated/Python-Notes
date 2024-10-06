
# `Python Objects`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works.*
<br>

___

<br>

Covered in this file:
1. [`Example Class Definition`](#example-class-definition)
1. [`Importing a Class from another file`](#importing-a-class)
1. [`Objects Defined`](#objects-defined)
1. [`Constructing Objects`](#constructing-objects)
1. [`Built-in Constructors`](#built-in-constructors)
1. [`Instance Variables`](#instance-variables)
    1. [`Accessing Instance Variables`](#accessing-instance-variables)
1. [`Class Variables`](#class-variables)
    1. [`Accessing Class Variables`](#accessing-class-variables)
1. [`Methods`](#methods)
    1. [`Calling a Method`](#calling-a-method)
1. [`Built-in function for Objects`](#built-in-functions-for-objects)
    1. [`type() Return an object's class`](#type-return-an-objects-class)
    1. [`isInstance() checks and object's class`](#isinstance-checks-an-objects-class)
    1. [`id() Returns an object's memory address`](#id-returns-an-objects-memory-address)
    1. [`help() Outputs an object's help info`](#help-outputs-an-objects-help-info)
    1. [`dir() Returns and object's attributes`](#dir-returns-an-objects-attributes)
    1. [`vars() Returns and object's variables`](#vars-returns-an-objects-variables)


<br>

___

<br>

# `Example Class Definition`

*Assume the class written below is defined in a file called player.py that exists in the same directory as this file. This is so we can focus on the objects themselves and not the class that defines them.*

*You can always refer back to this class definition if you are confused about what a 'Player' is and does.*

```python
import random

class Player():
    '''Defines a 'Player' of a classic role playing game.'''

    num_of_players = 0      # Class Variable

    @classmethod
    def from_dict(cls, player_info):
        '''Class Methods, returns a Player instance from a passed dictionary'''
        name = player_info["name"]
        health = player_info["health"]
        magic = player_info["magic"]
        stamina = player_info["stamina"]
        speed = player_info["speed"]

        return cls(name,health,magic,stamina,speed)


    def __init__(
        self, name = "Hero", health = 100, 
        magic = 50, stamina = 75, speed = 1
    ):
        '''Constructor: creates a Player instance'''
        Player.num_of_players += 1
        self.name = name                    # Instance Variable
        self.health = health                # Instance Variable
        self.magic = magic                  # Instance Variable
        self.stamina = stamina              # Instance Variable
        self.speed = speed                  # Instance Variable

        self.equipped_weapon = None         # Instance Variable
        self.equipped_armor = None          # Instance Variable
     
        self.bag = {                        # Instance Variable
            "Key Items":[],
            "Weapons":[],
            "Armor":[],
            "Potions":[],
        }
    


    def roll_dice(self, number = 1 , d = 20):
        '''Method to simulate dice roll'''
        rolls = []
        for n in range(number):
            rolls.append(random.randint(1,d))
        
        return max(rolls)

    def initiative(self):
        '''Method to roll for initiative'''
        roll = roll_dice()
        return roll + speed


    def attack(self,weapon_modifier, difficulty = 1):
        '''Method to return attack damage value'''
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * weapon_modifier

    def defend(self, armour_modifier, difficulty= 1):
        '''Method to return defense attempt value'''
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * armor_modifier
    
    def flee(self, difficulty_modifier = 1):
        '''Method to return flee attempt value'''
        roll = roll_dice()
        if roll <= difficulty:
            return 0
        return roll * speed

    def open_bag(self):
        '''Method to return the bag contents''' 
        return self.bag

    def display_vars(self):
        '''Method to display all instance variables'''
        for key, item in vars(self).items():
            print(f"{key} : {item}")
```

<br>

[Back to Top](#python-objects)

___

<br>

# `Importing a Class`
To use a `class` that is not defined in the current file (module), you must import the `class` from another file (`module`).

`In most cases importing should occur at the very top of your .py file.` 

syntax:

    from <module> import <Class>

real example:
```python
from player import Player
```

<br>

`Modules are files`

*If the module with the class definition is not in the same folder, you will need to better understand importing --> See 7-Advanced/Importing-Code*


<br>

[Back to Top](#python-objects)

___

<br>


# `Objects Defined`
`In Python everything is an object` 

Basically: `Objects` are an `instances of a class` that contain `data` and `methods` (functions) that operate on that data. 


Specifically: `Objects` are an `instances of a class` that encapsulate `data` and `methods` (functions) that operate on that data. `Objects` are created by using the class `constructor`, which uses the class 'blueprint' to build the `object`.  

<br>

* Objects follow variable naming conventions (`lower_snake_case`)  
* `Objects` are built using `Constructors`, and constructing an object is called `Instantiation` 
* Every instance of a class has the same attributes, but the values for those attributes may be different.  

<br>

### *`'Instance of a class' and  'object' mean the same thing.`*

*When we say "everything is an object", we mean that every piece of data (variables, functions, classes, modules, etc.) in Python are represented by an object in memory.*

<br>

[Back to Top](#python-objects)

___

<br>



# `Constructing Objects`

`Objects` are created by calling a class `constructor`.
The class `constructor` builds the `object` in memory and returns a reference to its memory location. Therefore `objects` are typically created and assigned to a variable.

Constructing an object is called `instantiation`.

instantiation syntax:
```
ClassName(arguments, ...)
```

<br>

instantiation and assignment syntax:
```
object_name = ClassName(arguments, ...)
```

example:
```python
from player import Player 
''' 
The class definition is placed in another location 
so that we can focus on how objects are handled.
'''

# Constructing a Player instance
Player()                                  
```
```python
from player import Player 
''' 
The class definition is placed in another location 
so that we can focus on how objects are handled.
'''

# Constructing and assigning a Player instance
player1 = Player()      
# player1 now holds the reference to a Player object.

#                                       module.Class
print(type(player1)) # Output:  <class 'player.Player'>
```



<br>

[Back to Top](#python-objects)

___

<br>

# `Built-in Constructors`
You have most likely already used some built-in constructors without knowing it. These are constructors for classes defined by the Standard Library

| **Function** | **Description**|
|------------------|--------------------------------------------------------------------------------------------------------------------|
| `int()`| Constructs an integer object with a default value of 0.|
| `float()`| Constructs a float object with a default value of 0.0. |
| `bool()` | Constructs a boolean object with a default value of `False`. |
| `str()`| Constructs an empty string object. |
| `list()` | Constructs an empty list object. |
| `tuple()`| Constructs an empty tuple object.|
| `set()`| Constructs an empty set object.|
| `dict()` | Constructs an empty dictionary object. |
| `complex()`| Constructs a complex number object. It takes two optional arguments: `real` and `imag`.|
| `bytes()`| Constructs a bytes object from an optional iterable of integers representing byte values.|
| `range()`| Constructs a range object that represents a sequence of numbers. It can take up to three arguments: `start`, `stop`, and `step`. |
| `frozenset()`| Constructs an immutable set object from an optional iterable.|
| `memoryview()` | Constructs a memory view object that exposes the buffer interface of an object.|
| `enumerate()`| Constructs an enumerate object that pairs each element of an iterable with its index.|
| `filter()` | Constructs an iterator that filters elements from an iterable based on a function. |
| `map()`| Constructs an iterator that applies a function to every item of an iterable, yielding the results. |
| `zip()`| Constructs an iterator that aggregates elements from multiple iterables into tuples. |
| `super(None)`| Constructs a super object, typically used for delegating method calls to a superclass.|



<br>

[Back to Top](#python-objects)

___

<br>

# `Instance Variables`

*`what an object is`*

Basically: `Instance Variables` are variables associated with an instance of a class (object)

Specifically: `Instance Variables` are variables that store a unique state associate with an instance of a class, typically defined within the constructor `__init__` method.

<br>

*The name of an instance variable is the same for every instance of the class, but the data referenced be each name is different for each instance of the class.*

For example:  
Every `Player` will have `hp`, but each individual `Player` may have a different value for `hp`.

<br>

## `Accessing Instance Variables`
Instance variables can be accessed using the object variable name, dot syntax, and the instance variable name. 

syntax:
```
object_name.variable_name
```

<br>

```python
from player import Player

player1 = Player()

# Instance Variable Access
player1.name               # Returns: Hero
```


<br>

[Back to Top](#python-objects)

___

<br>

# `Class Variables`

Basically: A `Class Variable` is a variable shared among all instances of a class.  

Specifically `Class Variables` are variables that are associated with a class and shared among all instances of a class. They have the same value for all instances of that class. 

<br>

`Class Variables are shared among all instances of a class.` 

<br>

## `Accessing Class Variables`
Class variables can be accessed with the class name or with any object of the class, dot syntax,  and the variable name. 

<br>

syntax for accessing variables associated with the class:
```
ClassName.variable_name
``` 
OR
```
object_name.variable_name
```

<br>

example:
```python
from player import Player

player1 = Player()
player2 = Player()

player1.num_of_players      # Returns: 2
player2.num_of_players      # Returns: 2

Player.num_of_players       # Returns: 2
```
<br>

[Back to Top](#python-objects)

___

<br>

# `Methods`
Basically: `Methods` are functions defined by a class.

Specifically: `Methods` are functions that are associated with an object or class. They define behaviors or actions that an object can perform and usually operate on the data contained within that object. Methods are often used to encapsulate functionality and data within an object-oriented programming (OOP) paradigm. 

<br>

### *`Methods use the same syntax as functions.`*

<br>

[Back to Top](#python-objects)

___

<br>

## `Calling a Method`
Methods are called using an object or class and dot `.` syntax

*`Aside from using dot syntax, methods are called the same way as functions. `*

calling instance methods: 
syntax :  
```
object_name.method_name(arguments, ...)
```
example:
```python
from player import Player

player1 = Player()

# Calling the attack() method
player1.attack()
```

<br>

calling class methods: 
syntax :  
```
ClassName.method_name(arguments, ...)
```
example:
```python
from player import Player

player_dict = {
    "name": "Hero",
    "health": 200,
    "magic": 150,
    "stamina":175,
    "speed": 10
}
#         Calling class method from_dict()
player1 = Player.from_dict(player_dict)
```

<br>

[Back to Top](#python-objects)

___

<br>

# `Built-in functions for Objects`

## `type() Return an object's class`

syntax:
```
type(object)
```

The `type()` function shows what class each object belongs too:

### Built-in Data Types
```python
type(10)              # Returns: <class 'int'>
type(3.14)            # Returns: <class 'float'>
type(True)            # Returns: <class 'bool'>
type("Hello")         # Returns: <class 'str'>
type(["a","b","c"])   # Returns: <class 'list'>
type(("a","b","c"))   # Returns: <class 'tuple'>
type({"a","b","c"})   # Returns: <class 'set'>
type({"a":1,"b":2})   # Returns: <class 'dict'>
type(range(10))       # Returns: <class 'range'>
type(bytes(b"hello")) # Returns: <class 'bytes'>
```

<br>

### Built-in Functions
```python
type(print)     # Returns: <class 'builtin_function_or_method'>
```

<br>

### Built In Modules
```python
import math

type(math)      # Returns: <class 'module'>
type(math.pi)   # Returns: <class 'float'>
type(math.sqrt) # Returns: <class 'builtin_function_or_method'>
```

### Written by User
```python
import player

var = None

def fun():
    pass

class Cls():
    pass

obj = Cls()

player1 = player.Player()

type(var)               # Returns: <class 'NoneType'>
type(fun)               # Returns: <class 'function'>
type(Cls)               # Returns: <class 'type'>
type(obj)               # Returns: <class '__main__.Cls'>

type(player)            # Returns: <class 'module'>
type(player.Player)     # Returns: <class 'type'>
type(player1)           # Returns: <class 'player.Player'>
type(player1.name)      # Returns: <class 'str'>
type(player1.attack)    # Returns: <class 'method'>
```
*In Python, `<class 'type'>` is the `metaclass` from which all classes are created. A `metaclass` is a class of a class, meaning it defines how classes behave. Since Python treats classes as first-class objects, every class in Python is an instance of `type`.*

*`__main__` is a reference to the current module (file)*

<br>

[Back to Top](#python-objects)

___

<br>

## `isInstance() checks an object's class`
isInstance() checks if an object is apart of a particular class.
```
isInstance(object,class)
```
```python
isInstance(10,int)      # Returns: True
isInstance(5,str)       # Returns: False
```

<br>

[Back to Top](#python-objects)

___

<br>

## `id() Returns an object's memory address`
id() returns a unique integer representing the memory address of an object.

```
id(object)
```
```python
from player import Player

player1 = Player()


id(player1)     # ex Return: 2072725232032    (this will vary)
```

<br>

[Back to Top](#python-objects)

___

<br>

## `help() Outputs an object's help info`
help() displays an object's class docstring and general information.

```
help(object)
```
```python
help(print)

# Outputs:
# Help on built-in function print in module builtins:

# print(*args, sep=' ', end='\n', file=None, flush=False)
#     Prints the values to a stream, or to sys.stdout by default.
```

<br>

[Back to Top](#python-objects)

___

<br>


## `dir() Returns an object's attributes`
dir() returns a list of all an objects attributes including:
* defined methods and data
* inherited methods and data
* special dunder `__` methods and data



syntax:
```
dir(object)
```
```python
from player import Player

player1 = Player()

dir(player1)

# Returns: 
[
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
'__eq__', '__format__', '__ge__', '__getattribute__',
'__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__weakref__', 'attack', 'bag', 'defend',
'display_attributes', 'equipped_armor', 'equipped_weapon',
'flee', 'health', 'initiative', 'magic', 'name', 'open_bag',
'roll_dice', 'speed', 'stamina'
]
```

<br>

[Back to Top](#python-objects)

___

<br>

## `vars() Returns an object's variables`
vars() returns a dictionary of an object's data members (fields aka variables).

```
vars(object)
```

```python

from player import Player

player1 = Player()

vars(player1)
# Returns:
{
'name': 'Hero', 'health': 100, 'magic': 50, 'stamina': 75, 
'speed': 1, 'equipped_weapon': None, 'equipped_armor': None, 
'bag': {'Key Items': [], 'Weapons': [], 'Armor': [], 'Potions': []}
}
```


<br>

[Back to Top](#python-objects)

___

<br>

*Created and maintained by Mr. Merritt*