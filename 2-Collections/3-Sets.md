# `Python Sets`


Covered in this file
1. [`Collection Types`](#collection-types)
1. [`Defining a Set`](#defining-a-set)
1. [`Creating a Set`](#creating-a-set)
1. [`Converting from Lists and Tuples`](#converting-from-lists-and-tuples)
1. [`Set Operations`](#set-operations)
    1. [`Checking Set Membership`](#checking-set-membership)
    1. [`Union`](#union)
    1. [`Intersection`](#intersection)
    1. [`Difference`](#difference)
    1. [`Symmetric Difference`](#symmetric-difference)
    1. [`Delete a Set`](#delete-a-set)
1. [`Individual Set Elements Cannot be Accessed`](#individual-set-elements-cannot-be-accessed)
1. [`Individual Set Elements Cannot be Changed`](#individual-set-elements-cannot-be-changed)
1. [`Built-in Set Function Calls`](#built-in-set-function-calls)
1. [`Built-in Set Method Calls`](#built-in-set-method-calls)
1. [`Unpacking Collections`](#unpacking-collections)
1. [`Unpacking Into Variables`](#unpacking-into-variables)
1. [`Unpacking Multiple Values Into One Variable`](#unpacking-multiple-values-into-one-variable)
1. [`Ignore Unpacked Values`](#ignore-unpacked-values)
1. [`Set Comprehension`](#set-comprehension)
1. [`Set Iteration: Looping`](#set-iteration-looping)

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


[Back to Top](#python-sets)

___

<br>


# `Defining a Set`
Basically: A `Set` is a list with no order, and no duplicates.

Specifically: A `Set` is a collection which is unordered(not indexed), mutable, and does NOT allow duplicate members.
> * use `{}` to enclose members.
> * can only contain immutable types

<br>

*Sets in Python can only contain immutable types because sets rely on the concept of hashing to ensure the uniqueness of their elements and to provide efficient access.*

<br>

A `set` contains multiple items called `elements` or `members`. 

<br>

> ***Sets unlike lists, tuples, and dictionaries are not indexed and have no order.***

The `length` of a set is the total number of elements contained in the list  

<br>

example:
```python
{"a","b","c","d","e"} #a Set

#add a newline after a comma to make the Set more readable
{'a', 'b', 'c', 'd', 'e', 
 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 
 'z'
}

# Other examples:
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

bools  = {True, False}

numerals = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

lcase_alpha = {
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
}

ucase_alpha = {
    'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z'
}
```

<br>


[Back to Top](#python-sets)

___

<br>

# `Creating a Set`
Use `{}` to denote a Set
> * seperate elements of a Set with commas
> * The `set(iterable)` constructor builds a Set

<br>

### Create an empty set with `{}`
```python
{} # creates an empty set

set1d = {}
```

<br>

### Enclose comma seperated elements with `{}`
```python
set1d = {1,2,3,4,5,6,7,8,9}
```

<br>

### Use the `set(iterable)` constructor call
syntax:

    set(iterable)

```python
#use the set(iterable) constructor call
set() # Returns: {}
set('abcdef') # Returns in random order: {}'a', 'b', 'c', 'd', 'e', 'f'}
```

<br>


[Back to Top](#python-sets)

___

<br>


# `Converting from Lists and Tuples`

> * The `list(iterable)` constructor builds a list
> * The `tuple(iterable)` constructor builds a tuple
> * The `set(iterable)` constructor builds a set

<br>

`Constructors` are special methods defined by a class that are used to build instances of a class. 
> * ie. the `set(iterable)` constructor makes a set.


```python
set("abcdef") #Returns: {'a', 'b', 'c', 'd', 'e', 'f'}
```


```python
list1d = ["dog","cat","horse","horse"]

set(list1d) # Returns: {'cat', 'dog', 'horse'}
```

```python
set1d = {1,2,3,4,5}

# From set to tuple use tuple(iterable))
tuple1d = tuple(set1d) # Returns: (1,2,3,4,5)

#From set to list use list(iterable)
list1d = list(set1d) # Returns: [1,2,3,4,5]
```

<br>


[Back to Top](#python-sets)

___

<br>

# `Set Operations`


|Operation| Description|
|:-:|:-:|
|`in`| checks if a value is a member|
|`not in`| checks if a value is not a member|
|`\`||Union: joins a set with another iterable|
|`&`|Intersection: joins and keeps only duplicates |
|`-`|Difference: joins and keeps all items from the first that are not present in the second|
|`^`|Symmetric Difference: joins and keeps all but duplicates|
|`del`| Deletes a set|

<br>

## `Checking Set Membership`
Use `in` to check if a value is a member of a set

syntax:

    value in set


```python
numerals = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

"1" in numerals # Returns: True
"a" in numerals # Returns: False
```

<br>

Use `not in` to check if a value is not apart of a set
syntax:

    value not in set


```python
numerals = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

"1" not in numerals # Returns: False
"a" not in numerals # Returns: True
```

<br>

## `Union`
Use `|` to join a set with another iterable

syntax:

    set | iterable
    
```python
set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,0}
set_3 = {4,5,6,7,8}

set_1 | set_2 # Returns in random order: {1,2,3,4,5,6,7,8,9,0}
set_2 | set_3 # Returns in random orde: {9,0,4,5,6}
#creates a new set of all unique elements from both sets
```

<br>

## `Intersection`
Use `&` to join a set with another set keeping only the duplicates.

syntax:

    set1 & set2


```python
set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,0}
set_3 = {4,5,6,7,8}

set_1 & set_3 #  Returns in random order: {4,5,6}
set_2 & set_3 #  Returns in random order: {7,8}
```

<br>

## `Difference` 
Use `-` to keep all items from the first set not present in the second.

syntax:

    set1 - set2


```python
set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,0}
set_3 = {4,5,6,7,8}

set_1 - set_3 # Returns in random order: {1,2,3}
set_2 - set_3 # Returns in random order: {9,0}
```

<br>

## `Symmetric Difference` 
Use `^` to join two sets keeping all but the duplicates.

syntax:

    set1 ^ set2


```python
set_1 = {1,2,3,4,5,6}
set_2 = {7,8,9,0}
set_3 = {4,5,6,7,8}

set_1 ^ set_3 # Returns in random order:{1,2,3,7,8}
set_2 ^ set_3 # Returns in random order:{4,5,6,9,0}
```

<br>

## `Delete a Set`
Use `del` to delete a set.

syntax:

    del set

```python
set1d = {"a","b","c"}
del set1d
```

<br>


[Back to Top](#python-sets)

___

<br>


# `Individual Set Elements Cannot be Accessed`
Sets are unordered and therfore unindexed, this means that it is not possible to access and individual elements in a set without iteration.

<br>


[Back to Top](#python-sets)

___

<br>

# `Individual Set Elements Cannot be Changed.`


Sets are unordered and therfore unindexed, this means that it is not possible change individual values of a set. 

<br>

HOWEVER, there are some functions and methods that can be used to change what data the set stores.

<br>


[Back to Top](#python-sets)

___

<br>

# `Built-in Set Function Calls`
`Functions` are blocks of reusable code, that perform a specific task.
> * must be defined before they are called
> * are typically called using their name followed by parenthesis with any required arguments inside.


`Built-in Functions are pre-defined by the Python standard library`


```python
set1d = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# len()
len(set1d) #Returns number of elements in a set

#max()
max(set1d) #Returns the largest element in the set.

#min()
min(set1d)#Returns the smallest element in the set.

#sum(set1d)
nums = {1,2,3,4,5}
sum(nums) #Returns the sum of all elements in a number set.

#Returns a sorted set in ascending order
sorted(set1d)

#Combines two sets into an iterator of tuples 
set1 = {"a","b","c"}
set2 = {1,2,3}
zip(set1, set2)
# ("a",1),("b",2),("c",3)

```

<br>

[Back to Top](#python-sets)

___

<br>

# `Built-in Set Method Calls`
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
set1d = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

# set1d.add(element) adds an element to the set.
set1d.add(10)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# set1d.clear() removes all elements from the set.
set1d.clear()  # {}

# set1d.copy() returns a shallow copy of the set.
set1d = {1, 2, 3}
set1d.copy()  # {1, 2, 3}

# set1d.difference(*others) returns the difference between the set and another set or sets.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
diff = set1.difference(set2)  # {1, 2}

# set1d.difference_update(*others) removes all elements of another set from this set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)  # {1, 2}

# set1d.discard(element) removes an element from the set if it is a member.
set1d = {1, 2, 3}
set1d.discard(2)  # {1, 3}

# set1d.intersection(*others) returns the intersection of the set with another set or sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection(set2)  # {2, 3}

# set1d.intersection_update(*others) updates the set with the intersection of itself and another set or sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)  # set1 is now {2, 3}

# set1d.isdisjoint(other) returns True if the set has no elements in common with another set.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set1.isdisjoint(set2)  # True

# set1d.issubset(other) returns True if every element of the set is in another set.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
set1.issubset(set2)  # True

# set1d.issuperset(other) returns True if every element of another set is in the set.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
set1.issuperset(set2)  # True

# set1d.pop() removes and returns an arbitrary element from the set.
set1 = {1, 2, 3}
set1.pop()  # e.g., 1

# set1d.remove(element) removes an element from the set. If the element is not a member, it raises a KeyError.
set1 = {1, 2, 3}
set1.remove(2)  # {1, 3}

# set1d.symmetric_difference(other) returns the symmetric difference of the set with another set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference(set2)  # {1, 2, 5, 6}

# set1d.symmetric_difference_update(other) updates the set with the symmetric difference of itself and another set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)  # set1 is now {1, 2, 5, 6}

# set1d.union(*others) returns the union of the set with another set or sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.union(set2)  # {1, 2, 3, 4, 5}

# set1d.update(*others) updates the set with the union of itself and another set or sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)  # set1 is now {1, 2, 3, 4, 5}
```

<br>

[Back to Top](#python-sets)

___

<br>

# `Unpacking Collections`
`Unpacking` refers to the process of extracting individual elements from a container (such as a list, tuple, set, dictionary)
> * Values in a collection can be automatically assigned to variables
> * Use the `*` symbol to unpack multiple values into a single variable
>
> * This used with `*args` and `**kwargs`, see variable length arguments 

<br>

## `Unpacking Into Variables`
```python
set1d = {1,2,3}
a, b, c = set1d

print(a, b, c) #Output: will vary as the values of a, b, and c are assigned in random order

set1d = {1,2,3}
a, b = set1d
# Outputs: ValueError: too many values to unpack (expected 2)
```

<br>
    

## `Unpacking Multiple Values Into One Variable`
```python
# collects multiple values into a single variable
set1d = {"a","b","c","d"}
first, *rest = set1d
# first = varies
# rest = the 3 values first did not recieve

*start, last = set1d
#start = the 3 values last did not recieve
#last = varies

l1 = {1,2,3}
l2 = {4,5,6}
print( {*l1,*l2} )# Output will vary in order: {1,2,3,4,5,6}
```

<br>
    

## `Ignore Unpacked Values` 
Ignore Unpacked Values with `_`


```python
set1d = {1,2,3}
_, b, _ = set1d
#b = varies 
```

<br>

[Back to Top](#python-sets)

___

<br>

# `Set Comprehension`
A `set comprehension` is a shorthand way to algorithmically create a list

syntax:

    {element_expression for variable in iterable}


```python
set1d = {num ** 2 for num in range(5)} 

print(set1d) # Output order varies: {0, 1, 4, 9, 16}
```
```python
import random
set1d = { random.randint(0,100) for _ in range(5)}

print(set1d)
# Output: varies
```

<br>

[Back to Top](#python-sets)

___

<br>
    

# `Set Iteration: Looping`

It is often necessary to go through the contents of a set item by item. This is called `iterating` through a set.

***Sets are unordered and unindexed which means that looping through the values will occur in a random order.***


***Running the code below 5 times could result in a different order each time.***


```python
set1d = {"a","b","c","d","e"}
list1d = []

for elem in set1d:
  list1d.append(elem)
print(list1d)

# 1 ['a', 'c', 'e', 'd', 'b']
# 2 ['a', 'd', 'c', 'b', 'e']
# 3 ['a', 'c', 'e', 'b', 'd']
# 4 ['a', 'c', 'd', 'b', 'e']
# 5 ['b', 'c', 'd', 'e', 'a']
```

___

<br>

[Back to Top](#python-sets)

___

<br>

*Created and maintained by Mr. Merritt*  

    
