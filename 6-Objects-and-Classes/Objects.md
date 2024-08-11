*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

# `Objects`

Covered in this file:
1. Importing a Class
1. Objects Defined
1. Calling Constructors: Building Objects
1. Built-in Constructors
1. Instance Variables : Attributes 
1. Instance Methods : Functions

***Assume the class written below is defined in a file called Classes.py that exists in the same directory as this file. We will not rewrite this code repeatedly to save space.***

```python
class Player():

    def __init__(self):
        ...

```

<br>

# `Importing a Class`
> * To use a class that is not defined in the same file, you must import the class from another file.

syntax:

    from Module import Class

real example:
```python
from Classes import Player
```

> * Modules are files
> * If the module with the class definition is not in the same folder, you will need to better understand importing --> See 7-Advanced/Importing-Code


<br>

# `Objects Defined`
In Python everything is an object 
> You have already been using objects  
> When we say "everything is an object", we mean that every piece of data (variables, functions, classes, modules, etc.) in Python is represented by an object in memory.

The type() function show what class each object belongs too:
```python
type(10)              #<class 'int'>
type(3.14)            #<class 'float'>
type(True)            #<class 'bool'>
type("Hello")         #<class 'str'>
type(["a","b","c"])   #<class 'list'>
type(("a","b","c"))   #<class 'tuple'>
type({"a","b","c"})   #<class 'set'>
type({"a":1,"b":2})   #<class 'dict'>
type(range(10))       #<class 'range'>
type(bytes(b"hello")) #<class 'bytes'>
```

## Objects
Are built from the Class blueprint
> * basically: an instance of a class that contains data and the methods that operate on that data.  
> * specifically: an instance of a class with its own unique state and behaviour as defined by the class.   

> * Objects follow variable naming conventions (lower_snake_case)  
> * Constructing an object is called Object Instantiation    

***NOTE: An instance of a class and an object are the same thing.***

<br>

# `Calling Constructors: Building Objects`

syntax for object instantiation:
```
ClassName(arguments, ...)
```
syntax for object instantiation and assignment:
```
object_name = ClassName(arguments, ...)
```

abstract example:
```python
from Classes import Player 
''' 
This hides the class definition in another location 
so that we can focus on how the objects are used.
'''

# Constructing a Player instance
Player()                            # Object Instantiation            

# Constructing and assigning a Player instance
player1 = Player()                  # Object Instantiation and Assignment


#                                       Module.Class
print(type(player1)) # Output: <class 'Classes.Player'>
```
```python
from Classes import Player 
''' 
This hides the class definition in another location 
so that we can focus on how the objects are used.
'''   

# This builds the object in memory and creates a reference
Player()            


# This builds the object, creates a reference, 
# and stores that reference in a variable for later access
player1 = Player()  

```

<br>

# `Built-in Constructors`
> * You have most likely already used some built-in constructors without knowing it.
> * These are constructors for classes defined by the Standard Library

```python
int()            # Constructs an integer object with a default value of 0.
float()          # Constructs a float object with a default value of 0.0.
bool()           # Constructs a boolean object with a default value of False.
str()            # Constructs an empty string object.
list()           # Constructs an empty list object.
tuple()          # Constructs an empty tuple object.
set()            # Constructs an empty set object.
dict()           # Constructs an empty dictionary object.
complex()        # Constructs a complex number object. It takes two optional arguments: real and imag.
bytes()          # Constructs a bytes object from an optional iterable of integers representing byte values.
range()          # Constructs a range object that represents a sequence of numbers. It can take up to three arguments: start, stop, and step.
frozenset()      # Constructs an immutable set object from an optional iterable.
memoryview()     # Constructs a memory view object that exposes the buffer interface of an object.
enumerate()      # Constructs an enumerate object that pairs each element of an iterable with its index.
filter()         # Constructs an iterator that filters elements from an iterable based on a function.
map()            # Constructs an iterator that applies a function to every item of an iterable, yielding the results.
zip()            # Constructs an iterator that aggregates elements from multiple iterables into tuples.
super(None)      # Constructs a super object, typically used for delegating method calls to a superclass.
```
# `Attributes: Variables  `
> * Instance Variable: This is a variable that is defined inside a class and is specific to an instance of the class.
> * Attribute: This is a more general term that refers to any property or method associated with an object.  

## Attributes
> * data values that are associated with a class or object that define its state or properties
> * are typically accessed using an object or class and dot ( . ) syntax

### Instance Variables
syntax for assigning variables associated with an instance:

    self.variable_name = ...

syntax for accessing variables associated with an instance:

    object_name.variable_name

<br>

### Class Variables
syntax for assigning variables associated with a class:

    variable_name = ...

syntax for accessing variables associated with the class:

    ClassName.variable_name

<br>

# `Attributes: Methods (functions)`
## Methods
> * basically: functions that are defined by a class
> * specifically: functions defined within a class that operate on instances of that class and can access and modify their state

## Defining Methods:
```
class ClassName():

    def method_name():
        ...
```
real example:
```python
class Player:
    def __init__(self):
        self.atk = 10


    def fight(self):
        '''Method'''
        print(f"The player does {self.atk}pt(s) of damage")
```

<br>

## Calling Methods
calling methods associated with an instance  
syntax :  

    object_name.method_name(arguments, ...)

calling methods associated with the class  
syntax :  

    ClassName.method_name(arguments, ...)

real method example:
```python
class Player():                         # Class Header

    def __init__(self):                 # Constructor Header
        self.name = "default_player"    # instance variable
        self.hp = 100                   # instance variable
        self.mp = 50                    # instance variable
        self.stamina = 75               # instance variable

    def display_attributes(self):
        '''Instance Method for displaying the variable in a Player object'''
        attributes = vars(self)
        for var in attributes:
            print(f"{var}: {attributes[var]}", end = " | ")

# end of class definition

# Constructing a Player instance with the name player1
player1 = Player()                      

# Displaying instance variables and thier values
player1.display_attributes() 
# Output: name: default_player | hp: 100 | mp: 50 | stamina: 75 |         

```

## Built-in Methods

Built-in methods are pre-defined by classes pre-defined by the standard library

To see what methods you can call on an object use:  
    
    dir(object_name)  

To see more information on a specific method use:  
    
    help(object_name.method_name)


<br>