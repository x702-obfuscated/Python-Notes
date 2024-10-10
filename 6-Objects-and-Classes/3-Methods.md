# `Python Methods`

*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

<br>

___

<br>

Covered in this file:
1. [`Methods Defined`](#methods-defined)
1. [`Instance Methods`](#instance-methods)
    1. [`Defining Instance Methods`](#defining-instance-methods)
    1. [`Calling Instance Methods`](#calling-instance-methods)
1. [`Class Methods`](#class-methods)
    1. [`Defining Class Methods`](#defining-class-methods)
    1. [`Calling Class Methods`](#calling-class-methods)
1. [`Static Methods`](#static-methods)
    1. [`Defining Static Methods`](#defining-static-methods)
    1. [`Calling Statice Methods`](#calling-static-methods)
1. [`Access Modifiers`](#access-modifiers)
    1. [`Public`](#public)
    1. [`Protected`](#protected)
    1. [`Private`](#private)
1. [`Getters`](#getters)
1. [`Setters`](#setters)
1. [`Deleters`](#deleters)
1. [`property()`](#property)
1. [`Using the @property decorator`](#using-the-property-decorator)
1. [`Special Methods to Define`](#special-methods-to-define)

[`__init__`](#__init__) [`__str__`](#__str__) [`__repr__`](#__repr__) [`__len__`](#__len__) [`__getitem__`](#__getitem__) [`__setitem__`](#__setattr__) [`__delitem__`](#__delitem__) [`__iter__`](#__iter__) [`__next__`](#__next__) [`__contains__`](#__contains__) [`__eq__`](__eq__) [`__lt__`](__lt__) [`__le__`](#__le__) [`__gt__`](#__gt__) [`__ge__`](#__ge__) [`__add__`](#__add__) [`__sub__`](#__sub__) [`__mul__`](#__mul__) [`__truediv__`](#__truediv__) [`__call__`](#__call__) [`__getattr__`](#__getattr__) [`__setattr__`](#__setattr__) [`__delattr__`](#__delattr__) [`__hash__`](#__hash__) [`__enter__`](#__enter__) [`__exit__`](#__exit__)

<br>

___

<br>

# `Methods Defined`
Basically: `Methods` are functions defined by a class.

Specifically: `Methods` are functions that are associated with an object or class. They define behaviors or actions that an object can perform and usually operate on the data contained within that object. Methods are often used to encapsulate functionality and data within an object-oriented programming (OOP) paradigm. 

<br>

### *`Methods use the same syntax as functions.`*

<br>

There are three types of methods defined by a class: 
|`instance methods`|`class methods`|`static methods`|
|:-:|:-:|:-:|

<br>

___

<br>

# `Instance Methods`

`What an object does (its behaviour)`

Basically: An `Instance Method` is a function defined in a class that operates on an instance of a class(object) 

Specifically: `Instance Methods` are functions defined within a class that operate on a specific instance, taking self as their first parameter to access and modify the instance's attributes and define behaviors unique to that object.

<br>

## `Defining Instance Methods`

`Instance Methods` are defined within the class and require `self` as the first parameter.

syntax:
```
class ClassName():

    def instance_method(self, parameters, ...):
        ...
```

real example:
```python
class Player():                                 # Class Header
    '''
    Player class that defines what a Player is (data), 
    and what a player does (methods)
    '''

    def __init__(self, name, hp, mp, stamina):  # Constructor Header
        '''Player constructor with parameters''' 
        self.name = name                        # instance variable
        self.hp = hp                            # instance variable
        self.mp = mp                            # instance variable
        self.stamina = stamina                  # instance variable

 
    def take_damage(self, amount):              # Method Header
        '''Instance method to reduce HP by a specified amount.'''
        self.hp -= amount
        if(self.hp < 0):
            self.hp = 0
        
  
    def display_attributes(self):               # Method Header
        '''Instance Method for displaying the attributes of a Player object'''
        attributes = vars(self)
        for var in attributes:
            print(f"{var}: {attributes[var]}", end = " | ")
        print()

#end of class definition
```

<br>


## `Calling Instance Methods`
`Instance Methods` require an object in order to be called.

Instance Methods are called using an instance of a class, dot syntax, and the method name. 

syntax:  
```
object.method(arguments, ...)
```

real example:
```python
class Player():                                 # Class Header
    '''
    Player Class that defines what a Player is (data), 
    and what a player does (methods)
    '''

    def __init__(self, name, hp, mp, stamina): 
        '''Player constructor with parameters''' 
        self.name = name                        # instance variable
        self.hp = hp                            # instance variable
        self.mp = mp                            # instance variable
        self.stamina = stamina                  # instance variable

    
    def take_damage(self, amount):
        '''Instance method to reduce HP by a specified amount.'''
        self.hp -= amount
        if(self.hp < 0):
            self.hp = 0
        

    def display_attributes(self):
        '''Instance Method for displaying the attributes of a Player object'''
        attributes = vars(self)
        for var in attributes:
            print(f"{var}: {attributes[var]}", end = " | ")
        print()

#<-- end of class definition

# Construct a Player instance with the name player1 and arguments
player1 = Player("Eldrin the Brave", 150, 70, 85)

#Calling an instance Method
player1.display_attributes()      
# Output: name: Eldrin the Brave | hp: 150 | mp: 70 | stamina: 85 |
#                                  ^^^^^^^

# Calling an Instance Method
player1.take_damage(15)            # Returns : None; This just modifies hp

# Calling an Instance Method 
player1.display_attributes()
# Output: name: Eldrin the Brave | hp: 135 | mp: 70 | stamina: 85 |
#                                  ^^^^^^^
```

<br>

[Back to Top](#python-methods)

___

<br>

# `Class Methods`

Basically: A `class method` is defined by a class and associated with the class, not an instance of the class. 

Specifically: A `class method` in Python is a method that is bound to the class and not the instance of the class. This means that it can modify class state that applies across all instances of the class. 

<br>

* `Class Methods` can access class variables, but not instance variables
* `Class Methods` use the `@classmethod` decorator

* `cls` is always the first parameter in Class methods. This parameter represents the Class, and is automatically passed when using dot syntax.    

<br>

## `Defining Class Methods`

To define a class method, you use the `@classmethod decorator`, and the first argument of the method must be `cls` (which refers to the class itself).



syntax:
```
class Class_Name():

    @classmethod
    def class_method(cls, parameters,  ... ):
        ...
```

real example:
```python
class Player():                         # Class Header
    
    @classmethod                        # Decorator
    def from_dict(cls, player_data):    # Class Method Definition
        """Class method to create a Player instance from a dictionary."""
        name = player_data.get("name", "Unknown")
        score = player_data.get("score", 0)
        return cls(name, score)

    # Class Constructor
    def __init__(self, name, score = 0): 
        self.name = name
        self.score = score

    # Instance Method
    def display(self):
        print(f"Player: {self.name}, Score: {self.score}")

#<-- end of class definition

```

<br>


## `Calling Class Methods`

Class methods can be called in two ways.
1. Using the ClassName, dot syntax, and the method name
1. Using the object_name, dot syntax, and the method name


`The class is passed as an argument by default. `
<br>
 
syntax:
```
ClassName.class_method(cls, arguments, ... )
```
```
object_name.class_method(cls, arguments, ... )
```

real example:
```python
class Player():                         # Class Header
    
    @classmethod                        # Decorator
    def from_dict(cls, player_data):    # Class Method Definition
        """Class method to create a Player instance from a dictionary."""
        name = player_data.get("name", "Unknown")
        score = player_data.get("score", 0)
        return cls(name, score)

    # Class Constructor
    def __init__(self, name, score = 0): 
        self.name = name
        self.score = score

    # Instance Method
    def display(self):
        print(f"Player: {self.name}, Score: {self.score}")

#<-- end of class definition


data = {"name":"Vector","score": 75}

#          Class.class_method()
player1 = Player.from_dict(data)        # Returns a Player object

player1.display()
# Output: Player: Vector, Score: 75



info = {"name":"Stewart","score": 50}

#          object.class_method()          Player is passed to cls
player2 = player1.from_dict(info)       # Returns a Player object

player2.display()
# Output: Player: Stewart, Score: 50
```

<br>

[Back to Top](#python-methods)

___

<br>

# `Static Methods`

Basically: A `static method` is defined by a class but is not associated with either the class or an instance of the class.

Specifically: A `static method` is a method that belongs to a class but does not require access to the class or its instances. It behaves like a regular function that resides in the class’s namespace. It cannot modify class state or instance state and is mainly used when functionality is logically related to the class but doesn't need access to class or instance data. You define a static method using the `@staticmethod` decorator.

<br>

* `Static Methods` logically belong to the class but do not require access to the class or its instances

* `Static Methods` are typically utility functions

*NOTE: the `@staticmethod` decorator we use here is not required for static methods, but is a good practice for clarity, design, and readability.*

<br>

## `Defining Static Methods`
Define a static method using the `@staticmethod` decorator. 

syntax:
```
class ClassName():

    @staticmethod
    def method_name(parameters, ... ):
        ...
```
real example:
```python
class Player():                 # Class Definition Header

    # Static Method Definition
    @staticmethod               # Decorator
    def is_valid_score(score):  
        """Static method to check if the given score is valid."""
        return(isinstance(score, int) and score >= 0)

#<-- end class definition
```

<br>

## `Calling Static Methods`

Static methods can be called in two ways.
1. Using the ClassName, dot syntax, and the method name
1. Using the object_name, dot syntax, and the method name

*Note: Using an object to call a static method without the `@staticmethod` decorator will raise a syntax/compile time `TypeError`*


syntax:
```
ClassName.static_method(arguments, ... )
```
```
object_name.static_method(arguments, ... )
```

real example:
```python
class Player():                 # Class Definition Header

    # Static Method Definition
    @staticmethod               # Decorator
    def is_valid_score(score):  
        """Static method to check if the given score is valid."""
        return(isinstance(score, int) and score >= 0)

#<-- end class definition


player1 = Player()              # Object Instantiation

Player.is_valid_score(1)        # ClassName.static_method()
# Returns: True

player1.is_valid_score(1)       # object_name.static_method()
# Returns: True
```

<br>

Using an object to call a static method without the `@staticmethod` decorator will raise a syntax/compile time `TypeError`  

real example:
```python
class Player():                 # Class Definition Header

    # Static Method Definition
    #                           <-- NO DECORATOR
    def is_valid_score(score):  
        """Static method to check if the given score is valid."""
        return(isinstance(score, int) and score >= 0)

#<-- end class definition


player1 = Player()              # Object Instantiation

Player.is_valid_score(1)        # ClassName.static_method()
# Returns: True

player1.is_valid_score(1)       # object_name.static_method()
# Output:
# Traceback (most recent call last):
#   File "<filepath>", line 17, in <module>
#     player1.is_valid_score(1)       # object_name.static_method()
#     ^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: Player.is_valid_score() takes 1 positional argument but 2 were given
```

<br>

[Back to Top](#python-methods)

___

<br>

# `Access Modifiers`

`Access modifiers` in Python determine the accessibility and visibility of class attributes and methods from outside the class, using naming conventions (e.g., `public`, `protected`, `private`) instead of explicit keywords like in other languages.

<br>

## `Public`
Public variables and methods are accessible from anywhere. No prefixing.     

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

* Trying to access the private method or attribute directly will result in an `AttributeError` 

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

[Back to Top](#python-methods)

___

<br>

# `Getters`
`Getters` are methods used to control how data is retrieved  
* Getter are typically prefixed with "get"  
* Getters require a return value

<br>

syntax:
```
def get_variable():
    return ...
```
real example:
```python
class Player():                                 # Class Header

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina

    def get_name(self):
        '''self.name getter'''
        return self.name
```

<br>

[Back to Top](#python-methods)

___

<br>

## `Setters`
Setters are methods used to control how data is changed
* Setters are typically prefixed with "set"
* Setters typically have parameters and accept arguments.

syntax:
```
def set_variable():
    ...
```
real example:
```python
class Player():     # Class Header

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina


    def set_hp(self, value):
        '''self.hp setter'''
        if value < 0:
            raise ValueError("HP cannot be negative")
        self.hp = value
```

<br>

[Back to Top](#python-methods)

___

<br>

## `Deleters`
Deleters are methods used to control how data is deleted
* Deleters are typically prefixed with "del"

syntax:
``` 
def del_variable():
    ...
```
real example:
```python
class Player():       # Class Header

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina


    def del_hp(self):
        '''self.hp deleter'''
        raise AttributeError("Cannot delete 'hp' attribute")
```

<br>

[Back to Top](#python-methods)

___

<br>

## `property()`
`property()` is a function that maps getters, setters, and deleters to a variable, so that they are automatically called when the variable is accessed.

* It is considered best practice to use the `@property` decorator instead. Take a look at decorators to learn more.

* Private or Protected values must be used to prevent raising a `RecursionError: maximum recursion depth exceeded`

<br>

syntax:
```
property(fget = None, fset = None, fdel = None, doc = None)
```
real example:
```python
class Player():        # Class Header

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self._name = name
        self._hp = hp
        self._mp = mp
        self._stamina = stamina


    def get_mp(self):
        '''self.mp getter'''
        return self._mp

    def set_mp(self, value):
        '''self.mp setter'''
        if value < 0:
            raise ValueError("mp cannot be negative")
        self._mp = value

    def del_mp(self):
        '''self.mp deleter'''
        raise AttributeError("Cannot delete 'mp' attribute")
    
    # Mapping these functions to self.mp
    mp = property(get_mp, set_mp, del_mp, "Magic Points value for casting spells.")

#<-- end of class definition


# Constructing a Player instance
player1 = Player("Eldrin the Brave", 150, 70, 85)

print(player1.mp)              # Calls player1.get_mp()     
# Output: 70    

player1.mp = -1                # Calls player1.set_mp(-1)
# Raises: ValueError: mp cannot be negative

del player1.mp                 # Calls player1.del_mp()
# Raises: AttributeError: Cannot delete 'mp' attribute
```

<br>

## `Using the @property decorator`

syntax:
```
@property
def name(self):
    ...

@<property_name>.setter
def name(self, value):
    ...

@<property_name>.deleter
def name(self, value):
    ...
```
real example:
```python
class Player():    # Class Header

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self._name = name
        self._hp = hp
        self._mp = mp
        self._stamina = stamina

    @property                       # mp Getter
    def mp(self):
        '''self.mp getter'''
        return self._mp

    @mp.setter                      # mp Setter
    def mp(self, value):
        '''self.mp setter'''
        if value < 0:
            raise ValueError("mp cannot be negative")
        self._mp = value

    @mp.deleter                     # mp Deleter
    def mp(self):
        '''self.mp deleter'''
        raise AttributeError("Cannot delete 'mp' attribute")
    

#<-- end of class definition

# Constructing a Player instance
player1 = Player("Eldrin the Brave", 150, 70, 85)


print(player1.mp)              # Calls the getter     
# Output: 70    

player1.mp = -1                # Calls the setter
# Raises: ValueError: mp cannot be negative

del player1.mp                 # Calls the deleter
# Raises: AttributeError: Cannot delete 'mp' attribute
```

<br>

[Back to Top](#python-methods)

___

<br>

# `Special Methods to Define:`
There are several special `dunder` (double underscore `__`) methods that can be defined in a class and perform special functions when defined. 


special dunder methods:

`__init__`, `__str__`, `__repr__`, `__len__`, `__getitem__ `, `__setitem__`, `__delitem__`, `__iter__ `, `__next__`, `__contains__`, `__eq__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__call__`, `__getattr__`, `__setattr__`, `__delattr__`, `__hash__`, `__enter__`, `__exit__`

| Dunder Method| Purpose| Example|
|:-:|:-|:-|
| `__str__`| Defines the human-readable (informal) string representation of an object (used by `print()`). | `print(obj)` → `obj.__str__()` |
| `__repr__` | Defines the official (formal) string representation of an object (used by `repr()`, meant for developers). | `repr(obj)` → `obj.__repr__()` |
| `__len__`| Defines behavior for the `len()` function, returning the length of the object. | `len(obj)` → `obj.__len__()` |
| `__getitem__`| Enables indexing and key access for objects.| `obj[key]` → `obj.__getitem__(key)`|
| `__setitem__`| Defines behavior for assigning a value to a specific key or index. | `obj[key] = value` → `obj.__setitem__(key, value)` |
| `__delitem__`| Defines behavior for deleting a key or index from an object. | `del obj[key]` → `obj.__delitem__(key)`|
| `__iter__` | Defines behavior for making an object iterable (returns an iterator object). | `for item in obj:` → `obj.__iter__()` |
| `__next__` | Defines behavior for the next item in an iterator (used by `next()`).| `next(iterator)` → `iterator.__next__()` |
| `__contains__` | Defines behavior for membership testing (e.g., `in` operator). | `x in obj` → `obj.__contains__(x)` |
| `__eq__` | Defines behavior for equality comparison. | `obj1 == obj2` → `obj1.__eq__(obj2)` |
| `__lt__` | Defines behavior for less-than comparison.| `obj1 < obj2` → `obj1.__lt__(obj2)`|
| `__le__` | Defines behavior for less-than-or-equal comparison. | `obj1 <= obj2` → `obj1.__le__(obj2)` |
| `__gt__` | Defines behavior for greater-than comparison. | `obj1 > obj2` → `obj1.__gt__(obj2)`|
| `__ge__` | Defines behavior for greater-than-or-equal comparison.| `obj1 >= obj2` → `obj1.__ge__(obj2)` |
| `__add__`| Defines behavior for the addition operator. | `obj1 + obj2` → `obj1.__add__(obj2)` |
| `__sub__`| Defines behavior for the subtraction operator.| `obj1 - obj2` → `obj1.__sub__(obj2)` |
| `__mul__`| Defines behavior for the multiplication operator. | `obj1 * obj2` → `obj1.__mul__(obj2)` |
| `__truediv__`| Defines behavior for the true division operator.| `obj1 / obj2` → `obj1.__truediv__(obj2)` |
| `__call__` | Makes an object callable like a function. | `obj()` → `obj.__call__()` |
| `__getattr__`| Defines behavior for accessing an attribute that doesn't exist.| `obj.non_existent` → `obj.__getattr__('non_existent')` |
| `__setattr__`| Defines behavior for setting an attribute value.| `obj.attr = value` → `obj.__setattr__('attr', value)` |
| `__delattr__`| Defines behavior for deleting an attribute. | `del obj.attr` → `obj.__delattr__('attr')` |
| `__hash__` | Defines behavior for obtaining the hash value of an object. | `hash(obj)` → `obj.__hash__()` |
| `__enter__`| Defines behavior for entering a context (used with the `with` statement). | `with obj:` → `obj.__enter__()` |
| `__exit__` | Defines behavior for exiting a context (used with the `with` statement). | `with obj:` → `obj.__exit__()`|


<br>

[Back to Top](#python-methods)

___

<br>

## `__init__`
```
def __init__(self, parameters, ... ):
    '''
    Used by constructor call --> ClassName()
    Constructor for a class, initializes instance variables
    Returns an object reference
    '''
```
real example:
```python
class Player():
    def __init__(self):
        self.name = "default_name"
        self.hp = 100
        self.mp = 50
        self.stamina = 75
# end of class definition

player1 = Player()      # Calls the __init__ method
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__str__`
```
def __str__(self):
    '''
    Used by the str() function.
    Returns a human-readable string representation of the object.
    '''
```
real example:
```python
class Player():
    def __init__(self):
        self.name = "default_name"
        self.hp = 100
        self.mp = 50
        self.stamina = 75

    def __str__(self):
        return self.name
# end of class definition

player1 = Player()

str(player1)        # Returns: default_name
print(player1)      # Output: default_name      

```

<br>

[Back to Top](#python-methods)

___

<br>

## `__repr__`
```
def __repr__(self):
    '''
    Used by the repr() function.
    Returns a detailed string representation of the object for debugging.
    '''
```
*NOTE: the `!r` in a formatted string (using f-strings) is a conversion flag that specifies that the repr() function should be used to format the value.*

real example:
```python
class Player():
    def __init__(self, name, hp, mp, stamina):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina

    def __repr__(self):
        '''Returns a detailed string representation for debugging.'''
        return (
            f"Player(name={self.name!r}, hp={self.hp!r}, "
            f"mp={self.mp!r}, stamina={self.stamina!r})"
        )

# Creating an instance of Player
player1 = Player("Eldrin the Brave", 150, 70, 85)

# Using the __repr__ method
print(repr(player1))
# Output: Player(name='Eldrin the Brave', hp=150, mp=70, stamina=85)
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__len__`
```
def __len__(self):
    '''
    Used by the len() function.
    Defines how to return the number of items in the object.
    '''
```
real example:
```python
class Player():
    def __init__(self, name, hp, mp, stamina):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina

    def __len__(self):
        '''Returns the number of attributes in the Player object.'''
        return len(vars(self))  
# end of the class definition


# Creating an instance of Player
player1 = Player("Eldrin the Brave", 150, 70, 85)

# Calling the __len__ method
len(player1)  # Returns: 4
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__getitem__`
```
def __getitem__(self, key):
    '''
    Used by subscripting [] --> object[key]
    Defines how to return the item corresponding to 'key'.
    '''
```
real example:
```python
class Player:
    def __init__(self):
        self.bag = {
            'potion': "heals the user for 10pts", 
            'map': "used to find where you are going",
            'sword': "sharp and does 10pts of damage",
            'shield': "sturdy and increases defense by 20pts"
            }

    def __getitem__(self, key):
        '''Gets the item corresponding to 'key'.'''
        if key in self.bag:
            return self.bag[key]
        else:
            raise KeyError(f"Invalid key: {key}")


player1 = Player()

# Using subscripting [] calls the __getitem__ method
player1['potion']        # Returns: heals the user for 10pts
player1['map']           # Returns: used to find where you are going
player1['sword']         # Returns: sharp and does 10pts of damage
player1['shield']        # Returns: sturdy and increases defense by 20pts
player1['helmet']        # Raises: KeyError: 'Invalid key: helmet'
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__setitem__`
```
def __setitem__(self, key, value):
    '''
    Used by subsripting [] --> object[key] = value
    Defines how to set the item corresponding to 'key' to 'value'.
    '''
```
real example:
```python
class Player:
    def __init__(self):
        self.bag = {
            'potion': "heals the user for 10pts", 
            'map': "used to find where you are going",
            'sword': "sharp and does 10pts of damage",
            'shield': "sturdy and increases defense by 20pts"
            }

    def __getitem__(self, key):
        '''Gets the item corresponding to 'key'.'''
        if key in self.bag:
            return self.bag[key]
        else:
            raise KeyError(f"Invalid key: {key}")

    def __setitem__(self, key, value):
        '''Sets the item corresponding to 'key'.'''
        self.bag[key] = value



player1 = Player()

# Using subscripting [] calls the __getitem__ method
player1['helmet']        # Raises: KeyError: 'Invalid key: helmet'

#Using subscripting [] = calls the __setitem__method
player1['helmet'] = "protects one's head from unwanted boops"

player1['helmet']       # Returns: protects one's head from unwanted boops
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__delitem__`
```
def __delitem__(self, key):
    '''
    Used by subscripting [] --> del object[key]
    Defines how to delete the item corresponding to 'key'.
    '''
```
real example:
```python
class Player:
    def __init__(self):
        self.bag = {
            'potion': "heals the user for 10pts", 
            'map': "used to find where you are going",
            'sword': "sharp and does 10pts of damage",
            'shield': "sturdy and increases defense by 20pts"
            }

    def __getitem__(self, key):
        '''Gets the item corresponding to 'key'.'''
        if key in self.bag:
            return self.bag[key]
        else:
            raise KeyError(f"Invalid key: {key}")

    def __delitem__(self, key):
        '''Deletes the item corresponding to 'key'.'''
        if key in self.bag:
            del self.bag[key]
        else:
            raise KeyError(f"Invalid key: {key}")



player1 = Player()

# Using subscripting [] calls the __getitem__ method
player1['potion']        # Returns: heals the user for 10pts

#Using subscripting del [] = calls the __delitem__ method
del player1['potion'] 

player1['potion']        # Raises: KeyError: 'Invalid key: potion'
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__iter__`
```
def __iter__(self):
    '''
    Used by for-loops and comprehensions
    Defines how to return an iterator for the object.
    '''
```
real example:
```python
class Player:
    def __init__(self):
        self.bag = {
            'potion': "heals the user for 10pts", 
            'map': "used to find where you are going",
            'sword': "sharp and does 10pts of damage",
            'shield': "sturdy and increases defense by 20pts"
            }

    def __iter__(self):
        '''Returns an iterator over the values in the bag.'''
        return iter(self.bag.keys())
    
# end of class definition

# Constructs a Player object
player1 = Player()

# Using player1 as an iterable calls the __iter__ method
for item in player1:
    print(item)
# Output:
# potion
# map
# sword
# shield
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__next__`
```
def __next__(self):
    '''
    Used by the next() function.
    Defines how to return the next item from the iterator.
    '''
```
real example:
```python
class Player:
    def __init__(self):
        self.bag = {
            'potion': "heals the user for 10pts", 
            'map': "used to find where you are going",
            'sword': "sharp and does 10pts of damage",
            'shield': "sturdy and increases defense by 20pts"
            }

    def __iter__(self):
        '''Returns an iterator over the values in the bag.'''
        return iter(self.bag.keys())


    def __next__(self):
        '''Returns the next item from the iterator.'''
        try:
            key = next(iter(self))
            return self.bag[key]
        except StopIteration:
            raise StopIteration("No more items in the bag.")
    
# end of class definition

# Constructs a Player object
player1 = Player()

# Stores the iterable version of player1 in player_items
player_items = iter(player1)

# Using next() calls the __next__ method
print(next(player_items))           # Output: potion
print(next(player_items))           # Output: map
print(next(player_items))           # Output: sword
print(next(player_items))           # Output: shield
print(next(player_items))           # Raises: StopIteration
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__contains__`
```
def __contains__(self, item):
    '''
    Used by the 'in' operator
    Defines how to check if 'item' is in the object.
    '''
```
real example:
```python
class Player:
    def __init__(self):
        self.bag = {
            'potion': "heals the user for 10pts", 
            'map': "used to find where you are going",
            'sword': "sharp and does 10pts of damage",
            'shield': "sturdy and increases defense by 20pts"
            }

    def __contains__(self, key):
        '''Checks if the key is in the bag.'''
        return key in self.bag
    
# end of class definition

# Constructs a Player object
player1 = Player()

# Using the 'in' operator calls the __contains__ method
print("potion" in player1)      # Output: True

print("boots" in player1)       # Output: False
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__eq__`
```
def __eq__(self, other):
    '''
    Used by the '==' operator.
    Defines how to check if the object is equal to 'other'.
    '''
```

<br> 

## `__lt__`
```
def __lt__(self, other):
    '''
    Used by the '<' operator.
    Defines how to check if the object is less than 'other'.
    '''
```
<br> 

## `__le__`
```
def __le__(self, other):
    '''
    Used by the '<=' operator.
    Defines how to check if the object is less than or equal to 'other'.
    '''   
```

<br> 

## `__gt__`
```
def __gt__(self, other):
    '''
    Used by the '>' operator.
    Defines how to check if the object is greater than 'other'.
    '''
```

<br> 

## `__ge__`
```
def __ge__(self, other):
    '''
    Used by the '>=' operator.
    Defines how to check if the object is greater than or equal to 'other'.
    '''
```
real example:
```python
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    

    def __eq__(self, other):
        '''Checks if two Player objects have the same name.'''
        if isinstance(other, Player):
            return self.name == other.name
        return False

    def __lt__(self, other):
        '''Checks if this Player has a lower level than another Player.'''
        if isinstance(other, Player):
            return self.level < other.level
        return False

    def __le__(self, other):
        '''Checks if this Player has a lower or equal level to another Player.'''
        if isinstance(other, Player):
            return self.level <= other.level
        return False

    def __gt__(self, other):
        '''Checks if this Player has a higher level than another Player.'''
        if isinstance(other, Player):
            return self.level > other.level
        return False

    def __ge__(self, other):
        '''Checks if this Player has a hight or equal level to another Player.'''
        if isinstance(other, Player):
            return self.level >= other.level
        return False

# Constructing two Player objects
player1 = Player("Eldrin", 10)
player2 = Player("Aria", 5)

# Using '==' calls the __eq__ method
print(player1 == player2)  # Output: False

# Using '<' calls the __lt__ method
print(player1 < player2)   # Output: False

# Using '<=' calls the __le__ method
print(player1 <= player2)  # Output: False

# Using '>' calls the __gt__ method
print(player1 > player2)   # Output: True

# Using '>=' calls the __ge__ method
print(player1 >= player2)  # Output: True
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__add__`
```
def __add__(self, other):
    '''
    Used by the '+' operator.
    Defines how to add 'self' and 'other'.
    '''
```

<br>

## `__sub__`
```
def __sub__(self, other):
    '''
    Used by the '-' operator.
    Defines how to subtract 'other' from 'self'.
    '''
```

<br>

## `__mul__`
```
def __mul__(self, other):
    '''
    Used by the '*' operator.
    Defines how to multiply 'self' by 'other'.
    '''
```

<br>

## `__truediv__`
```
def __truediv__(self, other):
    '''
    Used by the '/' operator.
    Defines how to divide 'self' by 'other'.
    '''
```
real example:
```python
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __add__(self, other):
        '''Adds the levels of two Player objects.'''
        if isinstance(other, Player):
            return self.level + other.level
        return NotImplemented

    def __sub__(self, other):
        '''Subtracts the level of another Player from this Player's level.'''
        if isinstance(other, Player):
            return self.level - other.level
        return NotImplemented

    def __mul__(self, other):
        '''Multiplies the levels of two Player objects.'''
        if isinstance(other, Player):
            return self.level * other.level
        return NotImplemented

    def __truediv__(self, other):
        '''Divides this Player's level by another Player's level.'''
        if isinstance(other, Player):
            if other.level != 0:
                return self.level / other.level
            else:
                raise ValueError("Cannot divide by zero.")
        return NotImplemented



# Example usage
player1 = Player("Eldrin", 10)
player2 = Player("Aria", 5)

# Using '+' calls the __add__ method
print(player1 + player2)
# Output: 15


# Using '-' calls the __sub__ method
print(player1 - player2)            
# Output: 5


# Using '*' calls the __mul__ method
print(player1 * player2)            
# Output: 50


# Using '/' calls the __truediv__ method
print(player1 / player2)            
# Output: 2.0

```

<br>

[Back to Top](#python-methods)

___

<br>

## `__getattr__`
```
def __getattr__(self, name):
    '''
    Used by object.attr
    Defines how to return the attribute named 'name' if it exists; 
    otherwise, raises AttributeError.
    '''
```

<br>

## `__setattr__`
```
def __setattr__(self, name, value):
    '''
    Used by object.attr = value
    Defines how to set the attribute 'name' to 'value'.
    '''
```

<br>

## `__delattr__`
```
def __delattr__(self, name):
    '''
    Used by del object.attr
    Defines how to delete the attribute named 'name'.
    '''
```
Unlike getters, setters, and deleters, which are specific to individual attributes, __getattr__, __setattr__, and __delattr__ apply to all attributes. 

real example:
```python
class Player():                                 # Class Header
    '''
    Player Class that defines what a Player is (attributes), 
    and what a player does (methods)
    '''

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina

    def __getattr__(self, attr):
        '''Called when the requested attribute is not found in the usual places.'''
        if attr in self.__dict__:
            return self.__dict__[attr]
        else:
            raise AttributeError(f"'Player' object has no attribute '{attr}'")

    def __setattr__(self, attr, value):
        '''Called when an attribute assignment is attempted.'''
        self.__dict__[attr] = value


    def __delattr__(self, attr):
        '''Called when an attribute deletion is attempted.'''
        if attr in self.__dict__:
            del self.__dict__[attr]
        else:
            raise AttributeError(f"'Player' object has no attribute '{attr}'")


# Constructing a Player instance
player1 = Player("Eldrin the Brave", 150, 70, 85)
```

<br>

[Back to Top](#python-methods)

___

<br>

## `__hash__`
```
def __hash__(self):
    '''
    Used by the hash() function.
    Defines how to return a hash value of the object and
    as a key in dictionaries.
    '''
```
To implement the __hash__ method in a class, you'll also need to make sure the class is immutable, or at least ensure that the attributes used in the hash computation are immutable. This is because hash values need to remain constant for the lifetime of the object.

real example:
```python
class Player():                                 # Class Header
    '''
    Player Class that defines what a Player is (attributes), 
    and what a player does (methods)
    '''

    def __init__(self, name, hp, mp, stamina):
        '''Player class constructor with parameters'''
        self.name = name
        self.hp = hp
        self.mp = mp
        self.stamina = stamina


    def __hash__(self):
        '''Returns a hash value based on the Player's attributes.'''
        return hash((self.name, self.hp, self.mp, self.stamina))


# Constructing a Player instance
player1 = Player("Eldrin the Brave", 150, 70, 85)

hash(player1)       
# Returns: it varies based on the object, but usually a large integer value
```

<br>

## `__enter__`
```
def __enter__(self):
    '''
    Used by the 'with' statement.
    Defines what happens when entering the runtime context.
    '''
```

<br>

## `__exit__`
```
def __exit__(self, exc_type, exc_value, traceback):
    '''
    Used by the 'with' statement
    Defines what happens when exiting the runtime context.
    '''
```

<br>

real example:
```python
import json            
''' 
Here I import a json module to simplify the code in my examples.
It is not required for the __enter__ or __exit__ methods
It is only need so that I can provide a relevant example.
'''

class Player:
    def __init__(self, name, level,  hp, mp, stamina):
        self.name = name
        self.level = level
        self.hp = hp
        self.mp = mp
        self.stamina = stamina
        self.save_file = None

    def __enter__(self):
        '''Opens a save file when entering the context.'''
        self.save_file = open(f'{self.name.replace(" ","-")}_save.json', 'w')
        
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Closes the save file when exiting the context.'''
        if self.save_file:
            self.save_file.close()
            self.save_file = None

        return False
# end of class definition

# Constructing a Player instance
player1 = Player("Eldrin the Brave", 1, 150, 70, 85)

# Using 'with' uses the __enter__ and __exit__ methods
with player1 as p:  # __enter__ called
    json.dump(str(p.__dict__), p.save_file)         # This creates a json object to save.
# __exit__ called
```

<br>

[Back to Top](#python-methods)

___

<br>

*Created and maintained by Mr. Merritt*




