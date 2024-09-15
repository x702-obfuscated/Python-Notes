
# `Python Iteration 1D Collections`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Collections Review`](#collections-review)
    1. [`Indexing`](#indexing)
    1. [`Length of a Collection`](#length-of-a-collection)
    1. [`Element Access`](#element-access)
    1. [`Changing an Element`](#changing-an-element)
    1. [`Slicing`](#slicing)
    1. [`Methods to remember`](#methods-to-remember)
1. [`Collection Iteration Syntax`](#collection-iteration-syntax)
    1. [`For Loops List Iteration Syntax`](#for-loops-list-iteration-syntax)
    1. [`While Loops List Iteration Syntax`](#while-loop-list-iteration-syntax)
    1. [`Dictionary Iteration Syntax`](#dictionary-iteration-syntax)
1. [`Forward Iteration: Beginning to End`](#forward-iteration-beginning-to-end)
    1. [`For Loops: Forward Iteration`](#for-loops-forward-iteration)
    1. [`While Loops: Forward Iteration`](#while-loops-forward-iteration)
    1. [`Dictionary Iteration`](#dictionary-iteration)
1. [`Reverse Iteration: End to Beginning`](#reverse-iteration-end-to-beginning)
    1. [`For Loops: Reverse Iteration`](#for-loops-reverse-iteration)
    1. [`While Loops: Reverse Iteration`](#while-loops-reverse-iteration)
1. [`Common Run Time Errors: Lookup Errors`](#common-run-time-errors-lookup-errors)
    1. [`IndexError`](#indexerror)
    1. [`KeyError`](#keyerror)
1. [`Complex Iteration`](#complex-iteration)
1. [`Middle Index Calculation`](#middle-index-calculation)
    1. [`Halves Iteration: Beginning to Middle`](#halves-iteration-beginning-to-middle)
    1. [`Halves Iteration: Middle to Beginning`](#halves-iteration-middle-to-beginning)
    1. [`Halves Iteration: Middle to End`](#halves-iteration-middle-to-end)
    1. [`Halves Iteration: End to Middle`](#halves-iteration-end-to-middle)
1. [`nth Element Iteration`](#nth-element-iteration)




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

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Collections Review`

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

*Note*: 
*`Strings can be iterated through similiarly to lists.`*

___

### *In this file we will focus on lists. Lists cover the widest range of possibilities, and the methods used for lists are identical in most cases to the other collections. Any important differences will be noted.*

___

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>


## `Indexing`
```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] 
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#length aka number of elements = 9 
```
`strings and tuples are identical`
`sets and dictionaries do not have indexes`

<br>

## `Length of a Collection`
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
number_of_elements = len(list1d)    # Returns: 9
last_index = len(list1d)-1          # Returns: 8
```
`tuples and strings are identical`
`sets and dictionaries are not indexed, but len() returns the number of items`


<br>

## `Element Access`
```python
list1d = ["a","b","c"]
list1d[0] # Returns: a
```
```python
dict1d = {"a": 1, "b": 2,"c": 3}

dict1d["a"]      # Returns: 1
dict1d.get("a")  # Returns: 1
```
`strings and tuples are identical to lists`
`individual members of a set cannot be accessed`

<br>

## `Changing an Element`
```python
list1d = ["a","b","c"]
list1d[0] = 1 

# list1d = [1,"b","c"]
```
`dictionaries are similiar, but use keys instead of indexes`  
`individual elements of sets cannot be altered in this way and must be altered with a method`  
`individual elements of a tuple or a string cannot be altered`


<br>

## `Slicing`
```python
#list[start_index:stop_index:step] 
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1d[0:])       # Returns: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(list1d[:3])       # Returns: ['a', 'b', 'c']
print(list1d[0:5])      # Returns: ['a', 'b', 'c', 'd', 'e']
print(list1d[:6:3])
print(list1d[1:6:2])    # Returns: ['b', 'd', 'f']
#note the stop_index is not included in the slice
```
`tuples and strings are identically sliced`
`sets and dictionaries cannot be sliced`


<br>



## `Methods to remember`

### List Methods

```python
list1d.extend(iterable)
```
> *Extends the list by appending all elements from the iterable (e.g., another list).*

<br>


```python
list1d.extend(iterable)
```
> *Extends the list by appending all elements from the iterable (e.g., another list).*

<br>

```python
list1d.insert(index, object)
```
> *Inserts an element object at the given index index.*

<br>

```python
list1d.remove(value)
```
> *Removes the first occurrence of the element value from the list.*

<br>

```python
list1d.pop(index=-1)
```
> *Removes and returns the element at the index index (default is the last element).*

<br>

```python
list1d.clear()
```
> *Removes all elements from the list, making it empty.*

<br>

```python
list1d.index(value, start=0, stop=sys.maxsize)
```
> *Returns the index of the first occurrence of element value in the list from start to stop.*

> *sys.maxsize is very large 2<sup>63</sup>-1: 9,223,372,036,854,775,807*

<br>

```python
list1d.count(value)
```
> *Returns the number of occurrences of element value in the list.*

<br>

```python
list1d.sort(*, key=None, reverse=False)
```
> *Sorts the list in ascending order (can be customized with a key function or reverse=True).*

<br>

```python
list1d.reverse()
```
> *Reverses the elements of the list in place.*

<br>

```python
list1d.copy()
```
> *Returns a shallow copy of the list (a new list with references to the original elements).*

<br>

### Dictionary Methods
```python
dict1d.copy()        
```
> *Returns a shallow copy of the dictionary.*

<br>

```python
dict1d.fromkeys(iterable, value = None)
```
> *Creates a new dictionary with keys from an `iterable` and values set to a specified value.*

<br>

```python
dict1d.pop(key, default)
```
> *Removes the specified `key` and returns the corresponding value. If the `key` is not found remove and return the `default`*

<br>

```python
dict1d.popitem()     
```
> *Removes and returns the last inserted key-value pair as a tuple.*

<br>

```python
dict1d.setdefault(key, default)  
```

> *Returns the value of a `key` if it is in the dictionary; if not, inserts the `key` with a specified value. If `key` is not found return or insert the default.*

<br>

```python
dict1d.clear()
```
> *Removes all items from the dictionary.*


<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Collection Iteration Syntax`
Loops are commonly used to access and operate on the elements of a collection. `for` loops are typically best suited to this type of iteration, however, `while` loops can also be used. 

<br>

*There are many possible operations that might be performed when iterating through a collection. We will keep things simple for now by just printing out the elements.*

<br>

## `For Loops List Iteration Syntax`
`looping through indexes` syntax:
```
for index in range(start, stop, step):
    <Code Block To Execute>
    ...
```
example:
```python
list1d = ["a","b","c","d","e"]

for index in list1d:
    print(list1d[index], end = " ")

# Output: a b c d e 
```

<br> 

`looping through elements` syntax:
```
for element in iterable:
    <Code Block To Execute>
    ...
```
example:
```python
list1d = ["a","b","c","d","e"]

for element in list1d:
    print(element, end = " ")

# Output: a b c d e
```

<br>

The best practice is to use the `enumerate()` function. `enumerate()` has the best of both worlds, offering the index and the element directly.

syntax:
```
for index, element in enumerate(iterable):
    <Code Block To Execute>
    ...
```

example:
```python
list1d = ["a","b","c","d","e"]

for index, element in enumerate(list1d):
    print((index,element), end = " ")

# Output: (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e') 
```

<br>

## `While Loop List Iteration Syntax`
`looping through indexes` syntax:
```
index = 0

while(index < len(iterable)):
    <Code Block To Execute>
    index += 1
```

example:
```python
list1d = ["a","b","c","d","e"]

index = 0
while(index < len(list1d)):
    print(list1d[index], end = " ")
    index += 1

# Output: a b c d e 
```

<br>


## `Dictionary Iteration Syntax`
Dictionaries are unordered, since `key:value` pairs are hashed order doesn't matter, `values` are simply accessed by thier `key`.

syntax:
```
for key in dict1d:
    ...
```
example:
```python
user_data = {
    "name": "Alice",
    "age": 30,
    "city": "Little Rock",
    "phone": "(479) 888 8888"
}

for data in user_data:
    print(data, end = " ")

# Output: name age city phone

for data in user_data:
    print(user_data[data], end = " ")

# Output: Alice 30 Little Rock (479) 888 8888
```

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Forward Iteration: Beginning to End`
`Forward Iteration`: looping from 0 to the length of the list

```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 9 
```

<br>

## `For Loops: Forward Iteration`
```python
'simple and quick plus indexes'

list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(len(list1d)):    # 0 (default) to last index by 1s (default)
    print(index, end =" ")          # printing indexes
    print(list1d[index],end = "|")  # printing elements 

# Output: 0 a|1 b|2 c|3 d|4 e|5 f|6 g|7 h|8 i|
```
```python
'more control with range(start, stop, step)'

list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(0,len(list1d),1):    # 0 to last index by 1s
    print(index, end =" ")              # printing indexes
    print(list1d[index],end = "|")      # printing elements

# Output: 0 a|1 b|2 c|3 d|4 e|5 f|6 g|7 h|8 i|
```
```python
'forward only and elements only'

list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for element in list1d:
    print(element, end = " ")       # printing elements
    #you cannot access indexes this way

# Output: a b c d e f g h i
```
```python
'forward only indexes and elements'
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index, element in enumerate(list1d):
    print(index, end =" ")                  # printing indexes
    print(element, end = "|")               # printing elements
#enumerate returns and enumerate object, basically (index, element)

# Output: 0 a|1 b|2 c|3 d|4 e|5 f|6 g|7 h|8 i|
```

<br>

## `While Loops: Forward Iteration`

```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = 0                               # start at the beginning index
while(index < len(list1d)):
    print(index, end = " ")             # printing indexes
    print(list1d[index], end = "|")     # printing elements
    index += 1                          # increment by 1

# Output: 0 a|1 b|2 c|3 d|4 e|5 f|6 g|7 h|8 i|
```

<br>

## `Dictionary Iteration`
```python
user =  {
    "UID": 1000,
    "username": "script-kitty007",
    "passwd_hash": "0xfb53a168a24ca9dfefa4ae82ed657988",
    "name": "Kat",
    "email": "kat@hackercat.org",
    "birthdate": "5/25/2001"
}

for key in user:
    print((key, user.get(key)), end = " ")

# Output:
# ('UID', 1000) ('username', 'script-kitty007') ('passwd_hash', '0xfb53a168a24ca9dfefa4ae82ed657988') ('name', 'Kat') ('email', 'kat@hackercat.org') ('birthdate', '5/25/2001')
```

<br> 

# `Reverse Iteration: End to Beginning`
`Reverse Iteration`: looping from the last element to the beginning
```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 9 
```

<br>

## `For Loops: Reverse Iteration`
```python
'more control with range(start, stop, step)'

list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(len(list1d)-1,-1,-1):    # start a the last index, stop at 0, decrement by 1
    print(index, end =" ")                  # printing indexes
    print(list1d[index],end = "|")          # printing elements

# Output: 8 i|7 h|6 g|5 f|4 e|3 d|2 c|1 b|0 a|
```

```python
'simpler syntax, but only works for looping through all elements backwards'

list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for element in reversed(list1d):
    print(element, end = " ")       # printing element

# Output: i h g f e d c b a
```

<br>

## `While Loops: Reverse Iteration`
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = len(list1d)-1                   # start at the last index

while(index > -1):                      # stop at 0
    print(index, end = " ")             # printing indexes
    print(list1d[index], end = "|")     # printing elements
    index -= 1                          # decrement by 1


# Output: 8 i|7 h|6 g|5 f|4 e|3 d|2 c|1 b|0 a|
```

*NOTE*:
*`Dictionaries are unordered, since key:value pairs are hashed order doesn't matter, values are simply accessed by their key.`*

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Common Run Time Errors: Lookup Errors`

## `IndexError`
`IndexErrors` are a type of LookUp Error that occurs when an algorithm attempts to access an index that does not exist.


examples
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

print(list1d[10])

# Output:
# Traceback (most recent call last):
#   File "<file_path>", line 3, in <module>
#     print(list1d[10])
#           ~~~~~~^^^^
# IndexError: list index out of range
```
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for i in range(0,10,1):
    print(list1d[i], end = " ")

# Output:
# Traceback (most recent call last):
# a b c d e f g h i Traceback (most recent call last):
#   File "<file_path>", line 3, in <module>
#     print(list1d[i], end = " ")
#           ~~~~~~^^^
# IndexError: list index out of range
```
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

i = 0
while (i <= 10):
    print(list1d[i], end = " ")
    i += 1

# Output:
# Traceback (most recent call last):
# a b c d e f g h i Traceback (most recent call last):
#   File "<file_path>", line 5, in <module>
#     print(list1d[i], end = " ")
#           ~~~~~~^^^
# IndexError: list index out of range
```

<br>

## `KeyError` 
`KeyErrors` are a type of lookup error that occurs when attempting to access a dictionary key that does not exist.


examples:
```python
dict1d = {"a": 97, "b":98,"c":99}

print(dict1d["d"])

# Output:
# Traceback (most recent call last):
#   File "<file_path>", line 3, in <module>
#     print(dict1d["d"])
#           ~~~~~~^^^^^
# KeyError: 'd'
```

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Complex Iteration`
Complex Iteration involves more complex algorithms for example
* Looping through the first or last half of the list
* Looping through every nth element
* etc.

<br>

# `Middle Index Calculation` 
Calculating the middle index of a list is necessary, in order to loop through half of the list.

<br>

## `Even Length Lists`

```python
#        [-----------------elements-------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
#index   [ 0    1    2    3    4    5    6    7 ]
#reverse [-8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 8
```

*Is the middle index 3 or 4?*
> 4 will work the best in many situations, but it is important that you the programmer decide how your algorithm will work.

```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
mid_index = len(list1d)/2 # Returns: 4
```
`len(list1d)/2` will work for even length lists, but not for odd length ones. We need a universal way.

<br>

## `Odd Length Lists`
```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] 
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 9 
```
Using simple division below `len(list1d)/2` returns 4.5 but floats cannot be used as indexes.
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
mid_index = len(list1d)/2 # Returns: 4.5 <-- Floats cannot be indexes
```
The solution is to use Floor division, or Cast to <class 'int'>
### `Floor division`
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
mid_index = len(list1d)//2 # Returns: 4
```

### `Casting to <class 'int'>` 
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
mid_index = int(len(list1d)/2) # Returns: 4
```
In odd length lists this calculation results in the second half being 1 element more than the first half  
*`The two methods above work for both even and odd length lists`*

<br>

## `Method for both`
syntax for calculating the middle index:
```python
list1d = ...

mid_index = len(list1d)//2
```
*`The method above can be consitently used to determine the middle of a list, tuple, string, etc.`*

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Halves Iteration: Beginning to Middle` 

## For Loop: Beginning to Middle
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(0, len(list1d)//2, 1):       # start at beginning, stop at the middle, increment by 1 
    print(index, end = " ")                     # printing indexes
    print(list1d[index],end = "|")              # printing elements

# Output: 0 a|1 b|2 c|3 d|
```

## While Loop: Beginning to Middle
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = 0                               # start at 0
while(index < len(list1d)//2):          # stop at the middle
    print(index, end = " ")             # print indexes
    print(list1d[index], end = "|")     # print elements    
    index += 1                          # increment by 1

# Output: 0 a|1 b|2 c|3 d| 
```

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `Halves Iteration: Middle to Beginning `
## For Loop: Middle to Beginning
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(len(list1d)//2 -1, -1, -1):  # start at middle, stop at the 0, decrement by 1 
    print(index, end =" ")                      # printing indexes
    print(list1d[index],end = "|")              # printing elements

# Output: 3 d|2 c|1 b|0 a|
```

## While Loop: Middle to Beginning
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = len(list1d)//2 -1               # start at the middle
while(index > -1):                      # stop at 0
    print(index, end = " ")             # print indexes
    print(list1d[index], end = "|")     # print elements
    index -= 1                          # decrement by 1

# Output: 3 d|2 c|1 b|0 a|
```

<br>

# `Halves Iteration: Middle to End `
## For Loop: Middle to End
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(len(list1d)//2, len(list1d), 1):     # start at middle, stop at the end, increment by 1 
    print(index, end =" ")                              # printing indexes
    print(list1d[index],end = "|")                      # printing elements

# Output: 4 e|5 f|6 g|7 h|8 i|
```

## While Loop: Middle to End
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = len(list1d)//2                  # start at the middle
while(index < len(list1d)):             # stop at the end
    print(index, end = " ")             # print indexes
    print(list1d[index], end = "|")     # print elements
    index += 1                          # increment by 1

# Output: 4 e|5 f|6 g|7 h|8 i|
```

<br>

# `Halves Iteration: End to Middle` 
## For Loop: End to Middle
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

for index in range(len(list1d) -1, len(list1d)//2 -1, -1):      # start at the end, stop at the middle, decrement by 1 
    print(index, end =" ")                                      # printing indexes
    print(list1d[index],end = "|")                              # printing elements

# Output: 8 i|7 h|6 g|5 f|4 e|
```

## While Loop: End to Middle
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = len(list1d) -1                  # start at the end
while(index > len(list1d)//2 -1):       # stop at the middle
    print(index, end = " ")             # print indexes
    print(list1d[index], end = "|")     # print elements
    index -= 1                          # decrement by 1

# Output: 8 i|7 h|6 g|5 f|4 e|
```

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

# `nth Element Iteration`
`nth` element refers to iterating at a different increment than 1, where n represents any integer.

## For Loop: nth Element
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

n = 2                                       # pick any number to for n

for index in range(0, len(list1d), n):      # start at 0, stop at the end, increment by n
    print(index, end =" ")                  # printing indexes
    print(list1d[index],end = "|")          # printing elements

# Output: 0 a|2 c|4 e|6 g|8 i|
```

## While Loop: nth Element
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

n = 2                                   # pick any number to for n
index = len(list1d) -1                  # start at the end
while(index > len(list1d)//2 -1):       # stop at the middle
    print(index, end = " ")             # print indexes
    print(list1d[index], end = "|")     # print elements
    index -= n                          # increment by n

# Output: 0 a|2 c|4 e|6 g|8 i|
```

<br>

[Back to Top](#python-iteration-1d-collections)

___

<br>

*Created and maintained by Mr. Merritt*
