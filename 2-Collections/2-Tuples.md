# `Python Tuples`
___

Covered in this file:
1. [`Collection Types`](#collection-types)
1. [`Defining a Tuple`](#defining-a-tuple)
1. [`Creating a Tuple`](#creating-a-tuple)
1. [`Converting from Lists and Sets`](#converting-from-lists-and-sets)
1. [`Tuple Operations`](#tuple-operations)
    1. [`Checking Tuple Membership`](#checking-tuple-membership)
    1. [`Concatenating Tuples (joining)`](#concatenating-tuples-joining)
    1. [`Concatenate and Assign Tuple`](#concatenate-and-assign-tuple)
    1. [`Duplicate Tuples`](#duplicate-tuples)
    1. [`Duplicate and Assign Tuples`](#duplicate-and-assign-tuples)
1. [`Accessing Elements in a Tuple`](#accessing-elements-in-a-tuple)
1. [`Tuple Elements Cannot be Changed`](#tuple-elements-cannot-be-changed)
1. [`Built-in Tuple Function Calls`](#built-in-tuple-function-calls)
1. [`Built-in Tuple Method Calls`](#built-in-tuple-method-calls)
1. [`Subtuples: Slicing and Concatenation`](#subtuples-slicing-and-concatenation)
1. [`Tuples of Tuples: Nested Tuples`](#tuples-of-tuples-nested-tuples)
1. [`Unpacking Collections`](#unpacking-collections)
1. [`Tuple Iteration: Looping`](#tuple-iteration-looping)

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


[Back to Top](#python-tuples)

___

<br>


# `Defining a Tuple`

Basically: `Tuples` are lists that cannot be changed

Specifically: `Tuples` are collections which are ordered(indexed), immutable, allow duplicate members and uses ( ) to enclose members.

Tuple Example:
```python
("a","b","c","d","e") #a tuple

#add a newline after a comma to make the tuple more readable
('a', 'b', 'c', 'd', 'e', 
 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 
 'z'
)

# Other examples:
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

bools  = (True, False)

numerals = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

lcase_alpha = (
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
)

ucase_alpha = (
    'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z'
)

```

A `tuple` contains multiple items called `elements` or `members`
|elements|"a"|"b"|"c"|"d"|"e"|
|:-:|:-:|:-:|:-:|:-:|:-:|
|indexes|0|1|2|3|4|
|Length|||||5|

> - An `index` indicates the spot at which an `element` is located.   
> - `Indexes` can be used to access each `element` in the list.   
> - The length of a tuple is the total number of elements contained in the list  

```python
#        (------------------elements---------------------)
tuple1d = ("a","b","c","d","e","f","g","h","i","j","k","l")
#index    ( 0   1   2   3   4   5   6   7   8   9   10  11)
#reverse  (-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1)
#Length = 12
```

<br>


[Back to Top](#python-tuples)

___

<br>

# `Creating a Tuple`
Use `()` to denote a tuple
> * seperate elements of a tuple with commas
> * The `tuple(iterable)` constructor builds a tuple

Create an empty tuple with `()`
```python
() # creates an empty tuple

tuple1d = ()
```

Create a tuple with a single value using a trailing `,`
```python
tuple1d = ("a",)
#OR
tuple1d = "a", 
```

Enclose comma seperated elements with `()`
```python
#use () and seperate each element with commas
tuple1d = (1,2,3,4,5,6,7,8,9)
#index     0 1 2 3 4 5 6 7 8
#length = 9
```

Use the `tuple(iterable)` constructor call

syntax:

    tuple(iterable)


```python
#use the tuple(iterable) constructor call
tuple() # Returns: ()
tuple('abcdef') # Returns('a', 'b', 'c', 'd', 'e', 'f')
```

<br> 

[Back to Top](#python-tuples)

___

<br>

# `Converting from Lists and Sets`
* The `list(iterable)` constructor builds a list
* The `tuple(iterable)` constructor builds a tuple
* The `set(iterable)` constructor builds a set

<br>

Constructors are special methods defined by a class that are used to build instances of a class. 
> * ie. the `tuple(iterable)` constructor makes a tuple.


```python
tuple("abcdef") #Returns: ('a', 'b', 'c', 'd', 'e', 'f')
```


```python
set1d = {"dog","cat","horse"}

tuple(set1d) # Returns: ('cat', 'dog', 'horse')
```


```python
tuple1d = (1,2,3,4,5)

# From tuple to list using list(iterable))
list1d = list(tuple1d) # Returns: [1,2,3,4,5]

#From tuple to set use set(iterable)
set1d = set(tuple1d) # Returns: {1,2,3,4,5}
```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Tuple Operations`
|Operation| Description|
|:-:|:-:|
|`in`| checks if a value is a member|
|`not in`| checks if a value is not a member|
|`+`|concatenates two tuples|
|`+=`|concatenates and assigns (must be another tuple)|
|`*`| duplicates a tuple|
|`*=`|duplicates and assigns |

<br>

## `Checking Tuple Membership`
Use `in` to check if a value is apart of a tuple

syntax:

    value in tuple


```python
numbers = (1,2,3,4,5)

3 in numbers # Returns: True
6 in numbers # Returns: False
```

Use `not in` to check if a value is not apart of a tuple. 

syntax:

    value not in tuple


```python
numerals = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

"10" not in numerals # Returns: True
"4"  not in numerals # Returns: False
```

<br>

## `Concatenating Tuples (joining)`
Use `+` to concatenate tuples.

syntax:

    tuple1 + tuple2


```python
animals = ("dog", "cat", "cow", "horse")
plants = ("tree","grass", "shrub", "moss")

living_things = animals + plants

print(living_things)
# Output:
# ('dog', 'cat', 'cow', 'horse', 'tree', 'grass', 'shrub', 'moss')
```

<br>

## `Concatenate and Assign Tuple`
Use `+=` to concatenate and assign tuples.
> * only works with two or more tuples

syntax:

    tuple1 += tuple2


```python
prime_numbers = (2, 3, 5, 7, 11)
more_primes = (13, 17, 19, 23, 29)

prime_numbers += more_primes

print(prime_numbers)
# Output:
# (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
```

<br>

## `Duplicate Tuples`
Use `*` to duplicate tuples.

syntax:

    tuple1 * n

> *n is the number of times to duplicate the tuple*


```python
pattern = (1,0,0,1)

pattern * 4 
# Returns: (1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1)
```

<br>

## `Duplicate and Assign Tuples`
Use `*=` to duplicate and assign tuples. 

syntax:

    tuple1 *= n

> *n is the number of times to duplicate the tuple*


```python
b =(1,0)
b *= 5
print(b) # Output: (1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Accessing Elements in a Tuple`
To access the data in a tuple using the `index` an subscripting `[]`
syntax:

    tuple[index]

`tuple1d = ("w","x","y","z")`
|elements |"w"|"x"|"y"|"z"|
|:-:|:-:|:-:|:-:|:-:|
|index|0|1|2|3|
|reverse/negative index|-4|-3|-2|-1|

`elements in a tuple are accessed by their index`


```python
#         (---elements----)
tuple1d = ("w","x","y","z")
# index   ( 0   1   2   3 )
# reverse (-4  -3  -2  -1 )
#             Length = 4
```

<br>

`Regular Indexing`


```python
tuple1d = ("a","b","c","d","e","f","g","h","i","j","k","l")

tuple1d[0]   # Returns: a
tuple1d[5]   # Returns: f
tuple1d[10]  # Returns: k
```

<br>

`Reverse/Negative Indexing`


```python
tuple1d = ("a","b","c","d","e","f","g","h","i","j","k","l")

tuple1d[-1]  # Returns: l
tuple1d[-5]  # Returns: h
tuple1d[-10] # Returns: c
```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Tuple Elements Cannot be Changed`
`Elements` (data) in a list cannot be changed in a tuple.
> Tuples are `immutable`, meaning that the data that it stores cannot be changed. In order to change a tuple a new tuple must be created.

<br>

[Back to Top](#python-tuples)

___

<br>

# `Built-in Tuple Function Calls`
___
`Functions` are blocks of reusable code, that perform a specific task.
> * must be defined before they are called
> * are typically called using their name followed by parenthesis with any required arguments inside.


`Built-in Functions are pre-defined by the Python standard library`


```python
#         (------------------elements---------------------)
tuple1d = ("a","b","c","d","e","f","g","h","i","j","k","l")
# index   ( 0   1   2   3   4   5   6   7   8   9   10  11)
# reverse (-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1)
# length = 12

#len()
len(tuple1d)   #returns number of elements in a tuple
len(tuple1d)-1 #returns the last index of the 

#max()
max(tuple1d) #Returns the largest element in the tuple.

#min()
min(tuple1d)#Returns the smallest element in the tuple.

#sum(tuple1d)
nums = (1,2,3,4,5)
sum(nums) #Returns the sum of all elements in a number tuple.

#sorted(iterable)
sorted(tuple1d) #returns a sorted list of the specified iterable

```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Built-in Tuple Method Calls`
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
#.index(x, start, end)
tuple1d.index("elem")# Returns the index of the first occurrence of element x 
tuple1d.index("elem",2,5) #(optional start and end indices can be specified).

#.count(x)
tuple1d.count("elem")# Returns the number of occurrences of element x in the tuple.
```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Subtuples: Slicing and Concatenation`
`Slicing` is the creation of a subtuple, by returning parts of an original tuple.
> * use slicing notation `[ : : ]` to return a subtuple

slicing syntax:
    
    tuple[start_index:stop_index:step]


> * start_index is inclusive (the character at start_index will appear in the sublist)
> * stop_index is exclusive (the character at the stop_index will NOT appear in the sublist)


Be sure to pick the right stop_index
> * for ascending ( + step ) subtuple add one to the last index you want to include (stop + 1)  
> * for descending ( - step ) subtuple subtract one from the last index you want to include (stop - 1)

examples:


```python
tuple1d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

# Ascending
tuple1d[1:6:2] # Returns: ('b', 'd', 'f')
tuple1d[0:9:3] # Returns: ('a', 'd', 'g')
tuple1d[2:8:3] # Returns: ('c', 'f')
tuple1d[1:7:1] # Returns: ('b', 'c', 'd', 'e', 'f', 'g')

# Descending
tuple1d[4:1:-1]    # Returns: ('e', 'd', 'c')
tuple1d[-1:-5:-1]  # Returns: ('i', 'h', 'g', 'f')
tuple1d[7:0:-1]    # Returns: ('h', 'g', 'f', 'e', 'd', 'c', 'b')
tuple1d[8:0:-2]    # Returns: ('i', 'g', 'e', 'c')
```

<br>

## `Ascending Slices`
> * Default start_index is 0
> * Default stop_index is len(tuple) (end of the tuple)
> * Default step is 1
> * The slice includes the start_index, but excludes the stop_index


```python
tuple1d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

#If a start_index is not provided the default is 0
tuple1d[:3:1] # Returns: ('a', 'b', 'c')
tuple1d[:6:3] # Returns: ('a', 'd')

#If a stop_index is not provided the default is len(list)
tuple1d[0:]   # Returns:  ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')
tuple1d[5:]   # Returns:  ('f', 'g', 'h', 'i')
tuple1d[::2]  # Returns:  ('a', 'c', 'e', 'g', 'i')

# If the step is not specified the default is 1 
tuple1d[0:5] # Returns: ('a', 'b', 'c', 'd', 'e')
tuple1d[:3]  # Returns: ('a', 'b', 'c')
tuple1d[6::] # Returns: ('g', 'h', 'i')
```

<br>

## `Descending Slices`
> * Default start_index is len(list) (end of the list)
> * Default stop_index is the beginning of the list
>   * In order to include the character at index 0 you must use the default stop_index 
> * Must specify a negative step
> * The slice includes the start_index, but excludes the stop_index


```python
tuple1d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

#If a start_index is not provided the default is len(list)
tuple1d[:4:-1]     # Returns: ('i', 'h', 'g', 'f')
tuple1d[:-6:-1]    # Returns: ('i', 'h', 'g', 'f', 'e')
tuple1d[::-1]      # Returns: ('i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')

#If a stop_index is not provided the default is len(list)
tuple1d[5::-1]     # Returns: ('f', 'e', 'd', 'c', 'b', 'a')
tuple1d[-3::-1]    # Returns: ('g', 'f', 'e', 'd', 'c', 'b', 'a')
tuple1d[::-3]      # Returns: ('i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')
```

<br>

[Back to Top](#python-tuples)
___

<br>

# `Tuples of Tuples: Nested Tuples`
A `Nested tuple` or `Multidimensional tuple` is a tuple that contains other tuples (a tuple of tuples).  
> * called a nested tuple or multidimensional tuple  
> * each tuple is accessed with its index and subscripting
>
> * each element of the tuples are access with 2 indexes and subscripting [][] 
>   * the first index is the tuple index, the second is the element index 




```python
#index    ((---------tuple 0-------),(--------tuple 1--------),(--------tuple 2--------),(--------tuple 3--------))
#reverse  ((---------tuple -4------),(--------tuple-3--------),(--------tuple -2-------),(--------tuple -1-------))
tuple2d = (("a","b","c","d","e","f"),("g","h","i","j","k","l"),("m","n","o","p","q","r"),("s","t","u","v","w","x"))
#index    (( 0   1   2   3   4   5 ),( 0   1   2   3   4   5 ),( 0   1   2   3   4   5 ),( 0   1   2   3   4   5 ))
#reverse  ((-6  -5  -4  -3  -2  -1 ),(-6  -5  -4  -3  -2  -1 ),(-6  -5  -4  -3  -2  -1 ),(-6  -5  -4  -3  -2  -1 ))               
```

Formatting the 2D tuples in our code can make them easier to read.  
> A 2D tuple can then be thought of as `rows`, and `columns`.


```python
#simplify by formatting the code this way 
tuple2d = (
  ("a","b","c","d","e","f"), #tuple 0 
  ("g","h","i","j","k","l"), #tuple 1 
  ("m","n","o","p","q","r"), #tuple 2 
  ("s","t","u","v","w","x")  #tuple 3 
)


#simplify in our mind as rows and columns 
tuple2d = (
  ("a","b","c","d","e","f"), # 0
  ("g","h","i","j","k","l"), # 1 row 
  ("m","n","o","p","q","r"), # 2   indexes
  ("s","t","u","v","w","x")  # 3
  # 0   1   2   3   4   5
) #    column indexes
```

<br>

## `Accessing Elements from a 2D List`
syntax:
    
    2DTuple[tuple_index][element_index]

    OR

    2DTuple[row][col]


```python
tuple2d = (
  ("a","b","c","d","e","f"), # 0
  ("g","h","i","j","k","l"), # 1 row 
  ("m","n","o","p","q","r"), # 2   indexes
  ("s","t","u","v","w","x")  # 3
  # 0   1   2   3   4   5
) #    column indexes

tuple2d[0][0] # Returns: a
tuple2d[0][1] # Returns: b
tuple2d[3][5] # Returns: x

```

<br>

## `Length of 2D Tuples`
The `len()` function call returns the number of elements in the tuple
> * `len(tuple2d)` returns the number of rows/tuples
> * `len(tuple2d[row])` returns the number of columns/elements in a given row/tuple

> * `len(tuple2d)-1` returns the last row index
> * `len(tuple2d[row])-1` returns the last column index in a given row/tuple


```python
tuple2d = (
  ("a","b","c","d","e","f"), # 0
  ("g","h","i","j","k","l"), # 1 row 
  ("m","n","o","p","q","r"), # 2   indexes
  ("s","t","u","v","w","x")  # 3
  # 0   1   2   3   4   5
) #    column indexes

#len()function call returns the number of elements in the tuple
len(tuple2d)   # 4 (number of rows/tuples)
len(tuple2d)-1 # 3 (last row index)


row = 0 #represents the row, in this case the row at index 0 
len(tuple2d[row])   # 6 number of columns/elements in a given row/tuple
len(tuple2d[row])-1 # 5 last column index 
```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Unpacking Collections`
`Unpacking` refers to the process of extracting individual elements from a container (such as a list, tuple, dictionary)
> * Values in a collection can be automatically assigned to variables
> * Use the `*` symbol to unpack multiple values into a single variable
>
> * This used with `*args` and `**kwargs`, see variable length arguments 

<br>

## `Unpacking Into Variables`
```python
tuple1d = (1,2,3)
a, b, c = tuple1d
# a = 1
# b = 2
# c = 3

tuple1d = (1,2,3)
a, b = tuple1d
# Outputs: ValueError: too many values to unpack (expected 2)
```

<br>

## `Unpacking Mutliple Values Into One Variable`

```python
# collects multiple values into a single variable
tuple1d = ("a","b","c","d")
first, *rest = tuple1d
# first = a
# rest = (b,c,d)

*start, last = tuple1d
#start = (a,b,c)
#last = d

l1 = (1,2,3)
l2 = (4,5,6)
print( (*l1,*l2) )# Output: (1,2,3,4,5,6)
```

<br>

## `Ignore Unpacked Values` 
Ignore Unpacked Values with `_`


```python
tuple1d = (1,2,3)
_, b, _ = tuple1d
#b = 2
```

<br>

[Back to Top](#python-tuples)

___

<br>

# `Tuple Iteration: Looping`
It is often necessary to go through the contents of a tuple item by item. This is called `iterating` through a tuple.

There are several ways to iterate through a tuple.

We will use this tuple of alphanumeric characters generated using tuple comprehensions as an example tuple to iterate through.


```python
alphanumeric = (
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
    'y', 'z'
)

```

<br>

## `Looping through the indexes of a tuple`
syntax:

    for index in range(len(tuple)):
        ...


```python
alphanumeric = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#for index in range(len(tuple)):
for i in range(len(alphanumeric)):
  print(i) #prints each index of alphanumeric
# Outputs: 
# 0
# 1
# 2
# 3
# ...
# 61
```

<br>

## `Looping through the elements of a tuple`
syntax:

    for element in tuple:
        ...


```python
alphanumeric = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

# for element in tuple:
for char in alphanumeric:
    print(char) #prints each element of alphanumberic

# Output:
# 0
# 1
# 2
# ...
# z
```

<br>

## `Looping through the elements backwards`
syntax:

    for element in reversed(tuple):
        ...


```python
alphanumeric = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#for element in reversed(list):
for elem in reversed(alphanumeric):
  print(elem)
#prints each element of the reversed list
# Output:
# z
# y 
# x
# ...
# 0
```

<br>

## `Looping through the index and elements at the same time`

syntax:

    for index, element in enumerate(tuple):
        ...


```python
alphanumeric = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

#for index, element in enumerate(tuple):
for index,element in enumerate(alphanumeric):
  alphanumeric[index] = (index, element)

print(alphanumeric)
# Output: 
# [(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), 
#  (10, 'A'), (11, 'B'), (12, 'C'), (13, 'D'), (14, 'E'), (15, 'F'), (16, 'G'), (17, 'H'), (18, 'I'), (19, 'J'), 
#  (20, 'K'), (21, 'L'), (22, 'M'), (23, 'N'), (24, 'O'), (25, 'P'), (26, 'Q'), (27, 'R'), (28, 'S'), (29, 'T'), 
#  (30, 'U'), (31, 'V'), (32, 'W'), (33, 'X'), (34, 'Y'), (35, 'Z'), (36, 'a'), (37, 'b'), (38, 'c'), (39, 'd'), 
#  (40, 'e'), (41, 'f'), (42, 'g'), (43, 'h'), (44, 'i'), (45, 'j'), (46, 'k'), (47, 'l'), (48, 'm'), (49, 'n'), 
#  (50, 'o'), (51, 'p'), (52, 'q'), (53, 'r'), (54, 's'), (55, 't'), (56, 'u'), (57, 'v'), (58, 'w'), (59, 'x'), 
#  (60, 'y'), (61, 'z')]
```

___

<br>

[Back to Top](#python-tuples)

___

<br>

*Created and maintained by Mr. Merritt*  
