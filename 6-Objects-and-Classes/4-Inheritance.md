# `Python Inheritence`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

<br>

___

<br>

Covered in this file:
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()
1. [``]()

<br>

___

<br>


# `Note on symbols used in this file`:
Symbols appearing in python blocks should be treated as Python syntax.  
`...` is used as a placeholder in Python. 
```python 
... 
```

<br>

### `Variable Information`
> Text inside of `<>` should be treated as a place holder for variable information
```
  <text>    
```

<br>

### `CLI Commands`
> The `>` indicates commands to be executed in the Windows Powershell prompt
```
  > command flags arguments 
```

<br>


> The `$` indicates commands to be executed in the Linux or Mac command line interface
```
  $ command flags arguments
```

<br>

[Back to Top](#python-classes)

___

<br>

# `Object Oriented Programming `

Basically: `Object-Oriented Programming (OOP)` groups data and functions together into a class that allows for the construction of an object that has access to its own unique data values and shared functions. 

Specifically: `Object-Oriented Programming (OOP)` is a programming paradigm that is based on the concept of `objects`, which are instances of classes. In OOP, software is organized around objects, which can represent real-world entities, concepts, or abstract data types. These objects contain both data and behavior, which allows for more modular, reusable, and scalable code.



Key Concepts in Object-Oriented Programming:
| Concept| Definition |
|:-:|:-|
| `Classes`      | A blueprint or template for creating objects. It defines the data (fields) and methods (functions) that the objects created from the class will have.  |
| `Objects`     | An instance of a class that contains actual data and behaviors as defined by the class. It is a specific realization of a class.                          |
| `Abstraction`| The concept of hiding the complex implementation details and showing only the essential features of an object, simplifying interaction with it.           |
| `Encapsulation`| The bundling of data and methods into a single unit (an object) and restricting direct access to some components, often using private/protected fields.|
| `Inheritance`| A mechanism by which one class (child or subclass) can derive or inherit attributes and methods from another class (parent or superclass), promoting reusability.|
| `Polymorphism`| The ability of different objects to respond to the same method or function in different ways, typically achieved through method overriding or overloading.  |

<br>

[Back to Top](#python-inheritence)

___

<br>

# `Inheritence Defined`
Basically: `Inheritence` allows for one class (aka: subclass, child class, derived class) to  inherit the data and methods from an existing class (super class, parent class, base class) 

Specifically: `Inheritance` is a mechanism where a new class (called a child class or subclass) derives data and methods from an existing class (called a parent class, super class, or base class). 

<br>

Inhertence is yet another way to reuse code. It allows for the creation of hierarchical relationships between classes, where child classes can inherit, extend, or modify the behavior of parent classes.

| **Term** | **Description**|
|-|-|
| `Metaclass` | A class that defines the behavior and rules for other classes. In Python, a metaclass controls how classes are created, and it allows customization of class creation and initialization processes. |
| `Parent Class` <br> `Super Class` <br> `Base Class`   | The class whose properties and methods are inherited. |
| `Child Class` <br> `Subclass` <br> `Derived Class` | The class that inherits from the parent class. |
| `Method Overriding`  | A child class can override or redefine methods from the parent class to provide its own implementation. |
| `Single Inheritance` | A child class inherits from one parent class. |
| `Multiple Inheritance` | A child class inherits from more than one parent class (Python supports this). |


<br>

[Back to Top](#python-inheritence)

___

<br>

.issubclass()
isinstance()

is
is not

Supre.__init__(self, ...)
super().__init__(...)
s


# `Single Inheritence`

 the subclass is able to modify its superclass behavior (just like in the example) is called polymorphism.

 inheritance extends a class's capabilities by adding new components and modifying existing ones; in other words, the complete recipe is contained inside the class itself and all its ancestors; the object takes all the class's belongings and makes use of them;

# `Multilevel Inheritence`


# `Multiple Inheritence` 
bottom to top overriding

class Sub(Super1,Super2) inherits left to right, overrides left to right.

# `Method Overriding`

# `Abstract Classes and Methods`

# `Composition`
composition projects a class as a container able to store and use other objects (derived from other classes) where each of the objects implements a part of a desired class's behavior.

```python
import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)
```


Error:
```python
class Top:
    def m_top(self):
        print("top")


class Middle(Top):
    def m_middle(self):
        print("middle")


class Bottom(Top, Middle):
    def m_bottom(self):
        print("bottom")


object = Bottom()qwa
object.m_bottom()
object.m_middle()
object.m_top()

```
Method Resolution Order
MRO, in general, is a way (you can call it a strategy) in which a particular programming language scans through the upper part of a class’s hierarchy in order to find the method it currently needs. It's worth emphasizing that different languages use slightly (or even completely) different MROs. Python is a unique creature in this respect, however, and its customs are a bit specific.

We're going to show you how Python's MRO works in two peculiar cases that are clear-cut examples of problems which may occur when you try to use multiple inheritance too recklessly.



Diamond problem
```python
class Top:
    def m_top(self):
        print("top")


class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")


class Middle_Right(Top):
    def m_middle(self):
        print("middle_right")


class Bottom(Middle_Left, Middle_Right):
    def m_bottom(self):
        print("bottom")


object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
```

