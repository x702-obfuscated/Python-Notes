*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
# <table><th>`Iterating Through 1D Collections`<th></table>
___

Covered in this file:
1. Collections Review
2. Collection Iteration Syntax
3. Forward Iteration: Beginning to End
4. Reverse Iteration: End to Beginning
5. Run Time Errors: LookUp Errors
6. Complex Iteration 
>> 0. Middle Index Calculation 
>> 1. Halves Iteration: Beginning to Middle  
>> 2. Halves Iteration: Middle to Beginning  
>> 3. Halves Iteration: Middle to End  
>> 4. Halves Iteration: End to Middle 
>> 5. nth Element Iteration

<br>

## Note on symbols used in this file:
> Symbols appearing in python blocks should be treated as Python syntax.  
>... is used a placeholder in Python. 
```python 
... 
```

### Variable Information
> Text inside of <> should be treated as a place holder for variable information
```
  <text>    
```

### CLI Commands
> The > indicates commands to be executed in the Windows Powershell prompt
```
  > command flags arguments 
```
> The $ indicates commands to be executed in the Linux or Mac command line interface
```
  $ command flags arguments
```

<br>

## <table><th>`Collections Review`</th></table>

There are four major collection data types in the Python programming language:

> **List:**   
collection which is ordered(indexed), mutable, allows duplicate members, and uses [ ] to enclose members.
```python
list1d = [1,2,3]
```

> **Tuple:**  
collection which is ordered(indexed), immutable, allows duplicate members and uses ( ) to enclose members.
```python
tuple1d = (1,2,3)
```
> **Set:**   
collection which is unordered(not indexed), mutable, does NOT allow duplicate members and uses { } to enclose members.
```python
set1d = {1,2,3}
```
> **Dictionary:**   
collection which is ordered(indexed with a key), mutable, does NOT allow duplicate members and uses { : } to enclose members.
```python
dict1d = {"a": 1, "b": 2,"c": 3}
```
|**List**|**Tuple**|**Set**|**Dictionary**|
|:-:|:-:|:-:|:-:|
|ordered (numerically indexed)|ordered (numerically indexed)|unordered (not indexed)|ordered (indexed with a key)|
|mutable|immutable|mutable|mutable|
|duplicates|duplicates|NO duplicates|NO duplicates|
|**[ ]**|**( )**|**{ }**|**{ : }**| 

> * *Data Structure: a specialized format for organizing, processing, retrieving, and storing data.*
> * *Collection: a data structure that holds multiple elements*
> * *Member: an item stored within a collection*
> * *Element: is a synonym for member*
> * *Ordered: having a specific order 0,1,2,... (ie. indexed)*
> * *Indexed:  elements are associated with a specific identifier (index), which can be used to directly locate and access the data*
> * *Mutable: elements can change*
> * *Immutable: elements cannot change*

> # Note: 
> Strings can be iterated through similiarly to lists.  
> From here we will focus on lists, as lists cover the widest range of possibilities, and the methods used for lists are identical in most cases to the other collections. 

> Import differences will be noted.

<br>

## Indexing
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

## Length of a Collection
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
number_of_elements = len(list1d)    # Returns: 9
last_index = len(list1d)-1          # Returns: 8
```
`tuples and strings are identical`
`sets and dictionaries are not indexed, but len() returns the number of items`


<br>

## Element Access
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

## Changing an Element
```python
list1d = ["a","b","c"]
list1d[0] = 1 

# list1d = [1,"b","c"]
```
`dictionaries are identical, but use keys instead of indexes`  
`individual elements of sets cannot be altered in this way and must be altered with a method`  
`individual elements of a tuple or a string cannot be altered`


<br>

## Slicing
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



## Methods to remember
```python
list1d.append()  # Adds a single element x to the end of the list.
list1d.extend()  # Extends the list by appending elements from the iterable.
list1d.insert()  # Inserts an element x at a given index i.
list1d.remove()  # Removes the first occurrence of element x from the list.
list1d.pop()     # Removes the element at the given index i and returns it. default is the last element
list1d.clear()   # Removes all elements from the list.
list1d.index()   # Returns the index of the first occurrence of element x 
list1d.count()   # Returns the number of occurrences of element x in the list.
list1d.sort()    # Sorts the list in ascending order. 
list1d.reverse() # Reverses the elements of the list in place.
list1d.copy()    # Returns a shallow copy (reference location) of the list.
```

```python
dict1d.copy()        # Returns a shallow copy of the dictionary.
dict1d.fromkeys()    # Creates a new dictionary with keys from an iterable and values set to a specified value.
dict1d.pop()         # Removes the specified key and returns the corresponding value.
dict1d.popitem()     # Removes and returns the last inserted key-value pair as a tuple.
dict1d.setdefault()  # Returns the value of a key if it is in the dictionary; if not, inserts the key with a specified value.
dict1d.clear()       # Removes all items from the dictionary.
```
<br>

## <table><th>`Collection Iteration Syntax`</th></table>
> * Loops are commonly used to access and operate on the elements of a collection
> * for loops are typically best suited to this type of iteration
> * However, while loops can also be used. 

> There are many possible operations that might be performed when iterating through a collection.  
> We will keep things simple for now by just printing out the elements. 


<br>

## For Loops List Iteration Syntax:
syntax:
```
for index in range(start, stop, step):
    <Code Block To Execute>
    ...
```
real example:
```python
list1d = ["a","b","c","d","e"]

for index in list1d:
    print(list1d[index], end = " ")

# Output: a b c d e 
```
syntax:
```
for element in iterable:
    <Code Block To Execute>
    ...
```
real example:
```python
list1d = ["a","b","c","d","e"]

for element in list1d:
    print(element, end = " ")

# Output: a b c d e
```

<br>

### This syntax is considered best practice.
> * it has the best of both worlds, offering the index and the element directly.

syntax:
```
for index, element in enumerate(iterable):
    <Code Block To Execute>
    ...
```

real example:
```python
list1d = ["a","b","c","d","e"]

for index, element in enumerate(list1d):
    print((index,element), end = " ")

# Output: (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e') 
```

<br>

## While Loop List Iteration Syntax:
syntax:
```
index = 0

while(index < len(iterable)):
    <Code Block To Execute>
    index += 1
```

real example:
```python
list1d = ["a","b","c","d","e"]

index = 0
while(index < len(list1d)):
    print(list1d[index], end = " ")
    index += 1

# Output: a b c d e 
```


## Dictionary Iteration
> Dictionaries are unordered, since key:value pairs are hashed order doesn't matter, values are simply accessed by thier key.

syntax:
```
for key in dict1d:
    ...
```

<br>

## <table><th>`Forward Iteration: Beginning to End`</th></table>
> * Forward Iteration: looping from 0 to the length of the list

```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 9 
```

## For Loops: Forward Iteration
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

## While Loops: Forward Iteration

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

## Dictionary Iteration
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

## <table><th>`Reverse Iteration: End to Beginning`</th></table>
> * Reverse Iteration: looping from the last element to the beginning
```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 9 
```

## For Loops: Reverse Iteration
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

## While Loops: Reverse Iteration
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

index = len(list1d)-1                   # start at the last index

while(index > -1):                      # stop at 0
    print(index, end = " ")             # printing indexes
    print(list1d[index], end = "|")     # printing elements
    index -= 1                          # decrement by 1


# Output: 8 i|7 h|6 g|5 f|4 e|3 d|2 c|1 b|0 a|
```

NOTE:
> Dictionaries are unordered, since key:value pairs are hashed order doesn't matter, values are simply accessed by thier key.

<br>

## <table><th>`Run Time Errors: LookUp Errors`</th></table>

## IndexError
> * IndexErrors are a type of LookUp Error that occurs when an algorithm attempts to access an index that does not exist.
> * error: Run Time

real examples
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

## KeyError: 
> * KeyErrors are a type of lookup error that occurs when attempting to access a dictionary key that does not exist.
> * error: Run Time

real examples:
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

## <table><th>`Complex Iteration`</th></table> 
> * Complex Iteration involves more complex algorithms for example
    > * Looping through the first or last half of the list
    > * Looping through every nth element
    > * etc.

## <table><th>`Middle Index Calculation`</th></table> 
> * Calculating the middle index of a list is necessary, in order to loop through half of the list.

<br>

## Even Length Lists

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
> This will work for even length lists, but not for odd length ones. We need a universal way.

<br>

## Odd Length Lists
```python
#        [-----------------elements------------------]
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'] 
#index   [ 0    1    2    3    4    5    6    7    8 ]
#reverse [-9   -8   -7   -6   -5   -4   -3   -2   -1 ]
#len(list1d) aka number of elements = 9 
```
> Using simple division, this returns 4.5 but floats cannot be used as indexes.
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
mid_index = len(list1d)/2 # Returns: 4.5 <-- Floats cannot be indexes
```
> Solution, use Floor division, or Cast to <class 'int'>
### Floor division
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
mid_index = len(list1d)//2 # Returns: 4
```

### Casting to <class 'int'> 
```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
mid_index = int(len(list1d)/2) # Returns: 4
```
> In odd length lists this calculation results in the second half being 1 element more than the first half  
> **The two methods above work for both even and odd length lists**

## Method for both
syntax for calculating the middle index:
```python
list1d = ...

mid_index = len(list1d)//2
```

<br>

## <table><th>`Halves Iteration: Beginning to Middle`</th></table> 

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

## <table><th>`Halves Iteration: Middle to Beginning `</th></table> 
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

## <table><th>`Halves Iteration: Middle to End `</th></table>
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

## <table><th>`Halves Iteration: End to Middle`</th></table> 
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

## <table><th>`nth Element Iteration`</th></table> 
> * nth element refers to iterating at a different increment than 1, where n represents any integer.

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
