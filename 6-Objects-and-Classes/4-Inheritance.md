*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python Inheritence`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

<br>

___

<br>

Covered in this file:
1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Object Oriented Programming`](#object-oriented-programming)
1. [`Inheritence Defined`](#inheritence-defined)
1. [`Single Inheritence`](#single-inheritence)
1. [`Constructor Inheritence`](#constructor-inheritence)
    1. [`super()`](#super)
1. [`Method Overriding`](#method-overriding)
1. [`Access Modifiers`](#access-modifiers)
1. [`Multilevel Inheritence`](#multilevel-inheritence)
1. [`Method Resolution Order`](#method-resolution-order)
1. [`Multiple Inheritence`](#multiple-inheritence)
1. [`Composition`](#composition)
1. [`Abstract Class and Methods`](#abstract-classes-and-methods)

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
Basically: `Inheritence` allows for one class (aka: subclass, child class, derived class) to  inherit the data and methods from an existing class (aka: super class, parent class, base class) 

Specifically: `Inheritance` is a mechanism where a new class (aka: subclass, child class, derived class) derives data and methods from an existing class (aka: super class, parent class, base class). 

<br>

Inhertence is another way to reuse code without duplication. It allows for the creation of hierarchical relationships between classes, where child classes can inherit, extend, or modify the behavior of parent classes.

| **Term** | **Description**|
|-|-|
| `Metaclass` | A class that defines the behavior and rules for other classes. In Python, a metaclass controls how classes are created, and it allows customization of class creation and initialization processes. |
| `Parent Class` <br> `Super Class` <br> `Base Class`   | The class whose properties and methods are inherited. |
| `Child Class` <br> `Subclass` <br> `Derived Class` | The class that inherits from the parent class. |
| `Method Overriding`  | A child class can override or redefine methods from the parent class to provide its own implementation. |
| `Single Inheritance` | A child class inherits from one parent class. |
| `Multiple Inheritance` | A child class inherits from more than one parent class (Python supports this). |

<br>

By default all classes in Python inherit from a built-in base class called `object`.
* Therefore every class is a child class of `object`
* Every class is also an object of class `type`

You can check the parent class of any class by accessing the `__bases__` attribute.

```python
class MyClass():
    pass


print(MyClass.__bases__)            # Output: (<class 'object'>,)
print(issubclass(MyClass,object))   # Output: True

print(type(MyClass)) # Output: <class 'type'>
```



<br>

[Back to Top](#python-inheritence)

___

<br>

# `Single Inheritence`
Single Inheritence refers to once class inheriting from a single parent class.

A child class:
* inherits attributes (variables and methods) from a parent class
* extends (adds to) the inherited attributes
* can modify the behaviour (methods) inherited from the parent class. (polymorphism)
* estabilshes a "is-a" relationship (Subclass is a Super class)

<br>

When learning about inheritence it can be difficult to keep all of the ducks in a row. 
The function below can be used to help you understand the relationships for any class you encounter. 
```python
def show_info(name:str=None,ignore_special:bool=True)-> None:
    '''
    Displays and returns detailed info about a given object

    Parameters:
    name (str) : The variable identifier associated with the object
    ignore_special (bool, optional) : If True ignores dunder '__' attributes
    '''

    import os
    
    if name in locals():
        obj = locals.get(name)
    elif name in globals():
        obj = globals().get(name)
    else:
        print(f"'{name}' Object Could Not Be Found")
        return 


    attributes = dir(obj)

    if ignore_special:
        attributes = list(filter(lambda atr : "__" not in atr, attributes))

    module = obj.__class__.__module__

    if module == "__main__":
        module = __file__.split(os.sep)[-1].replace(".py","")

    s = (
        f"Identifier: {name}",
        f"Class Module: {module}",
        f"Class: {obj.__class__}",
        f"Inherits From: {obj.__class__.__bases__}",
        f"Attributes: {attributes}"
    )

    print(*s,sep = "\n",end="\n\n")
```
```python
class Example():
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3


    def do_stuff(self):
        print("Doing stuff...")


obj = Example()
show_info("obj")
# Output:
# Identifier: obj
# Class Module: main
# Class: <class '__main__.Example'>
# Inherits From: (<class 'object'>,)
# Attributes: ['do_stuff', 'x', 'y', 'z']
```

<br>

## `Inherit`
A child class inherits the attributes (variables and methods) of its parent 
* To inherit from another class, pass the identifier of the parent class as an argument to the child class.

Syntax
```
class Parent:
    ...

class Child(Parent):
    ...
```

```python
class Parent():
    def __init__(self):
        self.variable = "This variable comes from Parent"

    def method(self):
        print("This method comes from Parent")


class Child(Parent):
    def __init__(self):
        super().__init__()



obj = Child()       # Constructing a Child object
print(obj.variable) # Output: This variable comes from Parent
obj.method()        # Output: This method comes from Parent
```

<br>

## `Extend`
A child class extends the functionality of the parent class from which it inherits attributes. 
* This means a child class adds its own attributes


The child class can add new variables and methods while also having access the parent class attributes. 
* The parent class will not have access to child class attributes. 
```python
class Parent():
    def __init__(self):
        self.variable = "This variable comes from Parent"

    def method(self):
        print("This method comes from Parent")


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.new_variable = "This variable comes from Child"

    def new_method(self):
        print("This method comes from Child")


parent = Parent()           # Construct and assign a Parent object
print(
    parent.variable,        # Output: This variable comes from Parent
    parent.new_varaible     # Output: AttributeError: 'Parent' object has no attribute 'new_varaible'
)

parent.method()             # Output: This method comes from Parent
parent.new_method()         # Output: AttributeError: 'Parent' object has no attribute 'new_method's


child = Child()             # Construct and assign a Child object

print(
    child.variable,         # Output: This variable comes from Parent
    child.new_variable,     # Output: This variable comes from Child
)

child.method()              # Output: This method comes from Parent
child.new_method()          # Output: This method comes from Child
```

<br>

## `Modify`
A child class can modify the functionality of the methods inherited from a parent class.
* This is a form of polymorphism.

This is called `method overriding`. 

```python
class Parent():
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"{self.name} acts like a Parent.")


class Child(Parent):
    def __init__(self,name):
        super().__init__(name)

    def action(self,act=None):
        '''Overrides action() with new functionality'''
        if act is None:
            super().action() # Calls the Parent version of action()
        else:
            print(f"{self.name} {act}")



parent = Parent("parent")
child = Child("child")

parent.action()                     # Output: parent acts like a Parent

child.action()                      # Output: child acts like a Parent
child.action("acts like a Child.")  # Output: child acts like a Child
```

Here the Child class overrides the function of its inherited method 'action'.

<br>

[Back to Top](#python-inheritence)

___

<br>

# `Constructor Inheritence`
A child class by default inherits the constructor (`__init__`) method of its parent. 

```python
class Parent():
    def __init__(self, name="Parent"):
        self.name = name

class Child(Parent):
    pass

child = Child("Bob")
print(child.name)       # Output: Bob
```

<br>

The child class can override the constructor (`__init__`) of its parent class to add new functionality.
1. To intialize the inherited parent attributes call `super().__init__()`

*`The parent constuctor should be called at the beginning of the child constructor to ensure all parent attributes are intialized before an specific child class attributes.`*

*`To properly inherit the parent class attributes super().__init__() must be called`*

```python
class Parent():
    def __init__(self, name="Parent"):
        self.name = name


class Child(Parent):

    def __init__(self, 
        name="Child",
        age=0
    ):
        super().__init__(name)     #Calling the Parent Constructor and passing name
        self.age = age


child = Child("Bob",30)
print(child.name)                  # Output: Bob
print(child.age)                   # Output: 30
```

<br>

## `super()`
The `super()` function in Python is used to access attributes (methods/variables) of a parent class.
* super() is the constructor for a special `super` builtin class.
* super() returns a proxy object that acts as a intermediary between the current object, and the parent class. 
* essentially it is a reference to the parent class attributes


```python
class Parent():

    def __init__(self):
        pass

class Child(Parent):
    
    def return_super(self):
        return super()

sup = Child().return_super()

show_info("sup") # Using the show_info() function provided in these notes
# Identifier: sup
# Class Module: builtins
# Class: <class 'super'>
# Inherits From: (<class 'object'>,)
# Attributes: []
```

<br>

Use `super()` to call the methods of the parent class.

```python
class Parent():
    def __init__(self, name):
        self.name = name

    def action(self):
        print(f"{self.name} acts like a Parent.")


class Child(Parent):
    def __init__(self,name):
        super().__init__(name)  # Calls the Parent constructor passing `name` as an argument

    def action(self,act=None):
        '''Overrides action() with new functionality'''
        if act is None:
            super().action()    # Calls the Parent version of action()
        else:
            print(f"{self.name} {act}")



parent = Parent("parent")
child = Child("child")

parent.action()                     # Output: parent acts like a Parent

child.action()                      # Output: child acts like a Parent
child.action("acts like a Child.")  # Output: child acts like a Child
```

<br>

[Back to Top](#python-inheritence)

___

<br>

# `Method Overriding`
`Method overriding` occurs when a child class provides a specific implementation of a method that is already defined in its parent class, replacing or extending the parent’s behavior.
1. Methods must have the same name. 
1. The child version of the method can use `super()` to call the parent version.

```python
class Parent():
    def __init__(self, name):
        self.name = name

    def action(self):
        print("Parent version of action()")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    
    def action(self):
        '''Overriding action()'''
        print("Child version of action()")  
        super().action()                    # Calling Parent version



child = Child("Alice")
child.action()
# Output:
# Child version of action()
# Parent version of action()
```

<br>

[Back to Top](#python-inheritence)

___

<br>

# `Access Modifiers`
`Access modifiers` in Python determine the accessibility and visibility of class attributes and methods from outside the class, using naming conventions (e.g., `public`, `protected`, `private`) instead of explicit keywords like in other languages.

<br>

## `Public`
Public variables and methods are accessible from anywhere. No prefixing.
1. This includes classes that inherit from this base class.     

syntax : 
```
def method_name():
    ...
```
real example:
```python
class Player:
    def __init__(self):
        self.atk = 10

    #Public Method
    def fight(self):
        print(f"The player does {self.atk}pt(s) of damage")
```

<br>

## `Protected`
Protected variables and methods are indicated by a single underscore `_` prefix, suggesting that it should not be accessed directly outside of the class and its subclasses.
1. These attributes are not intended for use outside of the class hierarchy.

*This is just a convention and is not actually enforced by the Python interpreter*

syntax:
```
def _method_name():
    ...
```
real example:
```python
class Player:
    def __init__(self, name, hp, mp, stamina):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina

    def regenerate_health(self, amount):
        '''Public method to regenerate health.'''
        self._calculate_regen_rate()
        self.hp += amount
        if self.hp > 100:  # Assuming 100 is the maximum health
            self.hp = 100

    #Protected Method
    def _calculate_regen_rate(self):
        '''
        Protected method to calculate regeneration rate based on stamina.
        '''
        regen_rate = self.stamina * 0.1  # Example calculation
        print(f"Regeneration rate is: {regen_rate}")


player1 = Player("Eldrin the Brave", 50, 70, 85)

player1.regenerate_health(20)   # Output: Regeneration rate is: 8.5
print(player1.hp)               # Output: 70
```

<br>

## `Private`
Indicated by a double underscore `__` prefix, suggesting that it should not be accessed from outside of the class. 
1. Trying to access the private method or attribute directly will result in an `AttributeError` 
1. private attributes are not directly accessible by derived classes. 


<br>
 
When you define a method or attribute with a name that starts with double underscores, Python internally changes the name by prefixing it with _ClassName, this is called `name mangling`. 

<br>

syntax:
```
def __method_name():
    ...
```
real example:
```python
class Player:
    def __init__(self, name, hp, mp, stamina):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina
        self.__secret_score = 0

    def perform_action(self, action_value):
        '''Public method that performs an action and updates the secret score.'''
        self.hp -= action_value  # Example action affecting health
        self.__update_secret_score(action_value)

    def __update_secret_score(self, value):
        '''Private method to update the secret score.'''
        self.__secret_score += value
        print(f"Secret score updated to: {self.__secret_score}")


player1.__update_secret_score(5)  # Raises: AttributeError


# Name mangling allows access, but it's not recommended
player1._Player__update_secret_score(5)  # Output: Secret score updated to: 15
``` 


<br>

`Private attributes are not directly accessible by derived classes.`
1. Name mangling provides access, but is not recommended.

```python
class Parent():
    def __init__(self, name):
        self.name = name

    def __action(self):
        print("Parent version of action()")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

        super().__action() # AttributeError: 'super' object has no attribute '_Child__action'
```
```python
class Parent():
    def __init__(self, name):
        self.name = name

    def __action(self):
        print("Parent version of action()")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

child = Child("Alice")

child.__action() # AttributeError: 'Child' object has no attribute '__action'
```

`Name Mangling to provide access, NOT RECOMMENDED.`

```python
class Parent():
    def __init__(self, name):
        self.name = name

    def __action(self):
        print("Parent version of action()")


class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

        super()._Parent__action() # Output: Perent version of action()
        

child = Child("Alice")

child._Parent__action()     # Output: Parent version of action()
```

<br>

[Back to Top](#python-inheritence)

___

<br>


# `Multilevel Inheritence`
Multilevel Inheritence involves a child class that inherits from a parent class which in turn inherits from its own parent class. 


```python
class GrandParent:
    def __init__(self,family_name):
        print("GrandParent() called.")
        self.family_name = family_name


class Parent(GrandParent):
    def __init__(self,family_name):
        print("Parent() called.")
        super().__init__(family_name) # Calls the GrandParent() constructor
        

class Child(Parent):
    def __init__(self, family_name):
        print("Child() called.")
        super().__init__(family_name) # Calls the Parent() constructor




child = Child("Smith")

print(child.family_name)  
# Output: 
# Child() called.
# Parent() called.
# GrandParent() called.
# Smith
```

<br>

It is not possible to directly access attributes from a GrandParent class using `super()`. If it is necessary to access a GrandParent attribute directly you will need to  us the name of the class. 
1. When accessing attributes this way, you must pass `self` to the method.
1. Generally this is not recommended as it breaks the inheritence chain (MRO)
1. Composition may make more sense in your use case.

```python
class GrandParent:
    def __init__(self,family_name):
        self.family_name = family_name


    def action(self):
        print("GrandParent action")

class Parent(GrandParent):
    def __init__(self,family_name):
        super().__init__(family_name) 

    def action(self):
        print("Parent action")
        

class Child(Parent):
    def __init__(self, family_name):
        super().__init__(family_name) 

    def action(self):
        GrandParent.action(self)      # Directly access the GrandParent action()


child = Child("Smith")

child.action()                        # Output: GrandParent action
```


<br>

[Back to Top](#python-inheritence)

___

<br>


# `Method Resolution Order`
`Method Resolution Order (MRO)` is the name given to how Python resolves methods through scanning each part of a class' hierarchy to find the method to execute. 
1. Different languages tend to use different MROs
1. Understanding MRO is necessary for working with Multilevel and Multiple Inheritence.

There are two ways to see the MRO of a particular class:
1. `__mro__` returns a list
2. `mro()`  returns a tuple

`For hierarchies Python resolves in a bottom to top manner C --> B --> A`

```python
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print(C.mro()) # Output: [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print(C.__mro__) # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

`When Inheriting from multiple classes Python resolves from left to right.`

```python
class A:
    pass

class B():
    pass

class C(A,B): # A comes before B
    pass



print(C.mro())      # Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.__mro__)    # Output: (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

```




<br>

[Back to Top](#python-inheritence)

___

<br>

# `Multiple Inheritence`
`Multiple inheritance` is a feature in object-oriented programming where a class can inherit attributes and methods from more than one parent class. 
1. Pay special attention to MRO when using multiple inheritence
1. Classes are inherited from left to right

`Attributes are inherited from the first class in the MRO (Method Resolution Order) that defines the attribute.`

```python
class Parent1:
    pass

class Parent2:
    pass
```
`Here Child will look to Parent1 first, then to Parent1`
```python
class Child(Parent1,Parent2):
    """Inherits from Parent1 First"""
    pass

print(Child.mro())  # Output: [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]    
```
`Here Child will look to Parent2 first, then to Parent1`
```python
class Child(Parent2,Parent1):
    """Inherits from Parent2 First"""
    pass

print(Child.mro()) # Output: [<class '__main__.Child'>, <class '__main__.Parent2'>, <class '__main__.Parent1'>, <class 'object'>]   
```

<br>

## `Common Problems with Multiple Inheritence`

### `The Diamond Problem`
```
     Top
    /   \
 Middle  Middle
    \   /
    Bottom
```
The `diamond problem` occurs in multiple inheritance when a class inherits from two classes that share a common parent, creating ambiguity in the attribute resolution order.

Consider the classes below:
```python
class Top:
    pass

class Middle(Top):
    pass

class Bottom(Top, Middle):
    pass

# Traceback (most recent call last):
#   File "/path/to/file.py", line 60, in <module>
#     class Bottom(Top, Middle):
#         pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases Top, Middle
```
This occurs because both Bottom, and Middle inherit from Top.

*`The MRO would look like this Bottom --> Top --> Middle --> Top. This order is an issue for resolving attributes.`*

<br>

Now consider these classes:
```python
class Top:
    pass

class Middle(Top):
    pass

class Bottom(Middle, Top):
    pass

print(Bottom.mro())  # Output: [<class '__main__.Bottom'>, <class '__main__.Middle'>, <class '__main__.Top'>, <class 'object'>]   
```

<br>

[Back to Top](#python-inheritence)

___

<br>

# `Composition`
`Composition` is a design principle where a class is built using instances of other classes as components.
1. This is different than inheritence
1. Establishes a "has-a" relationship (Class has a Component)

Example: A Computer is made of components: CPU, Memory, Storage, Motherboard, PowerSupply.
```python
class CPU:
    def process(self, process):
        print(f"CPU PROCESS: {process}")

    def execute_bootloader(self,storage, memory):
        self.process("executing bootloader...")
        storage.load(f"operating system kernal")
        self.initialize(storage)

    def initialize(self,storage=None):
        if storage:
            self.process(f"Kernel initializing hardware...")
            self.process(f"Kernel mounting the root filesystem from {storage.name}...")
            self.process(f"Kernal starting background processes and services...")
            self.process(f"Loading Command Line/Graphical User Interface...")
            
class Memory:
    def load(self, data):
        print(f"MEMORY LOADING: {data}...")
        return True

class Storage:
    def __init__(self, name=None):
        self.name = name

    def store(self,data):
        print(f"Storage saving {data}")

    def load(self, data):
        print(f"STORAGE LOADING:  {data}")
        return data



class Motherboard:
    def activate_uefi(self):
        print("Motherboard activating UEFI/BIOS...")

    def post(self):
        print("UEFI/BIOS performing Power on Self Test...")
        self.activate_uefi()

    def check_bootable_storage(self, storage_devices=None, memory=None, cpu=None):
        if storage_devices and memory and cpu:
            self.post()
            self.load(storage_devices[0],memory, cpu)
        elif not storage:
            print("No bootable storage...")
        elif not memory:
            print("No useable memory...")
        elif not cpu:
            print("No CPU...")
        else:
            print("An Error Occurred...")

    def load(self, storage=None, memory=None, cpu=None):
        failed = True
        if storage and memory:
            loaded_bootloader = memory.load(storage.load(f"bootloader of MBR/GPT from {storage.name}"))

            if loaded_bootloader: 
                cpu.execute_bootloader(storage, memory)

                failed = False

       
        if failed:
            print("Failed to boot..")


class PowerSupply:
    def __init__(self):
        self.switch = False

    def power(self,motherboard, storage_devices, memory, cpu):
        if self.switch:
            self.switch = False
        else:
            self.switch = True
            self.post(motherboard,storage_devices, memory, cpu)

    def post(self, motherboard, storage_devices, memory, cpu):
        print("PSU Performing Power On Self Test...")
        motherboard.check_bootable_storage(storage_devices, memory, cpu)
        


class Computer:
    def __init__(self, cpu, memory, storage, motherboard, power_supply):
        self.cpu = cpu                      # Computer has-a CPU component
        self.memory = memory                # Computer has-a Memory component
        self.storage = storage              # Computer has-a Storage component
        self.motherboard = motherboard      # Computer has-a Motherboard component
        self.power_supply = power_supply    # Computer has-a PowerSupply component

        self.storage_devices = []
        self.storage_devices.append(self.storage)

    def power_on(self):
        self.power_supply.power(self.motherboard,self.storage_devices, self.memory, self.cpu)
```
```python
# Instantiating a Computer with Components
computer = Computer(CPU(), Memory(), Storage("NVME_SSD1"), Motherboard(), PowerSupply())

computer.power_on()
# Output:
# PSU Performing Power On Self Test...
# UEFI/BIOS performing Power on Self Test...
# Motherboard activating UEFI/BIOS...
# STORAGE LOADING:  bootloader of MBR/GPT from NVME_SSD1
# MEMORY LOADING: bootloader of MBR/GPT from NVME_SSD1...
# CPU PROCESS: executing bootloader...
# STORAGE LOADING:  operating system kernal
# CPU PROCESS: Kernel initializing hardware...
# CPU PROCESS: Kernel mounting the root filesystem from NVME_SSD1...
# CPU PROCESS: Kernal starting background processes and services...
# CPU PROCESS: Loading Command Line/Graphical User Interface...
```

*Each Computer object is made up of component objects from other classes: CPU, Memory, Storage, and PowerSupply*


<br>

[Back to Top](#python-inheritence)

___

<br>

# `Abstract Classes and Methods`
An `abstract class` is a class that serves as a blueprint for other classes.
1. can include abstract methods
1. can include concrete methods
1. inherits from the ABC class in the abc (Abstract Base Class) module

<br>

An `abstract method` is a method declared in an abstract class without an implementation.
1. declared with the @abstractmethod decorator from the abc module.
1. must be implemented by the non-abstract subclass

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    '''Abstract Shape Class'''

    @abstractmethod 
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    '''Inherits from Shape and implements area, perimeter'''
    def __init__(self, width, height):
        self.name = "Rectangle"
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    '''Inherits from Shape and implements area, perimeter'''
    def __init__(self, radius):
        self.name = "Circle"
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius



shapes = [Rectangle(3, 4), Circle(5)]

for shape in shapes:
    print(f"{shape.name} --> Area: {shape.area()}, Perimeter: {shape.perimeter()}")

#Output:
# Rectangle --> Area: 12, Perimeter: 14
# Circle --> Area: 78.53975, Perimeter: 31.4159
```

<br>

[Back to Top](#python-inheritence)

___

<br>

*Created and maintained by Mr. Merritt*













