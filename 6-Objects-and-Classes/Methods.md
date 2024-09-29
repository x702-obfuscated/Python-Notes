*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

# `Methods`

Covered in this file:
1. Methods Defined  
1. Access Modifiers 
1. Instance Methods  
1. Static and Class Methods  
1. Getters, Setters, Deleters and the Property Function  
1. Special Methods

<br>

# `Methods Defined`
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

# `Access Modifiers`
> Access modifiers in Python determine the accessibility and visibility of class attributes and methods from outside the class, using naming conventions (e.g., public, protected, private) instead of explicit keywords like in other languages.

Access Modifier Conventions:  

## Public
> * Accessible from anywhere. No prefixing.     

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

## Protected
> * Indicated by a single underscore (_) prefix, suggesting that it should not be accessed directly outside of the class and its subclasses.  
> * This is just a convention and is not enforced by the Python interpreter

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

## Private
> * Indicated by a double underscore (__) prefix, suggesting that it should not be accessed from outside of the class.  
> * Trying to access the private method or attribute directly will result in an AttributeError 

Name Mangling
> * When you define a method or attribute with a name that starts with double underscores, Python internally changes the name by prefixing it with _ClassName

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


# `Instance Methods`
## Instance Methods
What an object does (its behaviour)
> * basically: a function defined in a class that operates on an instance of a class(object)  
> * specifically: functions defined within a class that operate on a specific instance, taking self as their first parameter to access and modify the instance's attributes and define behaviors unique to that object.

## Defining Instance Methods
> * instance methods are defined within the class and require ***self*** as the first parameter.

syntax:
```
class ClassName():

    def instance_method(self, parameters, ...):
        <Method Body>
        ...
```

real example:
```python
class Player():                                 # Class Header
    '''
    Player class that defines what a Player is (attributes), 
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

## Calling Instance Methods
> * instance methods require an object in order to be called
> * instance methods are called using dot syntax

syntax:  
```
object.method(arguments, ...)
```

real example:
```python
class Player():                                 # Class Header
    '''
    Player Class that defines what a Player is (attributes), 
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

#end of class definition

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

# `Static and Class Methods`
## Static Methods
> * are methods that logically belong to the class but do not require access to the class or its instances
> * these are typically utility functions

***NOTE: the @staticmethod decorator we use here is not required for static methods, but is a good practice for clarity, design, and readability.***

syntax:
```
class ClassName():

    @staticmethod
    def method_name(parameters, ... ):
        ...
```

Static Methods work just like other functions, but are called using dot syntax.  
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

# end class definition


player1 = Player()              # Object Instantiation

Player.is_valid_score(1)        # ClassName.static_method()
# Returns: True

player1.is_valid_score(1)       # object_name.static_method()
# Returns: True
```

Using an object to call a static method without the @staticmethod decorator will result in a compile time *TypeError*  
real example:
```python
class Player():                 # Class Definition Header

    # Static Method Definition
    #                           <-- NO DECORATOR
    def is_valid_score(score):  
        """Static method to check if the given score is valid."""
        return(isinstance(score, int) and score >= 0)

# end class definition


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

## Class Methods
> * are methods that are associated with the class, and can modify the state of the class that applies to all instances.      
> * can access class variables, but not instance variables
> * use the @classmethod decorator    
  
> * ***cls*** is always the first parameter in Class methods. This parameter represents the Class, and is automatically passed when using dot syntax.  

syntax:
```
class Class_Name():

    @classmethod
    def class_method(cls, parameters,  ... ):
        ...
```
Class Methods work just like other functions, but are called using dot syntax.  
syntax:
```
ClassName.class_method(cls, arguments, ... )
```
When using an object to call a class method, the class of the object is passed to the ***cls*** parameter. 
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

#end of class definition

data = {
    "name":"Vector",
    "score": 75
}

#          Class.class_method()
player1 = Player.from_dict(data)        # Returns a Player object

player1.display()
# Output: Player: Vector, Score: 75



info = {
    "name":"Stewart",
    "score": 50
}

#          object.class_method()          Player is passed to cls
player2 = player1.from_dict(info)       # Returns a Player object

player2.display()
# Output: Player: Stewart, Score: 50
```

<br>

# `Getters, Setters, Deleters and the Property Function`
## Getters
> * methods used to control how data is retrieved  
> * typically prefixed with "get"  
> * need to return a value
```
def get_variable():
    return ...
```
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

    def get_name(self):
        '''self.name getter'''
        return self.name
```
## Setters
> * methods used to control how data is changed
> * typically prefixed with "set"
```
def set_variable():
    ...
```
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


    def set_hp(self, value):
        '''self.hp setter'''
        if value < 0:
            raise ValueError("HP cannot be negative")
        self.hp = value
```

## Deleters
> * methods used to control how data is deleted
> * typically prefixed with "del"
``` 
def del_variable():
    ...
```
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


    def del_hp(self):
        '''self.hp deleter'''
        raise AttributeError("Cannot delete 'hp' attribute")
```

## property()
> * function that maps getters, setters, and deleters to a variable, so that they are automatically called when the variable is accessed.   
> * it is considered best practice to use the @property decoratar instead. Take a look at decorators to learn more.
> * private or protected values must be used to prevent RecursionError: maximum recursion depth exceeded
syntax:
```
property(fget = None, fset = None, fdel = None, doc = None)
```
real example:
```python
class Player():                                 # Class Header
    '''
    Player Class that defines what a Player is (attributes), 
    and what a player does (methods)
    '''

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

# end of class definition

# Constructing a Player instance
player1 = Player("Eldrin the Brave", 150, 70, 85)


print(player1.mp)              # Calls player1.get_mp()     
# Output: 70    

player1.mp = -1                # Calls player1.set_mp(-1)
# Raises: ValueError: mp cannot be negative

del player1.mp                 # Calls player1.del_mp()
# Raises: AttributeError: Cannot delete 'mp' attribute
```

example using the @property decorator
syntax:

    @property

    @<property_name>.setter
    @<property_name>.deleter


real example:
```python
class Player():                                 # Class Header
    '''
    Player Class that defines what a Player is (attributes), 
    and what a player does (methods)
    '''

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
    

# end of class definition

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

# `Special Methods to define:`
There are several special 'dunder' methods that can be defined in a class and perform special functions when defined. 

*dunder is short for double underscore*
special dunder methods:

> \_\_str\_\_, \_\_repr\_\_, \_\_len\_\_, \_\_getitem\_\_ , \_\_setitem\_\_, \_\_delitem\_\_, \_\_iter\_\_ , \_\_next\_\_, \_\_contains\_\_, \_\_eq\_\_, \_\_lt\_\_, \_\_le\_\_, \_\_gt\_\_, \_\_ge\_\_, \_\_add\_\_, \_\_sub\_\_, \_\_mul\_\_, \_\_truediv\_\_, \_\_call\_\_, \_\_getattr\_\_, \_\_setattr\_\_, \_\_delattr\_\_, \_\_hash\_\_, \_\_enter\_\_, \_\_exit\_\_

## \_\_init__
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
## \_\_str__
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
## \_\_repr__
```
def __repr__(self):
    '''
    Used by the repr() function.
    Returns a detailed string representation of the object for debugging.
    '''
```
***NOTE: the !r in a formatted string (using f-strings) is a conversion flag that specifies that the repr() function should be used to format the value.***  
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
## \_\_len__
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
## \_\_getitem__
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
## \_\_setitem__
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
## \_\_delitem__
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
## \_\_iter__
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
## \_\_next__
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
## \_\_contains__
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
## \_\_eq__
```
def __eq__(self, other):
    '''
    Used by the '==' operator.
    Defines how to check if the object is equal to 'other'.
    '''
```
## \_\_lt__
```
def __lt__(self, other):
    '''
    Used by the '<' operator.
    Defines how to check if the object is less than 'other'.
    '''
```
## \_\_le__
```
def __le__(self, other):
    '''
    Used by the '<=' operator.
    Defines how to check if the object is less than or equal to 'other'.
    '''   
```
## \_\_gt__
```
def __gt__(self, other):
    '''
    Used by the '>' operator.
    Defines how to check if the object is greater than 'other'.
    '''
```
## \_\_ge__
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
## \_\_add__
```
def __add__(self, other):
    '''
    Used by the '+' operator.
    Defines how to add 'self' and 'other'.
    '''
```
## \_\_sub__
```
def __sub__(self, other):
    '''
    Used by the '-' operator.
    Defines how to subtract 'other' from 'self'.
    '''
```
## \_\_mul__
```
def __mul__(self, other):
    '''
    Used by the '*' operator.
    Defines how to multiply 'self' by 'other'.
    '''
```
## \_\_truediv__
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

## \_\_getattr__
```
def __getattr__(self, name):
    '''
    Used by object.attr
    Defines how to return the attribute named 'name' if it exists; 
    otherwise, raises AttributeError.
    '''
```
## \_\_setattr__
```
def __setattr__(self, name, value):
    '''
    Used by object.attr = value
    Defines how to set the attribute 'name' to 'value'.
    '''
```
## \_\_delattr__
```
def __delattr__(self, name):
    '''
    Used by del object.attr
    Defines how to delete the attribute named 'name'.
    '''
```
Unlike getters, setters, and deleters, which are specific to individual attributes, \_\_getattr\_\_, \_\_setattr\_\_, and \_\_delattr\_\_ apply to all attributes. 

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
## \_\_hash__
```
def __hash__(self):
    '''
    Used by the hash() function.
    Defines how to return a hash value of the object and
    as a key in dictionaries.
    '''
```
> To implement the \_\_hash__ method in a class, you'll also need to make sure the class is immutable, or at least ensure that the attributes used in the hash computation are immutable. This is because hash values need to remain constant for the lifetime of the object.

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

## \_\_enter__
```
def __enter__(self):
    '''
    Used by the 'with' statement.
    Defines what happens when entering the runtime context.
    '''
```
## \_\_exit__
```
def __exit__(self, exc_type, exc_value, traceback):
    '''
    Used by the 'with' statement
    Defines what happens when exiting the runtime context.
    '''
```

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



## Built-in Methods
Built-in methods are pre-defined by classes pre-defined by the standard library

To see what methods you can call on an object use:  
    
    dir(object_name)  

To see more information on a specific method use:  
    
    help(object_name.method_name)

<br>
