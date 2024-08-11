*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
# <table><th>`Iterating Through 2D Collections`<th></table>
___

Covered in this file:
1. Multidimension Collections Review
2. Mutidimension Collection Iteration Syntax
3. Forward Iteration: Beginning to End
4. Reverse Iteration: End to Beginning
5. Complex Iteration

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

## <table><th>`Multidimension Collections Review`</th></table>

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
> From here we will focus on lists, as lists cover the widest range of possibilities, and the methods used for lists are identical in most cases to the other collections. 

> Important differences will be noted.

<br>

## Indexing
```python
#a 2D list is a list of lists
#        [------------------------------------------outer elements-----------------------------------------------]
#index   [[---------list 0--------],[--------list 1---------],[--------list 2---------],[--------list 3---------]]
#reverse [[---------list -4-------],[--------list-3---------],[--------list -2--------],[--------list -1--------]]
list2d = [["a","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"]]
#index   [[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ]]
#reverse [[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ]]
#        [[-----inner elements----],[-----inner elements----],[-----inner elements----],[-----inner elements----]]
#                
# list2d is a list of 4 lists
```
> * To simplify how we look at multi dimensional lists and tuples
```python
#simplify by formatting the code this way 
list2d = [
  ["a","b","c","d","e","f"], #list 0
  ["g","h","i","j","k","l"], #list 1
  ["m","n","o","p","q","r"], #list 2
  ["s","t","u","v","w","x"]  #list 3
]


#simplify in our mind as rows and columns 
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes
```

`tuples are identical`
`sets cannot be multidimensional as they can only contain immutable types`

`Nested Dictionaries use keys instead of indexes`  

real example:
> There are two user_info keys: jack_the_giant_slayer and jill_up_the_hill.  
> Each contains thier own nested dictionary with 5 keys: UID, passwd_hash, name, email, birthdate
```python
user_info = {
    "jack_the_giant_slayer": {
        "UID": 1000,
        "passwd_hash":"0x2ee0c497e12313b89429e0f66362c042",
        "name": "jack",
        "email": "jack@beanstalk.com",
        "birthdate": "9/21/2000"
    },
    "jill_up_the_hill": {
        "UID": 1001,
        "passwd_hash": "0x40474d3a9628ad6dc495fb4a75f61977",
        "name": "jill",
        "email": "jill@pailofwater.com",
        "birthdate": "4/13/1992"
    }
}
```

<br>

## Length of a Multidimensional Collection
```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

#len()function call returns the number of elements in the list
len(list2d)             # Returns: 4 (number of rows/lists)
len(list2d)-1           # Returns: 3 (last row index)


row = 0                 #represents the row, in this case the row at index 0 
len(list2d[row])        # Returns: 6 number of columns/elements in a given row/list
len(list2d[row])-1      # Returns: 5 last column index 
```
`tuples are identical`
`sets cannot be nested`

`Nested dictionaries use keys instead of indexes`
```python
user_info = {
    "jack_the_giant_slayer": {
        "UID": 1000,
        "passwd_hash":"0x2ee0c497e12313b89429e0f66362c042",
        "name": "jack",
        "email": "jack@beanstalk.com",
        "birthdate": "9/21/2000"
    },
    "jill_up_the_hill": {
        "UID": 1001,
        "passwd_hash": "0x40474d3a9628ad6dc495fb4a75f61977",
        "name": "jill",
        "email": "jill@pailofwater.com",
        "birthdate": "4/13/1992"
    }
}

# len() function call returns the number of elements in the dictionary
len(user_info)  # Returns: 2


# Both of the following return the number of items in the inner dictionary
len(user_info.get("jack_the_giant_slayer"))     # Returns: 5
len(user_info["jack_the_giant_slayer"])         # Returns: 5
```

<br>

## Element Access

```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

# Use subscript notation to access elements --> list[row][col]
list2d[0][0] # Returns: a
list2d[0][1] # Returns: b
list2d[3][5] # Returns: z
```

```python
user_info = {
    "jack_the_giant_slayer": {
        "UID": 1000,
        "passwd_hash":"0x2ee0c497e12313b89429e0f66362c042",
        "name": "jack",
        "email": "jack@beanstalk.com",
        "birthdate": "9/21/2000"
    },
    "jill_up_the_hill": {
        "UID": 1001,
        "passwd_hash": "0x40474d3a9628ad6dc495fb4a75f61977",
        "name": "jill",
        "email": "jill@pailofwater.com",
        "birthdate": "4/13/1992"
    }
}


# Use subscript notation [] or .get() to access dictionary elements

user_info["jack_the_giant_slayer"]
user_info.get("jack_the_giant_slayer")
# Returns;
# {'UID': 1000, 'passwd_hash': 62311549687829319667013574547529187394, 'name': 'jack', 'email': 'jack@beanstalk.com', 'birthdate': '9/21/2000'}

user_info["jack_the_giant_slayer"]["email"]         # Returns: jack@beanstalk.com
user_info.get("jack_the_giant_slayer").get("email") # Returns: jack@beanstalk.com
```

<br>

## Changing Elements
```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

# Use subscript notation to access elements --> list[row][col]
list2d[0][0] = 65
list2d[0][1] = 66
list2d[3][5] = 120

# Changed list
# [
#   [ 65, 66,"c","d","e","f"], # 0
#   ["g","h","i","j","k","l"], # 1 row 
#   ["m","n","o","p","q","r"], # 2   indexes
#   ["s","t","u","v","w",120]  # 3
#   # 0   1   2   3   4   5
# ] #    column indexes
```
`tuples are immutable`
`sets cannot be nested `

`Dictionaries use keys instead of indexes`
```python
user_info = {
    "jack_the_giant_slayer": {
        "UID": 1000,
        "passwd_hash":"0x2ee0c497e12313b89429e0f66362c042",
        "name": "jack",
        "email": "jack@beanstalk.com",
        "birthdate": "9/21/2000"
    },
    "jill_up_the_hill": {
        "UID": 1001,
        "passwd_hash": "0x40474d3a9628ad6dc495fb4a75f61977",
        "name": "jill",
        "email": "jill@pailofwater.com",
        "birthdate": "4/13/1992"
    }
}


# Use subscript notation [] or .get() to access dictionary elements
user_info["jack_the_giant_slayer"]["email"] = "jack@goldengoose.org"   
user_info.get("jack_the_giant_slayer").get("email") = "jack@goldengoose.org"

# Updated dictionary
# user_info = {
#     "jack_the_giant_slayer": {
#         "UID": 1000,
#         "passwd_hash":"0x2ee0c497e12313b89429e0f66362c042",
#         "name": "jack",
#         "email": "jack@goldengoose.org",
#         ...
# ...
```

<br>

## Methods to remember
```python
list2d.append()  # Adds a single element x to the end of the list.
list2d.extend()  # Extends the list by appending elements from the iterable.
list2d.insert()  # Inserts an element x at a given index i.
list2d.remove()  # Removes the first occurrence of element x from the list.
list2d.pop()     # Removes the element at the given index i and returns it. default is the last element
list2d.clear()   # Removes all elements from the list.
list2d.index()   # Returns the index of the first occurrence of element x 
list2d.count()   # Returns the number of occurrences of element x in the list.
list2d.sort()    # Sorts the list in ascending order. 
list2d.reverse() # Reverses the elements of the list in place.
list2d.copy()    # Returns a shallow copy (reference location) of the list.
```

```python
dict2d.copy()        # Returns a shallow copy of the dictionary.
dict2d.fromkeys()    # Creates a new dictionary with keys from an iterable and values set to a specified value.
dict2d.pop()         # Removes the specified key and returns the corresponding value.
dict2d.popitem()     # Removes and returns the last inserted key-value pair as a tuple.
dict2d.setdefault()  # Returns the value of a key if it is in the dictionary; if not, inserts the key with a specified value.
dict2d.clear()       # Removes all items from the dictionary.
```

<br>


## <table><th>`Multidimensional Collection Iteration Syntax`</th></table>
> * Nested loops are used to iterate through the contents of a collection
> * for loops are typically best suited to this type of iteration
> * However, while loops can also be used. 

## For Loops

### Lists and Tuples
`r represents row indexes ` 
`row represents row elements`

`c represents column indexes`
`col represents column elements`

syntax:
```
for r in range(start,stop,step):
    for c in range(start, stop, step):
        ...
    ...
```
abstract example:
```python
#Outer Loop 
#start a the first list, stop at the last list, increment by 1
for row in range(0,len(list2d),1):
    ...
 

#Inner Loop
#start at the first item, stop at  the last item, increment by 1
for col in range(0,len(list2d[row]),1):
    ...


'The inner loop goes inside of the outer loop'
#Outer Loop-------------------------------------------------#
for row in range(0,len(list2d),1):                          #
    #Inner Loop----------------------------------#          #
    for col in range(0,len(list2d[row]),1):      #          #
        ...                                      #          #
    #exit inner loop-----------------------------#          #
#exit outer loop--------------------------------------------#
```
For Each Loop

syntax:
```
for row in list2d:
    for col in row:
        ...
    ...
```

abstract example:
```python
for row in list2d:
    for col in row:
        print(col, end = " ")
```

***Using enumerate() is considered best practice***
> * it allows access to both the index, and element.

syntax:
```
for r, row in enumerate(list2d):
    for c, col in enumerate(row):
        ...
    ...
```
abstract example:
```python
for r, row in enumerate(list2d):
    for c, col in enumerat(row):
        print((r,c,col), end = " ")
    print()
```

<br>

## Dictionaries
> * Dictionaries are not numerically indexed
> * This means that for-each loops are necessary to access all elements of a list
NOTE:
> Dictionaries are unordered, since key:value pairs are hashed order doesn't matter, values are simply accessed by thier key.

syntax: 
```
for dict_key in dict2d:
    for inner_key in dict2d.get(dict_key):
        ...
    ...
```
abstract example:
```python
for dict_key in dict2d:
    for inner_key in dict2d.get(dict_key):
        print((inner_key, dict2.get(dict_key).get(inner_key)), end = " ")
    print()
```
<br>

## While Loops

syntax:
```
r = row_start
while(r < len(list2d)):
    c = col_start
    while(c < len(list2d[r])):
        ...
        c += col_step
    ...
    r += row_step
```

abstract example:
```python
#Outer loop
r = 0 #start at the first list 
while( r < len(list2d) ): #OR r <= len(list2d)-1 ; stop at last list
    ...
    r += 1 #increment by 1
#exit outer while


#Inner Loop
c = 0 #start at first item
while( c < len(list2d[r]) ): #OR c <= len(list2d[r])-1 ; stop at last item
    ...
    c += 1 #increment by 1
#exit inner loop


'The inner loop goes inside of the outer loop'
#Outer loop-------------------------------------------#
r = 0                                                 #
while( r < len(list2d) ):                             #
                                                      #
    #Inner Loop---------------------------#           #
    c = 0 #start at first item            #           #
    while( c < len(list2d[r]) ):          #           #
        ...                               #           #
        c += 1                            #           #
    #exit inner loop----------------------#           #
                                                      #
    r += 1                                            # 
#exit outer while-------------------------------------#

```
<br>

## <table><th>`Forward Iteration: Beginning to End`</th></table>

## For Loop: Forward
```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes


for r, row in enumerate(list2d):
    for c, col in enumerate(row):
        print((r,c,col), end = " ")
    print()

#Output:
# (0, 0, 'a') (0, 1, 'b') (0, 2, 'c') (0, 3, 'd') (0, 4, 'e') (0, 5, 'f') 
# (1, 0, 'g') (1, 1, 'h') (1, 2, 'i') (1, 3, 'j') (1, 4, 'k') (1, 5, 'l') 
# (2, 0, 'm') (2, 1, 'n') (2, 2, 'o') (2, 3, 'p') (2, 4, 'q') (2, 5, 'r') 
# (3, 0, 's') (3, 1, 't') (3, 2, 'u') (3, 3, 'v') (3, 4, 'w') (3, 5, 'x') 
```

```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

for r in range(0,len(list2d),1):                    # start at 0, stop at the last row, increment by 1
    for c in range(0,len(list2d[row]),1):           # start at 0, stop at the last col, increment by 1
        print((r,c,list2d[row][col]), end = " ")    # print r index, c index, and element
    print()                                         # print a new line

#Output:
# (0, 0, 'a') (0, 1, 'b') (0, 2, 'c') (0, 3, 'd') (0, 4, 'e') (0, 5, 'f') 
# (1, 0, 'g') (1, 1, 'h') (1, 2, 'i') (1, 3, 'j') (1, 4, 'k') (1, 5, 'l') 
# (2, 0, 'm') (2, 1, 'n') (2, 2, 'o') (2, 3, 'p') (2, 4, 'q') (2, 5, 'r') 
# (3, 0, 's') (3, 1, 't') (3, 2, 'u') (3, 3, 'v') (3, 4, 'w') (3, 5, 'x') 
```

```python
user_info = {
    "jack_the_giant_slayer": {
        "UID": 1000,
        "passwd_hash":"0x2ee0c497e12313b89429e0f66362c042",
        "name": "jack",
        "email": "jack@beanstalk.com",
        "birthdate": "9/21/2000"
    },
    "jill_up_the_hill": {
        "UID": 1001,
        "passwd_hash": "0x40474d3a9628ad6dc495fb4a75f61977",
        "name": "jill",
        "email": "jill@pailofwater.com",
        "birthdate": "4/13/1992"
    },
    "hansel_in_the_woods": {
        "UID": 1002,
        "passwd_hash": "0x7a62d08f8d6d5f4a3d1b56f4a73a5b7e",
        "name": "hansel",
        "email": "hansel@gingerbread.com",
        "birthdate": "3/10/1995"
    },
    "gretel_with_the_crumbs": {
        "UID": 1003,
        "passwd_hash": "0x3b5a6f6d8c4b7a3a3f2c5b6a7d5e3f4b",
        "name": "gretel",
        "email": "gretel@gingerbread.com",
        "birthdate": "7/19/1996"
    },
    "red_riding_hood": {
        "UID": 1004,
        "passwd_hash": "0x8d6f5b4c7a3e5d6f4b3a7c6d8f5b4a6c",
        "name": "red",
        "email": "red@wolf.com",
        "birthdate": "5/25/2001"
    }
}

for user in user_info:
    print(user)
    for key in user_info.get(user):
        print((key, user_info.get(user).get(key)),end = " ")
    print()

#Output:
# jack_the_giant_slayer
# ('UID', 1000) ('passwd_hash', '0x2ee0c497e12313b89429e0f66362c042') ('name', 'jack') ('email', 'jack@beanstalk.com') ('birthdate', '9/21/2000')       
# jill_up_the_hill
# ('UID', 1001) ('passwd_hash', '0x40474d3a9628ad6dc495fb4a75f61977') ('name', 'jill') ('email', 'jill@pailofwater.com') ('birthdate', '4/13/1992')     
# hansel_in_the_woods
# ('UID', 1002) ('passwd_hash', '0x7a62d08f8d6d5f4a3d1b56f4a73a5b7e') ('name', 'hansel') ('email', 'hansel@gingerbread.com') ('birthdate', '3/10/1995') 
# gretel_with_the_crumbs
# ('UID', 1003) ('passwd_hash', '0x3b5a6f6d8c4b7a3a3f2c5b6a7d5e3f4b') ('name', 'gretel') ('email', 'gretel@gingerbread.com') ('birthdate', '7/19/1996') 
# red_riding_hood
# ('UID', 1004) ('passwd_hash', '0x8d6f5b4c7a3e5d6f4b3a7c6d8f5b4a6c') ('name', 'red') ('email', 'red@wolf.com') ('birthdate', '5/25/2001') 
```

<br>

## While Loop: Forward
```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

r = 0                                               # start at row 0
while( r < len(list2d)):                            # stop at the last row
    c = 0                                           # start at col 0
    while(c < len(list2d[r])):                      # stop at the last col
        print((r,c,list2d[r][c]), end = " ")        # print the row index, col index, and element
        c += 1                                      # increment col by 1
    r += 1                                          # increment row by 1
    print()

# Output:
# (0, 0, 'a') (0, 1, 'b') (0, 2, 'c') (0, 3, 'd') (0, 4, 'e') (0, 5, 'f') 
# (1, 0, 'g') (1, 1, 'h') (1, 2, 'i') (1, 3, 'j') (1, 4, 'k') (1, 5, 'l')
# (2, 0, 'm') (2, 1, 'n') (2, 2, 'o') (2, 3, 'p') (2, 4, 'q') (2, 5, 'r')
# (3, 0, 's') (3, 1, 't') (3, 2, 'u') (3, 3, 'v') (3, 4, 'w') (3, 5, 'x')
```

<br>

## <table><th>`Reverse Iteration: End to Beginning`</th></table> 
```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes


for r, row in enumerate(reversed(list2d)):
    for c, col in enumerate(reversed(row)):
        print((r,c,col), end = " ")
    print()

# Output:
# (0, 0, 'x') (0, 1, 'w') (0, 2, 'v') (0, 3, 'u') (0, 4, 't') (0, 5, 's') 
# (1, 0, 'r') (1, 1, 'q') (1, 2, 'p') (1, 3, 'o') (1, 4, 'n') (1, 5, 'm') 
# (2, 0, 'l') (2, 1, 'k') (2, 2, 'j') (2, 3, 'i') (2, 4, 'h') (2, 5, 'g') 
# (3, 0, 'f') (3, 1, 'e') (3, 2, 'd') (3, 3, 'c') (3, 4, 'b') (3, 5, 'a') 
```

```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes


for r in range(len(list2d)-1,-1,-1):            # start at the last row stop at 0, decrement by 1
    for c in range(len(list2d[r])-1,-1,-1):     # start at the last col, stop at 0, decrement by 1
        print((r,c,list2d[r][c]), end = " ")    # print r index, c index, and element
    print()                                     # print a new line

# Output:
# (3, 5, 'x') (3, 4, 'w') (3, 3, 'v') (3, 2, 'u') (3, 1, 't') (3, 0, 's') 
# (2, 5, 'r') (2, 4, 'q') (2, 3, 'p') (2, 2, 'o') (2, 1, 'n') (2, 0, 'm') 
# (1, 5, 'l') (1, 4, 'k') (1, 3, 'j') (1, 2, 'i') (1, 1, 'h') (1, 0, 'g') 
# (0, 5, 'f') (0, 4, 'e') (0, 3, 'd') (0, 2, 'c') (0, 1, 'b') (0, 0, 'a') 

# Notice that the indexes did not change.
```

<br>

## While Loop: Reverse
```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

r = len(list2d)-1                                   # start at the last row
while( r > -1 ):                                    # stop at 0
    c = len(list2d[r])-1                            # start at last col
    while(c > -1):                                  # stop at 0
        print((r,c,list2d[r][c]), end = " ")        # print the row index, col index, and element
        c -= 1                                      # decrement col by 1
    r -= 1                                          # decrement row by 1
    print()

# Output:
# (3, 5, 'x') (3, 4, 'w') (3, 3, 'v') (3, 2, 'u') (3, 1, 't') (3, 0, 's') 
# (2, 5, 'r') (2, 4, 'q') (2, 3, 'p') (2, 2, 'o') (2, 1, 'n') (2, 0, 'm')
# (1, 5, 'l') (1, 4, 'k') (1, 3, 'j') (1, 2, 'i') (1, 1, 'h') (1, 0, 'g') 
# (0, 5, 'f') (0, 4, 'e') (0, 3, 'd') (0, 2, 'c') (0, 1, 'b') (0, 0, 'a')
```

<br>

## <table><th>`Complex Iteration`</th></table>
> Nested collections can become quite complicated, but ultimately are extremely useful.
> There are many different possiblities when it comes to complex iteration.

## Below are examples to get you thinking

*Working with large data sets*
```python
# Count the number of 7s
list2d = [
    [4, 2, 7, 2, 7, 2, 6, 5, 6, 6], [7, 7, 8, 5, 8, 1, 3, 7, 6, 5], [5, 1, 3, 8, 8, 0, 6, 3, 6, 6], [5, 8, 6, 0, 4, 4, 9, 9, 6, 8], 
    [4, 8, 3, 1, 7, 9, 3, 4, 7, 1], [4, 7, 4, 7, 7, 1, 7, 4, 7, 4], [6, 0, 6, 1, 2, 7, 8, 1, 7, 5], [9, 3, 6, 1, 4, 2, 0, 1, 3, 1], 
    [8, 2, 5, 1, 1, 2, 6, 2, 0, 2], [2, 8, 7, 0, 6, 0, 7, 5, 3, 4], [2, 3, 8, 0, 8, 9, 8, 2, 5, 0], [8, 2, 9, 5, 4, 5, 2, 5, 3, 8], 
    [8, 3, 7, 2, 3, 7, 3, 4, 9, 4], [6, 6, 7, 2, 3, 2, 6, 1, 5, 7], [0, 0, 3, 7, 5, 6, 9, 9, 9, 8], [6, 7, 8, 0, 4, 1, 0, 0, 3, 7], 
    [8, 4, 4, 2, 4, 2, 4, 4, 1, 0], [9, 0, 1, 1, 2, 3, 3, 6, 9, 4], [6, 7, 2, 3, 9, 3, 1, 4, 1, 5], [7, 3, 6, 5, 3, 7, 6, 1, 6, 3], 
    [1, 5, 7, 4, 7, 6, 6, 2, 9, 9], [1, 7, 0, 6, 8, 0, 0, 4, 8, 2], [0, 1, 5, 3, 0, 4, 6, 6, 0, 9], [5, 6, 8, 7, 1, 5, 9, 1, 9, 2], 
    [1, 4, 1, 0, 7, 2, 6, 1, 3, 4], [8, 8, 9, 7, 4, 6, 0, 6, 7, 6], [6, 5, 7, 6, 1, 3, 5, 6, 4, 7], [9, 2, 1, 7, 1, 9, 5, 4, 3, 7], 
    [2, 2, 9, 8, 7, 4, 0, 0, 1, 8], [8, 0, 1, 0, 8, 1, 8, 4, 8, 4], [2, 0, 8, 0, 9, 1, 8, 7, 9, 8], [6, 2, 8, 0, 1, 9, 0, 1, 3, 9], 
    [1, 1, 7, 0, 1, 5, 5, 1, 2, 2], [9, 6, 0, 0, 2, 4, 7, 1, 1, 6], [5, 5, 6, 7, 6, 8, 7, 1, 4, 3], [3, 2, 6, 7, 2, 8, 3, 0, 2, 6], 
    [2, 2, 6, 0, 7, 9, 9, 9, 3, 6], [8, 7, 6, 1, 2, 3, 6, 1, 4, 2], [9, 1, 4, 9, 0, 8, 7, 7, 3, 0], [1, 8, 5, 6, 2, 5, 7, 1, 5, 4], 
    [4, 8, 6, 9, 0, 6, 8, 9, 7, 4], [9, 6, 3, 9, 1, 3, 2, 5, 6, 0], [9, 8, 7, 6, 6, 9, 5, 1, 8, 1], [4, 7, 5, 8, 1, 1, 4, 8, 9, 1], 
    [9, 6, 7, 2, 7, 1, 9, 9, 1, 0], [1, 0, 5, 3, 3, 4, 5, 0, 2, 1], [4, 5, 6, 8, 5, 3, 9, 6, 5, 3], [9, 2, 1, 3, 6, 6, 7, 0, 5, 5], 
    [8, 8, 0, 2, 2, 1, 7, 8, 7, 3], [8, 0, 2, 3, 3, 6, 5, 3, 3, 3], [5, 1, 8, 6, 5, 7, 8, 9, 8, 6], [7, 3, 8, 9, 9, 3, 2, 6, 4, 9], 
    [7, 6, 6, 8, 6, 9, 1, 3, 8, 9], [1, 4, 6, 3, 7, 3, 4, 0, 5, 0], [7, 4, 0, 5, 5, 8, 1, 8, 4, 8], [5, 9, 6, 0, 3, 3, 1, 9, 7, 6], 
    [6, 1, 5, 4, 2, 1, 0, 7, 1, 8], [0, 8, 1, 2, 8, 6, 1, 9, 8, 2], [5, 6, 8, 4, 7, 3, 0, 6, 5, 0], [2, 7, 7, 3, 0, 4, 0, 9, 0, 2], 
    [7, 3, 2, 8, 2, 0, 0, 5, 1, 8], [4, 3, 8, 0, 1, 6, 8, 2, 5, 3], [4, 8, 2, 9, 0, 9, 6, 1, 8, 4], [2, 2, 7, 8, 6, 5, 2, 9, 5, 6], 
    [5, 0, 5, 4, 9, 8, 6, 3, 3, 7], [0, 6, 6, 6, 2, 1, 7, 8, 4, 6], [1, 8, 7, 2, 1, 8, 0, 9, 1, 2], [0, 2, 3, 2, 4, 4, 7, 0, 1, 2], 
    [2, 0, 1, 0, 6, 3, 3, 8, 6, 3], [4, 6, 1, 4, 8, 1, 3, 8, 0, 3], [1, 6, 5, 9, 5, 1, 5, 6, 2, 5], [9, 7, 3, 7, 3, 7, 8, 4, 4, 6], 
    [2, 8, 2, 7, 9, 8, 4, 5, 7, 8], [9, 8, 7, 9, 8, 3, 3, 1, 7, 8], [8, 8, 3, 2, 5, 3, 4, 1, 0, 8], [9, 6, 1, 6, 2, 2, 5, 2, 3, 9], 
    [5, 3, 1, 2, 9, 7, 1, 6, 0, 4], [6, 2, 0, 5, 7, 2, 2, 8, 4, 0], [4, 4, 0, 4, 5, 1, 6, 6, 6, 9], [2, 0, 7, 5, 6, 3, 9, 8, 4, 2], 
    [9, 2, 8, 8, 4, 1, 7, 2, 8, 3], [0, 3, 4, 0, 8, 9, 5, 0, 3, 9], [4, 5, 6, 1, 8, 3, 5, 4, 9, 8], [0, 3, 7, 2, 6, 0, 8, 3, 2, 7], 
    [8, 1, 6, 7, 4, 5, 6, 9, 8, 0], [5, 5, 1, 0, 5, 1, 0, 7, 9, 1], [5, 4, 8, 1, 0, 2, 2, 3, 5, 2], [4, 9, 8, 2, 7, 8, 9, 2, 4, 2], 
    [2, 1, 5, 7, 7, 6, 7, 1, 8, 2], [5, 3, 6, 3, 6, 4, 1, 2, 9, 3], [6, 6, 4, 7, 3, 6, 5, 1, 3, 0], [3, 4, 4, 2, 0, 5, 7, 4, 2, 3], 
    [3, 4, 7, 6, 7, 7, 0, 5, 5, 0], [6, 7, 7, 5, 3, 0, 8, 0, 9, 6], [2, 5, 3, 2, 3, 2, 3, 2, 4, 3], [2, 5, 9, 8, 5, 9, 0, 6, 6, 2], 
    [6, 9, 9, 4, 8, 6, 5, 0, 2, 0], [5, 1, 4, 2, 8, 6, 2, 7, 9, 5], [0, 6, 4, 9, 4, 4, 3, 0, 0, 7], [3, 0, 2, 8, 9, 9, 4, 3, 5, 8]
]

count = 0
for row in range(len(list2d)):              #defaults start == 0 and step == 1
    for col in range(len(list2d[row])):     #defaults start == 0 and step == 1
        if(7 == list2d[row][col]):
            count +=1
print(count) # Output: 101
```

```python
#Change each consonant to a "C" and each vowel to a "V"

list2d = [                                      #For Loops with 2d Lists
  ["a","b","c","d","e","f"],# 0                 Keep these things in mind
  ["g","h","i","j","k","l"],# 1  row indexes        to access an element --> list2d[row][col]
  ["m","n","o","p","q","r"],# 2                     range(start, stop, step)
  ["s","t","u","v","w","x"] # 3               
  # 0   1   2   3   4   5
        #column indexes
]
# len(list2d) == 4 // len(list2d[row] == 6)

vowels = "aeiou"
for row in range(len(list2d)):                  #defaults start == 0 and step == 1
    for col in range(len(list2d[row])):         #defaults start == 0 and step == 1
        if list2d[row][col] in vowels:
            list2d[row][col] = "V"
        else:
            list2d[row][col] = "C"

print(list2d)
```

```python
#Loop in a serpentine pattern
list2d = [ 
  [0, 1, 2, 3, 4], #forward
  [0, 1, 2, 3, 4], #backward
  [0, 1, 2, 3, 4], #forward
  [0, 1, 2, 3, 4], #backward
  [0, 1, 2, 3, 4]  #forward
] 

for row in range(len(list2d)):
    if(0 == row % 2):
        for col in range(len(list2d[row])):
            print(list2d[row][col], end = " ")
    else:
        for col in range(len(list2d[row]-1,-1,-1)):
            print(list2d[row][col], end = " ")
```