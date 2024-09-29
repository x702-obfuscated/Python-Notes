
***SPECIAL NOTE: The best way to understand classes is to start trying to write a class. Try writing a Player class like we do here to get stared.***

# `Python Classes`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*



Covered in this file:
1. Classes and Objects Defined 
1. Constructors: __init__(self) 
1. Instance Variables   
1. Instance Methods
1. Class Variables
1. Access Modifiers
1. Concrete Examples of Simple Classes


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

# `A Zero Programming Definition of Classes and Objects`

# `Classes Defined`

Basically: A `Class` is a blueprint for creating objects that defines what an object is (`data`) and what an object does (`methods`). 

Specifically: A `Class` is a blueprint for an object that encapsulates the `data` and `methods` that operate on that `data`.  



* Classes can also be thought of as custom data types
* Classes use `UpperCamelCase` for class names.
* Many `objects` can be created from the same class.

<br>

syntax for defining a class:
```
class ClassName():
    <Class Body>
    ...
```

<br>

[Back to Top](#python-classes)

___

<br>

# `Instances of a Class (Objects) Defined`
Basically: `Objects` are an `instances of a class` that contain `data` and `methods` (functions) that operate on that data. 


Specifically: `Objects` are an `instances of a class` that encapsulate `data` and `methods` (functions) that operate on that data. `Objects` are created by using the class `constructor`, which uses the class 'blueprint' to build the `object`.  

* Objects follow variable naming conventions (`lower_snake_case`)  
* Constructing an object is called `Instantiation` 
* Every instance of a class has the same attributes, but the values for those attributes may be different.  

<br>

### *`'Instance of a class' and  'object' mean the same thing.`*

<br>

[Back to Top](#python-classes)

___

### *To illustrate the concepts of creating class a concrete real example is often more helpful than abstractions. In this file we will use a Player class that defines a Player of an role playing video game to provide a concrete example.* 

*Additional examples can be found at the end of this file.*

___

<br>




# `Class Definition`

Classes are defined using the `class` keyword.

Parts of a class definition:
1. Class Header
1. Class Constructor
1. Attributes
    1. Data --> *What an object is*
    1. Methods --> *What an object does*

syntax:
```
class ClassName():

    def __init__(self):
        self.attribute = <value>

    def method(self):
        <method body>
        ...

    ...
```
example:
```python
class Player():

    def __init__(self):
        self.name = "Hero"
```

```python
class Player():                                 # Class Header
    '''Defines a Player for a video game.'''    # docstring
    
    def __init__(self):                         # Constructor Header
        '''Class Constructor'''                 # docstring
        self.name = "Hero"                      # Attribute
```




<br>

[Back to Top](#python-classes)

___

<br>

# `Class Constructors: __init__(self)`
Basically: A `Constructor` is a special `method` used to build instances of the class (`objects`)  

Specifically: A `Constructor` is a special `method` used to initialize the state of an `object` by assigning values to its `fields` (data).

<br>

* Constructors are defined using the dunder keyword `__init__` keyword.
* Constructors are called using the name of the class. 

### *`The function of a constructor is to initialize instance variables and call any default methods.`* 

*See >>> [`Constructors Initialize Instance Variables`]()*

<br>

definition syntax:
```
def __init__(self):
    <constructor body>
    ...
```

calling syntax:
```
ClassName()
```

<br>

example:
```python
class Player():

    def __init__(self):                 # Defining the Player constructor
        self.name = "Hero"              # Instance Variable

#<-- End of class definition

Player()                                # Calling the Player constructor
```

<br>

*Constructing an object in Python involves calling a constructor `__init__` method, which initializes the object's instance variables. When an object is created, a pointer to a memory location is allocated, and the attributes of the object are stored at that location. To access these attributes, first reference the object and then use dot syntax to access the data it stores. While each object has its own unique set of attributes stored separately in memory, the methods of the class are stored once in the class itself and shared among all instances, accessed through the object's reference to its class.*

<br>

[Back to Top](#python-classes)

___

<br>


# `Instantiation`

`Instantiation` is the process of creating an instance of a class (object) by calling the class constructor.

syntax:
```
ClassName(arguments, ...)
```

<br>

syntax for instantiation and assignment:
```
object_name = ClassName(arguments, ...)
```

<br>

example:
```python
class Player():                     

    def __init__(self):             
        self.name = "Hero"    

Player()                                    

player1 = Player()      
```
```python
class Player():
    '''Defines a Player for a video game.'''                     

    def __init__(self):             
        '''Class Constructor'''
        self.name = "Hero"    

# <-- End Class Definition

# Constructing a Player instance
Player()                            # Object Instantiation            

# Constructing and assigning a Player instance
player1 = Player()                  # Object Instantiation and Assignment
```

<br>

The constructor `Player()` builds the class instance (`object`) in memory and creates a reference to the instance. A variable, `player1`, can then be used to reference the object and access attributes and methods. 
```python  
Player()    
# This builds the object in memory and creates a reference        
```
```python
player1 = Player() 
# This builds the object, creates a reference, 
# and stores that reference in a variable for later access 
```


<br>

[Back to Top](#python-classes)

___

<br>

# `Dot Syntax`
`Dot syntax` is used to access the `attributes` and `methods` of `modules`,`classes`, and `objects`.  

<br>

### `Module`: a python source file
```
module_name.attribute_name
module_name.function_name()

module_name.ClassName.attribute_name
module_name.ClassName.method_name()
```
example:
```python
main.num
main.add()
```

<br>

### `Class`: a blueprint for objects
```
ClassName.attribute_name
ClassName.method_name()
```
example:
```python
Player.num_of_players
Player.display_players()
```

<br>

### `Object`: an instance of a class
```
object_name.attribute_name
object_name.method_name()
```
example:
```python
player1.hp
player1.attack()
```
<br>

[Back to Top](#python-classes)

___

<br>

# `self`
Basically: `self` is a placeholder variable that represents any instance of the class.

Specifically: `self` is the name given, by convention, to a variable that is a reference to any instance of the class (object). This variable allows access to the attributes of an object while within the class definition. 

<br>


* `self` is always the first parameter in the Constructor, and Methods.  
* `self` is required when attempting to access instance variables, or methods within the class definition.

<br>

*Naming this variable `self` is a convention in Python, not actually a requirement. `self` could be replaced with any other name. Despite this it is best to follow the convention when writing Python code.*


example:
```python
class Player():
    '''Defines a Player for a class rpg video game'''

    def __init__(self):
        '''Constructor'''
        self.name = "Hero"
        self.hp = 100
        self.mp = 50
        self.stamina = 75

    
    def display_data(self):
        '''Displays each field and its value for a given object'''
        for key, value in vars(self).items():
            print(f"{key} = {value}")
```

<br>

[Back to Top](#python-classes)

___

<br>


# `Attributes`

Basically: `Attributes` are the data and methods associated with an object that can be accessed with dot `.` syntax. 

Specifically: `Attributes` are values associated with an object that define the characteristics(data) and behaviours (methods) of that object. `Attributes` are accessed using dot `.` syntax.


Types of Attributes:
|Attribute|Explanation|
|:-:|:-|
| `Instance Variables` | Variables that are specific to an instance of a class. They are defined within methods, typically `__init__`, and their values vary between instances. |
| `Instance Methods`   | Methods that operate on an instance of the class. They are defined with a `self` parameter, which refers to the instance on which the method is called. |
| `Class Variables`    | Variables that are shared across all instances of the class. They are defined directly in the class body and have the same value for all instances, unless explicitly overridden. |
| `Class Methods`      | Methods that are bound to the class and not the instance. They are defined using the `@classmethod` decorator and take `cls` as their first parameter, referring to the class itself rather than an instance. |

<br>

[Back to Top](#python-classes)

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

[Back to Top](#python-classes)

___

<br>

## `Defining Instance Variables`
Instance variables are defined in the class definition typically within the `__init__` constructor method.

*In class definitions, instance variables are always attached to `self`*

<br>

instance variable assignment syntax:
```
self.variable_name = <value>
```

<br>

Here we will define 4 instance variables:  
* `self.name`
* `self.hp`
* `self.mp`
* `self.stamina`

Defining with literals:
```python
class Player()

    def __init__(self):
        '''Player Constructor'''
        self.name = "Hero"              # Instance Variable
        self.hp = 100                   # Instance Variable         
        self.mp = 50                    # Instance Variable
        self.stamina = 75               # Instance Variable
```
Defining with parameters:
```python
class Player(): 
    
    def __init__(self, name, hp, mp, stamina):  
        '''Player Constructor with parameters'''
        self.name = name                        # Instance Variable
        self.hp = hp                            # Instance Variable
        self.mp = mp                            # Instance Variable
        self.stamina = stamina                  # Instance Variable
```


example:
```python
class Player():                               

    def __init__(self, name, hp, mp, stamina):  
        '''Player Constructor with paramters'''
        self.name = name                        # Instance Variable
        self.hp = hp                            # Instance Variable
        self.mp = mp                            # Instance Variable
        self.stamina = stamina                  # Instance Variable

    def display_data(self):
        '''Displays each field and its value for a given object'''
        for key, value in vars(self).items():
            print(f"{key} : {value}", end = " | ")
        print()

#<-- End of class definition

# Constructing 4 Player instances
player1 = Player("Eldrin the Brave", 150, 70, 85)
player2 = Player("Morgana the Sorceress", 90, 120, 60)
player3 = Player("Thorne the Warrior", 180, 40, 95)
player4 = Player("Lyra the Enchantress", 110, 150, 55)


# Printing each players instance variables
player1.display_data() 
# Output: name: Eldrin the Brave | hp: 150 | mp: 70 | stamina: 85 | 

player2.display_data() 
# Output: name: Morgana the Sorceress | hp: 90 | mp: 120 | stamina: 60 |

player3.display_data() 
# Output: name: Thorne the Warrior | hp: 180 | mp: 40 | stamina: 95 |

player4.display_data() 
# Output: name: Lyra the Enchantress | hp: 110 | mp: 150 | stamina: 55 |
```

<br>

[Back to Top](#python-classes)

___

<br>

## `Accessing Instance Variables`
Instance variables are accessed using dot syntax.  

<br>

Inside the class definition, use:
```
self.variable_name
```

Outside the class definition, use:
```
object_name.variable_name
```

example:
```python
player1.name
player1.hp
player1.mp
player1.stamina
```

real example:
```python
class Player():                                 

    def __init__(self, name, hp, mp, stamina):
        '''Player Constructor with parameters'''  
        self.name = name                        # Instance Variable
        self.hp = hp                            # Instance Variable
        self.mp = mp                            # Instance Variable
        self.stamina = stamina                  # Instance Variable

#<-- End of class definition


# Constructing a Player instance
player1 = Player("Eldrin the Brave", 150, 70, 85)

# Accessing each instance variable
#      object.variable
print(player1.name)         # Output: Eldrin the Brave
print(player1.hp)           # Output: 150
print(player1.mp)           # Output: 70
print(player1.stamina)      # Output: 85
```

<br>

[Back to Top](#python-classes)

___

<br>

## `Constructors Initialize Instance Variables`
The function of a constructor is to initialize instance variables and call any default methods.


Initializing instance variables involves defining and assigning values to variables that are associated with a specific instance of a class (object).  

real example:
```python
class Player():                         # Class Header

    def __init__(self):                 # Defining Player constructor

        self.name = "default_player"    # instance variable
        self.hp = 100                   # instance variable
        self.mp = 50                    # instance variable
        self.stamina = 75               # instance variable


    # Method for displaying the variables in a Player object
    def display_attributes(self):
        attributes = vars(self)
        for var in attributes:
            print(f"{var}: {attributes[var]}")

# end of class definition

# Constructing a Player instance with the name player1
player1 = Player()                      

# Displaying instance variables and thier values
player1.display_attributes()          
# Output:
# name: default_player
# hp: 100
# mp: 50
# stamina: 75
```

Constructors can also accept parameters other than ***self***
* There is a difference between self.name and name, etc.  
> * self.name is a reference to the instance variable  
> * name is a reference to the parameter  
> * this is one reason that ***self*** is necessary when writing classes

real example:
```python
class Player():                                 # Class Header

    # Defining Player constructor with parameters
    def __init__(self, name, hp, mp, stamina):  
        self.name = name                        # instance variable
        self.hp = hp                            # instance variable
        self.mp = mp                            # instance variable
        self.stamina = stamina                  # instance variable

    # Method for displaying the variables in a Player object
    def display_attributes(self):
        attributes = vars(self)
        for var in attributes:
            print(f"{var}: {attributes[var]}")
# end of class definition           

# Constructing a Player instance with the name player1 and passing arguments 
player1 = Player("Hero", 1000, 500, 750)

# Displaying instance variables and thier values
player1.display_attributes()
# Output:
# name: Hero
# hp: 1000
# mp: 500
# stamina: 750
```

<br>

Putting it all together
```python
class Player():                                 # Class Header

    # Defining Player constructor with parameters and defaults
    #   here the parameters are indented for readability
    def __init__(
            self, 
            name = "default_name",
            hp = 100,
            mp = 50, 
            stamina = 75
        ):  
        self.name = name                        # instance variable
        self.hp = hp                            # instance variable
        self.mp = mp                            # instance variable
        self.stamina = stamina                  # instance variable

    # Method for displaying the variables in a Player object
    def display_attributes(self):
        attributes = vars(self)
        for var in attributes:
            print(f"{var}: {attributes[var]}", end = " | ")
        print()
# end of class definition  

# Constructing a Player instance with the name player1 using default constructor 
player1 = Player()

# Displaying instance variables and thier values
player1.display_attributes()
# Output: name: default_name | hp: 100 | mp: 50 | stamina: 75 | 

        
# Constructing a Player instance with the name player2 and arguments
player2 = Player("Hero", 1000, 500, 750)


# Displaying instance variables and thier values
player2.display_attributes()
# Output: name: Hero | hp: 1000 | mp: 500 | stamina: 750 | 
```


<br>

[Back to Top](#python-classes)

___

<br>

# `Class Variables`
syntax for assigning variables associated with a class:

    variable_name = ...

syntax for accessing variables associated with the class:

    ClassName.variable_name

> * basically: variables shared among all instances of a class.  
> * specifically: variables that are associated with a class and shared among all instances of a class. They have the same value for all instances of that class.   

<br> 

## Class Variable Creation
> * class variables are created by defining a variable inside of the class definition, and outside of any class methods

abstract example:
```
class ClassName():

    class_variable = ...
```

real example:
```python
class Player():             # Class Definition Header

    number_of_players = 0  # <-- CLASS VARIABLE
```

<br>

## Class Variable Access
> * class variables can be accessed using dot syntax in two ways

syntax
```
ClassName.class_variable
```
```
object_name.class_variable
```

real example:
```python
class Player():                 # Class Definition Header

    number_of_players = 0       # <-- CLASS VARIABLE

    def __init__(self):         # Class Constructor
        Player.number_of_players += 1

# End of Class Definition    


player1 = Player()              # Object Instantiation and Assignment

# Accessing 'number_of_players'
Player.number_of_players        # Returns: 1
#         OR
player1.number_of_players       # Returns: 1
```

<br>

## Putting it all together: Creation and Access
real example: 
```python
class Player():                 # Class Definition Header

    number_of_players = 0       # <-- CLASS VARIABLE

    def __init__(self):         # Class Constructor
        Player.number_of_players += 1

# end of class definition

player1 = Player()              # Object Instantiation
player2 = Player()              # Object Instantiation
player3 = Player()              # Object Instantiation

# Access with Class_Name
#      Class.variable
print(Player.number_of_players) # printing the value of number_of_players
# Output: 3


# Access with Object_Name
#      object.variable
print(player1.number_of_players)   # Output: 3
print(player2.number_of_players)   # Output: 3
print(player3.number_of_players)   # Output: 3
# The same value appears regardless of the object

```

<br>

[Back to Top](#python-classes)

___

<br>

# `Methods`
> * are functions defined by a class
> * are typically called using an object or class and dot ( . ) syntax

### Defining a Method
> to define a method, define a function inside of the class definition

syntax:
```
class ClassName():

    def method_name():
        ...
```

<br>

[Back to Top](#python-classes)

___

<br>

### Calling a Method
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

<br>

[Back to Top](#python-classes)

___

<br>

# `Access Modifiers`
> Access modifiers in Python determine the accessibility and visibility of class attributes and methods from outside the class, using naming conventions (e.g., public, protected, private) instead of explicit keywords like in other languages.

Access Modifier Conventions:  

## Public
> * Accessible from anywhere. No prefixing.     

syntax : 
```
variable_name = ...
```
real example:
```python
class Player:
    def __init__(self, name, hp, mp, stamina):
        self.name = name                           # Public attribute
        self.hp = hp                               # Public attribute
        self.mp = mp                               # Public attribute
        self.stamina = stamina                     # Public attribute
```

<br>

## Protected
> * Indicated by a single underscore (_) prefix, suggesting that it should not be accessed directly outside of the class and its subclasses.

syntax:
```
_variable_name = ...
```
real example:
```python
class Player:
    def __init__(self, name, hp, mp, stamina):
        self._name = name                           # Protected attribute
        self._hp = hp                               # Protected attribute
        self._mp = mp                               # Protected attribute
        self._stamina = stamina                     # Protected attribute
```

<br>

## Private
> * Indicated by a double underscore (__) prefix, suggesting that it should not be accessed from outside of the class.  
> * Trying to access the private method or attribute directly will result in an AttributeError 

Name Mangling
> * When you define a method or attribute with a name that starts with double underscores, Python internally changes the name by prefixing it with _ClassName

syntax:
```
__variable_name = ...
```
real example:
```python
class Player:
    def __init__(self, name, hp, mp, stamina):
        self.__name = name                           # Private attribute
        self.__hp = hp                               # Private attribute
        self.__mp = mp                               # Private attribute
        self.__stamina = stamina                     # Private attribute


player1 = Player("Eldrin the Brave", 50, 70, 85)


#Access by prefixing with _ClassName, this is not recommended
print(player1._Player__name)        # Output: Eldrin the Brave
```

<br>


# `Concrete Examples with Simple Classes`

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def description(self):
        return f"{self.year} {self.make} {self.model}"
    
    def start(self):
        return f"{self.make} {self.model} is starting."

# Creating objects
car1 = Car("Toyota", "Camry", 2021)
car2 = Car("Honda", "Civic", 2022)

print(car1.description())  # Output: 2021 Toyota Camry
print(car2.description())  # Output: 2022 Honda Civic
```
```python
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
    
    def introduce(self):
        return f"My name is {self.name}, my student ID is {self.student_id}, and I major in {self.major}."

# Creating objects
student1 = Student("Alice", "S12345", "Computer Science")
student2 = Student("Bob", "S67890", "Mathematics")

print(student1.introduce())  # Output: My name is Alice, my student ID is S12345, and I major in Computer Science.
print(student2.introduce())  # Output: My name is Bob, my student ID is S67890, and I major in Mathematics.
```
```python
class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def info(self):
        return f"'{self.title}' by {self.author}, published in {self.year_published}"

# Creating objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("1984", "George Orwell", 1949)

print(book1.info())  # Output: 'To Kill a Mockingbird' by Harper Lee, published in 1960
print(book2.info())  # Output: '1984' by George Orwell, published in 1949
```
```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        return f"{self.name} says woof!"

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Luna", "Labrador", 2)

print(dog1.bark())  # Output: Buddy says woof!
print(dog2.bark())  # Output: Luna says woof!
```