# `Python Dictionaries`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Collection Types`](#collection-types)
1. [`Defining a Dictionary: Key:Value Pairs`](#defining-a-dictionary-keyvalue-pairs)
1. [`Creating a Dictionary`](#creating-a-dictionary)
1. [`Converting to and from a Dictionary`](#convert-to-and-from-a-dictionary)
1. [`Accessing Dictionary Items`](#accessing-dictionary-items)
1. [`Changing Dictionary Items`](#changing-dictionary-items)
1. [`Dictionary Operations`](#dictionary-operations)
    1. [`Checking Dictionary Membership`](#checking-dictionary-membership)
    1. [`Deleting key:value pairs`](#deleting-keyvalue-pairs)
    1. [`Comparing Dictionary Contents`](#comparing-dictionary-contents)
    1. [`Merging Dictionaries`](#merging-dictionaries)
1. [`Built-in Dictionary Function Calls`](#built-in-dictionary-function-calls)
1. [`Built-in Dictionary Method Calls`](#built-in-dictionary-method-calls)
1. [`Nested Dictionaries`](#nested-dictionaries)
1. [`Iterating Through Dictionaries`](#iterating-through-dictionaries)
    1. [`Loop through dictionary keys`](#loop-through-dictionary-keys)
    1. [`Loop through dictionary values`](#loop-through-dictionary-values)
    1. [`Loop through key:value pairs`](#loop-through-keyvalue-pairs)
1. [`Unpacking Dictionaries`](#unpacking-dictionaries)
    1. [`Unpack into variables`](#unpack-into-variables)
    1. [`Unpack Multiple Key:Value pairs`](#unpack-multiple-keyvalue-pairs)
1. [`Dictioanry Comprehension`](#dictionary-comprehension)
    1. [`Including a Filter Statement`](#including-a-filter-statement)


<br>

___

<br>

# `Collection Types`

There are four major collection data types in the Python programming language:

A `List` is a collection which is ordered(indexed), mutable, allows duplicate members, and uses [ ] to enclose members.
```python
list1d = [1,2,3]
```

<br>

A `Tuple` is a collection which is ordered(indexed), immutable, allows duplicate members and uses ( ) to enclose members.
```python
tuple1d = (1,2,3)
```

<br>

A `Set` is a collection which is unordered(not indexed), mutable, does NOT allow duplicate members and uses { } to enclose members.
```python
set1d = {1,2,3}
```

<br>

A `Dictionary` is a collection which is ordered(indexed with a key), mutable, does NOT allow duplicate members and uses { : } to enclose members.
```python
dict1d = {"a": 1, "b": 2,"c": 3}
```

<br>

|`List`|`Tuple`|`Set`|`Dictionary`|
|:-:|:-:|:-:|:-:|
|ordered (numerically indexed)|ordered (numerically indexed)|unordered (not indexed)|ordered (indexed with a key)|
|mutable|immutable|mutable|mutable|
|duplicates|duplicates|NO duplicates|NO duplicates|
|**[ ]**|**( )**|**{ }**|**{ : }**| 

* *`Data Structure`: a specialized format for organizing, processing, retrieving, and storing data.*
* *`Collection`: a data structure that holds multiple elements*
* *`Member`: an item stored within a collection*
* *`Element`: is a synonym for member*
* *`Ordered`: having a specific order 0,1,2,... (ie. indexed)*
* *`Indexed`:  elements are associated with a specific identifier (index), which can be used to directly locate and access the data*
* *`Mutable`: elements can change*
* *`Immutable`: elements cannot change*


<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Defining a Dictionary: Key:Value Pairs`
Basically: A `dictionary` is a list that maps two values together; a key and a value. 

Specifically: A dictionary is a collection which is ordered(indexed with a key), mutable, does NOT allow duplicate members and uses { : } to enclose members.
> * In other programming languages dictionaries are called: maps, hashmaps, or associative arrays

Dictionary syntax:

    {key1:value1, key2:value2, ...}

`Dictionary keys must be an immutable data type`


example:
```python
{"name": "John", "age" :22, "school" : "University of Louisville","good_standing" : True}
# key  : value , 


#add a newline after a comma to make the dictionary more readable

{
    "name": "John", 
    "age" : 22, 
    "school" : "University of Louisville",
    "good_standing" : True
}

# Other examples
numerals = {
  '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
  '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
}

ucase_alpha = {
  'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 
  'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 
  'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 
  'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 
  'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 
  'Z': 90
}

lcase_alpha = {
  'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 
  'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 
  'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 
  'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116,
  'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121,
  'z': 122
} 
```

<br>

## `Note on dictionaries`
While not always called dictionaries, dictionaries show up quite a bit in computer science.
> * Dictionaries are use to store configuration data, track state in applications, databases, form data, etc.

Dictionaries are also knowns as:
>   * associative arrays  
>   * hashmaps  
>   * maps  
>   * javascript objects  
>   * Tables  
>   * hash table  
>   * symbol table  

Dictionary values are hashed, meaning that key values are mapped to the memory location of the values. 

> *Hashing refers to the use of hash tables that utilize hash functions to convert data (usually text or binary) into a fixed-size string of characters, which is typically a hash value or hash code. This value is then mapped to unique identifiers or memory addresses, allowing for quick lookup, insertion, or deletion operations.*

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Creating a Dictionary`
Use `{:}` to denote a dictionary.
> * seperate key:value pairs with commas
> * the `dict(iterable)` constructor builds a dictionary

There are several ways to create a dictionary:

<br>

### Create an empty dictionary with `{}`
```python
{} #creates an empty dictionary

dict1d = {}
```

<br>

### Enclose comma separated key:value pairs with `{}`
```python
dictionary = {
    "name": "John", 
    "age" : 22, 
    "school" : "University of Louisville",
    "good_standing" : True
}
```

<br>

### Use the `dict(iterable)` constructor call to build dictionaries from sequences of key-value pairs
```python
dict() # Returns: {}
```
> * Using an iterable with data pairs
```python
# Converting from a list of tuples
list1d = [("a", 97),("b",98),("c",99)]
dict(list1d)
# Returns: {'a': 97, 'b': 98, 'c': 99}
```

<br>

### Using keyword arguments

syntax:

    dict(key=value,...)


```python
dict(a=97, b=98, c=99)
# Returns: {'a': 97, 'b': 98, 'c': 99}
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Convert to and from a Dictionary`
To convert to a dictionary use the `dict()` constructor as used above
> * To convert a dictionary to another collection type use the ***list(), tuple(), or set()*** constructors

<br>

`When converting to a list, tuple or set, only the keys of the dictionary are used`


```python
dictionary = {'a': 97, 'b': 98, 'c': 99}

key_list = list(dictionary)     # Returns: ['a', 'b', 'c']
key_tuple = tuple(dictionary)   # Returns: {'a', 'b', 'c'}
key_set = set(dictionary)       # Returns: ('a', 'b', 'c')
# Note: remember that sets are unordered
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Accessing Dictionary Items`
There are several ways to access the items inside a dictionary
> Use the dictionary and a key to retrieve the value

<br>

Subscripting `[]` syntax

    dict[key]

```python
dictionary = {'a': 97, 'b': 98, 'c': 99}

dictionary["a"]                 # Returns: 97
```

<br>

`get()` method syntax
> *Here [ ] indicates an optional parameter*

    dict.get(key[,default])

```python
dictionary = {'a': 97, 'b': 98, 'c': 99}

dictionary.get("b")             # Returns: 98
dictionary.get("d","Not Found") # Returns: Not Found
```

<br>


Returning a list of keys with `dict.keys()`


```python
numerals = {
  '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
  '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
}

numerals.keys()
# Returns: dict_keys(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
```

<br>

Returning a list of values with `dict.values()`
```python
numerals = {
  '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
  '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
}

numerals.values()
# Returns: dict_values([48, 49, 50, 51, 52, 53, 54, 55, 56, 57])
```

<br>

Returning a list of tuples containing the key value pairs with `dict.items()`


```python
numerals = {
  '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
  '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
}

numerals.items()
# Returns: dict_items([('0', 48), ('1', 49), ('2', 50), ('3', 51), ('4', 52), ('5', 53), ('6', 54), ('7', 55), ('8', 56), ('9', 57)])
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Changing Dictionary Items`
There are several ways to change the values in a dictionary


Use `dict[key] =` to assign a new value to the key  

syntax

    dict[key] = new_value

> *If the key does not exist it is added to the dictionary along with its value*


```python
upper_alpha = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69}

upper_alpha['A'] = 41
upper_alpha['B'] = 42
upper_alpha['C'] = 43
upper_alpha['D'] = 44
upper_alpha['E'] = 45

# key doesn't exist
upper_alpha['F'] = 46

print(upper_alpha)
# Output: {'A': 41, 'B': 42, 'C': 43, 'D': 44, 'E': 45, 'F': 46}
```

<br>

Add Values from another dictionary or iterable type with `key:value` pairs  

syntax:

    dict.update(iterable)
    
```python
weekdays = {"Mon": "Monday", "Tue":"Tuesday","Wed":"Wednesday","Thur":"Thursday","Fri":"Friday"}
weekend = {"Sat":"Saturday","Sun":"Sunday"}

weekdays.update(weekend) # Returns: None

print(weekdays)
# Output: {'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thur': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday'}
```


```python
current_users = {
    "CosmicCaleb89": "e10adc3949ba59abbe56e057f20f883e",
    "GalacticCaden77": "5f4dcc3b5aa765d61d8327deb882cf99",
    "KyleeKraze45": "25d55ad283aa400af464c76d713c07ad",
    "LeilaLegend14": "8621ffdbc5698829397d97767ac13db3",
    "MelaneeMystic22": "d8578edf8458ce06fbc5bb76a58c5ca4",
    "JackNova66": "0d107d09f5bbe40cade3de5c71e9e9b7" 
}

new_users = {
    "BrooklynX7L4M3": "e99a18c428cb38d5f260853678922e03", 
    "NavaehQ3M8P1": "1a1dc91c907325c69271ddf0c944bc72"
}

current_users.update(new_users) # Returns: None


current_users.update({"MasonD3Y2X7": "df53ca268240ca76670c8566ee54568a" }) # Returns: None


print(current_users)
# Output:
# {'CosmicCaleb89': 'e10adc3949ba59abbe56e057f20f883e', 
# 'GalacticCaden77': '5f4dcc3b5aa765d61d8327deb882cf99', 
# 'KyleeKraze45': '25d55ad283aa400af464c76d713c07ad', 
# 'LeilaLegend14': '8621ffdbc5698829397d97767ac13db3', 
# 'MelaneeMystic22': 'd8578edf8458ce06fbc5bb76a58c5ca4', 
# 'JackNova66': '0d107d09f5bbe40cade3de5c71e9e9b7', 
# 'BrooklynX7L4M3': 'e99a18c428cb38d5f260853678922e03', 
# 'NavaehQ3M8P1': '1a1dc91c907325c69271ddf0c944bc72', 
# 'MasonD3Y2X7': 'df53ca268240ca76670c8566ee54568a'
# }
```

<br>


[Back to Top](#python-dictionaries)

___

<br>


# `Dictionary Operations`

|Operator|Operation|
|:-:|:-:|
|`in`| Check if a key exists in the dictionary|
|`not in`| Check if a key does NOT exist in the dictionary|
|`del`| Delete a key:value pair in the dictionary|
|`==`| compare the contents of two dictionaries regardless of order|
|`\|`| merge two dictionaries; the values of the second dictionary take priority when keys are shared|
|`\|=`| update one dictionary with the values of a second dictionary|

<br>

## `Checking Dictionary Membership`
Use `in` to check if a `key` is apart of a dictionary
  
syntax:

    key in dict


```python
bin_alpha = {
    "a": "0b01100001",
    "b": "0b01100010",
    "c": "0b01100011"
}

"a" in bin_alpha  # Returns: True
"d" in bin_alpha # Returns: False

```

<br>

Use `not in` to check if a `key` is NOT in the dictionary  

syntax:

    key not in dictionary


```python
bin_alpha = {
    "a": "0b01100001",
    "b": "0b01100010",
    "c": "0b01100011"
}

"b" not in bin_alpha  # Returns: False 
"m" not in bin_alpha  # Returns: True
```

<br>


## `Deleting key:value pairs`
Use `del` to delete a `key:value` pair in the dictionary  

syntax:

    del dict[key]


```python
bin_alpha = {
    "a": "0b01100001",
    "b": "0b01100010",
    "c": "0b01100011"
}

del bin_alpha["c"]

print(bin_alpha)
# Output:
# {'a': '0b01100001', 'b': '0b01100010'}
```

<br>

## `Comparing Dictionary Contents`
Use `==` to compare the contents of two dictionaries regardless of order  

syntax:

    dict1 == dict2


```python
dict1 = {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102}
dict2 = {'d': 100, 'e': 101, 'f': 102,'a': 97, 'b': 98, 'c': 99 }

dict1 == dict2 # Returns: True
```

<br>

## `Merging Dictionaries`

Use `|` to merge teh contents of two
>   * The values of the second dictionary take priority when keys are shared between the two dictionaries

syntax:

    dict1 | dict2


```python
alpha_bin = {'a': '0b1100001', 'b': '0b1100010', 'c': '0b1100011', 'd': '0b1100100', 'e': '0b1100101', 'f': '0b1100110'}
alpha_hex = {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'} 

alpha_bin | alpha_hex 
# Returns: {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'}
```


```python
alpha_bin1 = {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'}
alpha_bin2 = {'a': '0b1100001', 'b': '0b1100010', 'c': '0b1100011', '1': '0b110001', '2': '0b110010', '3': '0b110011'}

alpha_bin1 |= alpha_bin2
# Returns: 
# {
#  'a': '0b1100001', 'b': '0b1100010', 'c': '0b1100011', 
#  'd': '0b1100100', 'e': '0b1100101', 'f': '0b1100110', 
#  '1': '0b110001', '2': '0b110010', '3': '0b110011'
# } 
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Built-in Dictionary Function Calls`
`Functions` are blocks of reusable code, that perform a specific task.
> * must be defined before they are called
> * are typically called using their name followed by parenthesis with any required arguments inside.


`Built-in Functions are pre-defined by the Python standard library`


```python
#len(dictionary) return the number of elements
len(ucase_alpha) #26

#iter(dictionary) return an iterator over the keys of the dictionary. 
iter(ucase_alpha)

#reversed(dictionary) return a reverse iterator over the keys of the dictionary.
reversed(ucase_alpha)
```

<br>


[Back to Top](#python-dictionaries)

___

<br>


# `Built-in Dictionary Method Calls`
`Methods` are functions defined by a class
> * are typically called using an object or class and dot ( . ) syntax

<br>

> syntax for methods which require objects:

    object.method(arguments)

> syntax for methods which DO NOT require objects:

    class.method(arguments)

`Built-in methods are pre-defined by classes pre-defined by the standard library`

> To see what methods you can call on an object use:  
    
    dir(object)  

> To see more information on a specific method use:  
    
    help(object.method)


```python
# dict.copy() return a shallow copy of a dictionary
ucase_alpha.copy()

# dict.fromkeys(iterable[, value=None]) returns a new dictionary with specified keys and optional default values.
keys = ['a', 'b', 'c']
default_value = 0
dict.fromkeys(keys, default_value)

#dict.pop(key[,default=]) iff key is in the dictionary, remove it and return its value, else return default. 
ucase_alpha.pop("example", "Not Found")

#dict.popitem() remove and return a (key, value) pair from the dictionary. Pairs are returned in last in first out(LIFO) order.
ucase_alpha.popitem()

# setdefault(key[, default]) If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.
ucase_alpha.setdefault("example", None)

# dict.clear() remove all items from the dictionary.
ucase_alpha.clear() # {}
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Nested Dictionaries`
`Nested Dictionaries` are dictionaries that contain other dictionaries.


```python
alphanumeric = {
    "numerals" :  {
        '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
        '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
    },
    "upper_alpha" : {
        'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 
        'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 
        'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 
        'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 
        'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 
        'Z': 90
    },
    "lower_alpha" : {
        'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 
        'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 
        'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 
        'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116,
        'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121,
        'z': 122
    } 
}

#Access
alphanumeric["numerals"]["7"] # Returns: 55
alphanumeric.get("upper_alpha").get("X") # Returns: 88
alphanumeric.get("lower_alpha").get("?", "Not Found") # Returns: Not Found

#Change
alphanumeric["symbols"] = {}
alphanumeric["symbols"]["!"] = 33

```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Iterating through Dictionaries`
It is often necessary to go through the contents of a dictionary item by item. This is called `iterating` through a dictionary.

> There are multiple ways to iterate through a dictionaries items


<br>

## `Loop through dictionary keys`

syntax:
```
for key in dict:
    ...
```  
OR 
```
for key in dict.keys():
    ...
```


```python
alpha_hex = {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'} 

for key in alpha_hex:
    print(key, end = " ")
#Output: a b c d e f

for key in alpha_hex.keys():
    print(key, end = " ")
#Output: a b c d e f
```

<br>

## `Loop through dictionary values`

syntax:

    for value in dict.values():
        ...


```python
alpha_hex = {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'} 

for value in alpha_hex.values():
    print(value, end = " ")
#Output: 0x61 0x62 0x63 0x64 0x65 0x66 
```

<br>

## `Loop through key:value pairs`
syntax:

    for key,value in dict.items():
        ...


```python
alpha_hex = {'a': '0x61', 'b': '0x62', 'c': '0x63', 'd': '0x64', 'e': '0x65', 'f': '0x66'} 

for key, value in alpha_hex.items():
    print(key, value, end = ", ")
#Output: a 0x61, b 0x62, c 0x63, d 0x64, e 0x65, f 0x66,
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Unpacking Dictionaries`
`Unpacking` refers to the process of extracting individual elements from a container (such as a list, tuple, dictionary)
> * Values in a collection can be automatically assigned to variables
> * Use the `**` symbol to unpack multiple `key:value` pairs into a single variable
>
> * This used with `*args` and `**kwargs`, see variable length arguments 

<br>

## `Unpack into variables`

```python
alpha = {'a': 97, 'b': 98, 'c': 99}

a, b, c = alpha.values()

x, y, z = alpha.keys()

```

<br>

## `Unpack Multiple Key:Value pairs` 
Unpack Multiple Key:Value pairs with `**`

```python
alpha = {'a': 97, 'b': 98, 'c': 99}
beta = {'d': 100, 'e': 101, 'f': 102}

cappa = {**alpha, **beta}
print(cappa)
#Output: {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102}
```


```python
alpha = {'a': 97, 'b': 98, 'c': 99}
beta = {'d': 100, 'e': 101, 'f': 102}

def example(a,b,c):
    print(a, b, c)

example(**alpha) # Output: 97 98 99
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

# `Dictionary Comprehension`
A `dictionary comprehension` is a shorthand way to algorithmically create a dictionary

syntax:

    {key_expression:value_expression for item in iterable}


```python
times_table_9 = {num: num * 9 for num in range(5)}

print(times_table_9) # Output: {0: 0, 1: 9, 2: 18, 3: 27, 4: 36}
```


```python
numerals = {str(x) : ord(str(x)) for x in range(10)}
print(numerals)
# Output: {'0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57}
```

<br>

## `Including a filter statement`

syntax:

    {key_expression:value_expression for item in iterable if condition}



```python
even_squares = {num: num**2 for num in range(10) if num % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

<br>


[Back to Top](#python-dictionaries)

___

<br>

*Created and maintained by Mr. Merritt*  