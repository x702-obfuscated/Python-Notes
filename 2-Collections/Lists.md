# <table><th>Python Lists</th></table>
___
**Covered in this file:**
```
1. Defining a list
2. Creating a List 
3. Converting from Tuples and Sets
4. List Operations
5. Accessing Elements in a List
6. Changing Elements in a List
7. Built-in list function calls 
8. Built-in list methods calls
9. List Slicing and Concatenation
10. Lists of Lists: Nested Lists
11. Unpacking Collections
12. List Comprehension
13. List Iteration: Looping
```

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


## <table><th>Defining a List</th></table>
___
**Lists:** 
> * are basically a collection of  comma seperated elements
> * are specifically a collection of data that is ordered, mutable, and allows duplicate members.
> * use [ ] to enclose elements

*Note: Python lists are similiar to arrays in other programming languages. Unlike lists, arrays have a fixed size meaning values cannot be added to the array.*

### List Example


```python
["a","b","c","d","e"] #a list

#add a newline after a comma to make the list more readable
['a', 'b', 'c', 'd', 'e', 
 'f', 'g', 'h', 'i', 'j', 
 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 
 'u', 'v', 'w', 'x', 'y', 
 'z'
]

# Other examples:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bools  = [True, False]

numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lcase_alpha = [
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
]

ucase_alpha = [
    'A', 'B', 'C', 'D', 'E', 'F', 
    'G', 'H', 'I', 'J', 'K', 'L', 
    'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 
    'Y', 'Z'
]
```

A list contains multiple items called elements or members
|elements|"a"|"b"|"c"|"d"|"e"|
|:-:|:-:|:-:|:-:|:-:|:-:|
|indexes|0|1|2|3|4|
|Length|||||5|

An index indicates the spot at which an element is located.   
Indexes can be used to access each element in the list. 

The length of a list is the total number of elements contained in the list   




```python
#         [------------------elements---------------------]
list1d =  ["a","b","c","d","e","f","g","h","i","j","k","l"]
# index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
# reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]
#                          Length = 12
```

## <table><th>Creating a list</th></table>
___
> * use [ ] to denote a list
> * seperate elements of a list with commas
> * The list(iterable) constructor builds a list

> * Create and empty list with [ ]


```python
[] #creates an empty list

list1d = [] 
```

> * Enclose comma seperated elements with [ ]


```python
#use [] and seperate each element with commas
list1d = [1,2,3,4,5,6,7,8,9] 
#index    0 1 2 3 4 5 6 7 8
#length = 9
```

> * Use the list(iterable) constructor call

syntax:

    list(iterable)
    


```python
#use the list(iterable) constructor call
list() # Returns: []
list('abcdef') # Returns: ['a', 'b', 'c', 'd', 'e', 'f']
```

## <table><th>Converting from Tuples and Sets</th></table>
___
> * The list(iterable) constructor builds a list
> * The tuple(iterable) constructor builds a tuple
> * The set(iterable) constructor builds a set

Constructors are special methods defined by a class that are used to build instances of a class. 
> * ie. the list(iterable) constructor makes a list.


```python
list("abcdef") #Returns: ['a', 'b', 'c', 'd', 'e', 'f']
```


```python
tuple1d = (1,2,3,4,5)

list(tuple1d) #Returns: [1, 2, 3, 4, 5]
```


```python
set1d = {"dog","cat","horse"}

list(set1d) # Returns: ['cat', 'dog', 'horse']
```


```python
list1d = [1,2,3,4,5]

#From list to tuple use tuple(iterable)
tuple1d = tuple(list1d) #Returns: (1,2,3,4,5)

#From list to set use set(iterable)
set1d = set(list1d) #Returns: {1,2,3,4,5}
```

## <table><th>List Operations</th></table>
___

|Operation| Description|
|:-:|:-:|
|in| checks if a value is a member|
|not in| checks if a value is not a member|
|+|concatenates two lists|
|+=|concatenates and assigns|
|*| duplicates a list|
|*=|duplicates and assigns|



```python
#multi variable assignment with lists
a, b, c = [1,2,3]
#a = 1 b = 2 c = 3
```

> * Check if a value is a member of a list

syntax:

    value in list


```python
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha = [
  'a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

#Check Membership (in/not in)
"a" in alpha    #Returns: True
"a" in numerals #Returns: False

```

> * Check if a value is not apart of a list

syntax:

    value not in list



```python
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha = [
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
]

#Check Membership (in/not in)
"5" not in alpha    #Returns: True
"5" not in numerals #Returns: False
```

> * Concatenation (joining)

syntax:

    list1 + list2


```python
numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alpha = [
  'a', 'b', 'c', 'd', 'e', 'f',
  'g', 'h', 'i', 'j', 'k', 'l', 
  'm', 'n', 'o', 'p', 'q', 'r', 
  's', 't', 'u', 'v', 'w', 'x', 
  'y', 'z'
]

numerals + alpha

# Returns:
# [ '0', '1', '2', '3', '4', '5', 
#   '6', '7', '8', '9', 'a', 'b',
#   'c', 'd', 'e', 'f', 'g', 'h',
#   'i', 'j', 'k', 'l', 'm', 'n',
#   'o', 'p', 'q', 'r', 's', 't', 
#   'u', 'v', 'w', 'x', 'y', 'z' ] 
```

> * Concatenate and Assign

syntax:

    list1 += list2


```python
a = [1,2,3,4]
a += [5,6,7,8]
a += [9,10,11,12]

print(a) #Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

> * Duplication

syntax:

    list1 * n

*n is the number of times to duplicate the list*



```python
pattern = [1, 0, 0, 1]

pattern * 4 
# Returns: [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1]
```

> * Duplicate and Assign

syntax:

    list1 *= n

*n is the number of times to duplicate the list*


```python
b = [1, 0]
b *= 5
print(b) #Output: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
```

## <table><th>Accessing Elements in a List</th></table>
___

To access the data in a list using the index an subscripting []
syntax:

    list[index]

list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
|elements |"a"|"b"|"c"|"d"|"e"|"f"|"g"|"h"|"i"|"j"|"k"|"l"|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|index|0|1|2|3|4|5|6|7|8|9|10|11|
|reverse/negative index|-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

elements in a list are accessed by their index


```python
#         [------------------elements---------------------]
list1d =  ["a","b","c","d","e","f","g","h","i","j","k","l"]
# index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
# reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]
#                          Length = 12
```

**Regular Indexing**


```python
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]

list1d[0]   # Returns: a
list1d[5]   # Returns: f
list1d[10]  # Returns: k
```

**Reverse/Negative Indexing**


```python
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]

list1d[-1]  # Returns: l
list1d[-5]  # Returns: h
list1d[-10] # Returns: c
```

## <table><th>Changing Elements in a List</th></table>
___

Elements (data) in a list can be changed using the index of the element and subscripting []

syntax:

    list[index] = new_value

list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
|elements |"a"|"b"|"c"|"d"|"e"|"f"|"g"|"h"|"i"|"j"|"k"|"l"|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|index|0|1|2|3|4|5|6|7|8|9|10|11|
|reverse/negative index|-12|-11|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

elements in a list are changed by assigning a new value to its index


```python
list1d = ["a","b","c","d","e","f","g","h","i","j","k","l"]
print(f"Before: {list1d}") 


# Starting from the front end
list1d[0] = "z" 
list1d[5] = "y" 
list1d[10] = "x" 

# Starting from the back end (Reverse indexing)
list1d[-1] = "m"
list1d[-5] = "n"
list1d[-10] = "o"


print(f"After:  {list1d}")
# Here is the list after running the code above:
#list1d = ["z","b","o","d","e","y","g","n","i","j","x","m"]
#index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
#reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]
```

## <table><th>Built-in List Function Calls</th></table>
___
**Functions:**
* are blocks of reusable code, that perform a specific task.
* must be defined before they are called

* are typically called using their name followed by parenthesis with any required arguments inside.


Built-in Functions are pre-defined by the standard library


```python
#         [------------------elements---------------------]
list1d =  ["a","b","c","d","e","f","g","h","i","j","k","l"]
# index   [ 0   1   2   3   4   5   6   7   8   9   10  11]
# reverse [-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1]
# length = 12

# len()
len(list1d)   #returns number of elements in a list
len(list1d)-1 #returns the last index of the list

#max()
max(list1d) #Returns the largest element in the list.

#min()
min(list1d)#Returns the smallest element in the list.

#sum(list1d)
nums = [1,2,3,4,5]
sum(nums) #Returns the sum of all elements in a number list.

# Returns the list reversed
reversed(list1d)

# Returns an iterator of tuples containing the index, and elem of the list.
enumerate(list1d)

#Returns a sorted list in ascending order
sorted(list1d)

#Combines two lists into an iterator of tuples 
list1 = ["a","b","c"]
list2 = [1,2,3]
zip(list1, list2)
# ("a",1),("b",2),("c",3)
```

## <table><th>Built-in List Method Calls</th></table>
___
**Methods:**
* are functions defined by a class
* are typically called using an object or class and dot ( . ) syntax

syntax for methods which require objects:

    object.method(arguments)

syntax for methods which DO NOT require objects:

    class.method(arguments)

Built-in methods are pre-defined by classes pre-defined by the standard library

To see what methods you can call on an object use:  
    
    dir(object)  

To see more information on a specific method use:  
    
    help(object.method)


```python
#To see what methods you can call on an object use dir(object)
#To see more information on a specific method use help(object.method)

#.append() 
list1d.append("new elem")# Adds a single element x to the end of the list.

#.extend(iterable)
list1d.extend("iterable")# Extends the list by appending elements from the iterable.

#.insert(i, x)
list1d.insert(5, "new elem")# Inserts an element x at a given index i.

#.remove(x)
list1d.remove("elem to remove")# Removes the first occurrence of element x from the list.

#.pop(i)
list1d.pop(1)# Removes the element at the given index i and returns it.
list1d.pop() #If no index is specified, pop() removes and returns the last element in the list.

#.clear()
list1d.clear()# Removes all elements from the list.

#.index(x, start, end)
list1d.index("elem")# Returns the index of the first occurrence of element x 
list1d.index("elem",2,5)#(optional start and end indices can be specified).

#.count(x)
list1d.count("elem")# Returns the number of occurrences of element x in the list.

#.sort(key=None, reverse=False)
list1d.sort()# Sorts the list in ascending order. 
list1d.sort(key=len)#Optionally, you can provide a key function call for custom sorting
list1d.sort(reverse=True)#set reverse to True for descending order.

#.reverse()
list1d.reverse()# Reverses the elements of the list in place.

#.copy()
list1d.copy()# Returns a shallow copy (reference location) of the list.
```

## <table><th>List Slicing and Concatenation</th></table>
___

**Slicing:**
> * is creating a sublist, by returning parts of the original list
> * use slicing notation [ : : ] to return a sublist

slicing syntax:
    
    list[start_index:stop_index:step]

> * start_index is inclusive (the character at start_index will appear in the sublist)
> * stop_index is exclusive (the character at the stop_index will NOT appear in the sublist)


Be sure to pick the right stop_index
> * for ascending ( + step ) sublists add one to the last index you want to include (stop + 1)  
> * for descending ( - step ) sublists subtract one from the last index you want to include (stop - 1)

### Slicing Examples:


```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# Ascending
list1d[1:6:2] # Returns: ['b', 'd', 'f']
list1d[0:9:3] # Returns: ['a', 'd', 'g']
list1d[2:8:3] # Returns: ['c', 'f']
list1d[1:7:1] # Returns: ['b', 'c', 'd', 'e', 'f', 'g']

# Descending
list1d[4:1:-1]    # Returns: ['e', 'd', 'c']
list1d[-1:-5:-1]  # Returns: ['i', 'h', 'g', 'f']
list1d[7:0:-1]    # Returns: ['h', 'g', 'f', 'e', 'd', 'c', 'b']
list1d[8:0:-2]    # Returns: ['i', 'g', 'e', 'c']

```

### Ascending Slices:
> * Default start_index is 0
> * Default stop_index is len(list) (end of the list)
> * Default step is 1
> * The slice includes the start_index, but excludes the stop_index


```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

#If a start_index is not provided the default is 0
list1d[:3:1] # Returns: ['a', 'b', 'c']
list1d[:6:3] # Returns: ['a', 'd']

#If a stop_index is not provided the default is len(list)
list1d[0:]   # Returns:  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list1d[5:]   # Returns:  ['f', 'g', 'h', 'i']
list1d[::2]  # Returns:  ['a', 'c', 'e', 'g', 'i']

# If the step is not specified the default is 1 
list1d[0:5] # Returns: ['a', 'b', 'c', 'd', 'e']
list1d[:3]  # Returns: ['a', 'b', 'c']
list1d[6::] # Returns: ['g', 'h', 'i']
```

### Descending Slices:
> * Default start_index is len(list) (end of the list)
> * Default stop_index is the beginning of the list
>   * In order to include the character at index 0 you must use the default stop_index 
> * Must specify a negative step
> * The slice includes the start_index, but excludes the stop_index


```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

#If a start_index is not provided the default is len(list)
list1d[:4:-1]     # Returns: ['i', 'h', 'g', 'f']
list1d[:-6:-1]    # Returns: ['i', 'h', 'g', 'f', 'e']
list1d[::-1]      # Returns: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

#If a stop_index is not provided the default is len(list)
list1d[5::-1]     # Returns: ['f', 'e', 'd', 'c', 'b', 'a']
list1d[-3::-1]    # Returns: ['g', 'f', 'e', 'd', 'c', 'b', 'a']
list1d[::-3]      # Returns: ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
```

> * Assign to a slice of a list using slice notation

slice assignment syntax:

    list[start_index:stop_index:step] = [new list values]


```python
list1d = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1d[2:5] = [1,2,3]
print(list1d) # Outputs: ['a', 'b', 1, 2, 3, 'f', 'g', 'h', 'i']
```

## <table><th>Lists of Lists: Nested Lists</th></table>
___
> * a 2D list is a list that contains other lists (a list of lists).  
> * called a nested list or multidimensional list  
> * each list is accessed with its index and subscripting
>
> * each element of the lists are access with 2 indexes and subscripting [][] 
>   * the first index is the list index, the second is the element index 




```python
#index   [[---------list 0--------],[--------list 1---------],[--------list 2---------],[--------list 3---------]]
#reverse [[---------list -4-------],[--------list-3---------],[--------list -2--------],[--------list -1--------]]
list2d = [["a","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"]]
#index   [[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ],[ 0   1   2   3   4   5 ]]
#reverse [[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ],[-6  -5  -4  -3  -2  -1 ]]   
```

Formatting the 2D lists in our code can make them easier to read.  
A 2D list can then be thought of as rows, and columns.


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

### Accessing Elements from a 2D List
syntax:
    
    2DList[list_index][element_index]
    OR
    2DList[row][col]


```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

list2d[0][0] # Returns: a
list2d[0][1] # Returns: b
list2d[3][5] # Returns: x
```

### Changing the Value of an index in a 2D List
syntax:

    2DList[list_index][element_index] = new_value
    OR
    2DList[row][col] = new_value


```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

list2d[0][0] = "aa"
#[["aa","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"]]
#   ^^

list2d[3][5] = "xx"
#[["aa","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","xx"]]
#-->                                                                                                   ^^     
```

### Length of 2D Lists
The len() function call returns the number of elements in the list
> * len(list2d) returns the number of rows/lists
> * len(list2d[row]) returns the number of columns/elements in a given row/list

> * len(list2d)-1 returns the last row index
> * len(list2d[row])-1 returns the last column index in a given row/list


```python
list2d = [
  ["a","b","c","d","e","f"], # 0
  ["g","h","i","j","k","l"], # 1 row 
  ["m","n","o","p","q","r"], # 2   indexes
  ["s","t","u","v","w","x"]  # 3
  # 0   1   2   3   4   5
] #    column indexes

#len()function call returns the number of elements in the list
len(list2d)   # 4 (number of rows/lists)
len(list2d)-1 # 3 (last row index)


row = 0 #represents the row, in this case the row at index 0 
len(list2d[row])   # 6 number of columns/elements in a given row/list
len(list2d[row])-1 # 5 last column index 
```

## <table><th>Unpacking Collections</th></table>
___

> * Unpacking refers to the process of extracting individual elements from a container (such as a list, tuple, dictionary)
> * Values in a collection can be automatically assigned to variables
> * Use the \* symbol to unpack multiple values into a single variable
>
> * This used with *args and **kwargs, see variable length arguments 

### Unpack Into Variables


```python
list1d = [1,2,3]
a, b, c = list1d
# a = 1
# b = 2
# c = 3

list1d = [1,2,3]
a, b = list1d
# Outputs: ValueError: too many values to unpack (expected 2)
```

### Unpack Mutliple Values Into One Variable With *


```python
# collects multiple values into a single variable
list1d = ["a","b","c","d"]
first, *rest = list1d
# first = a
# rest = [b,c,d]

*start, last = list1d
#start = [a,b,c]
#last = d

l1 = [1,2,3]
l2 = [4,5,6]
print( [*l1,*l2] )# Output: [1,2,3,4,5,6]
```

### Ignore Unpacked Values with ( _ )


```python
list1d = [1,2,3]
_, b, _ = list1d
#b = 2
```

## <table><th>List Comprehension</th></table>
___

A list comprehension is a shorthand way to algorithmically create a list

### 1D List Comprehensions

syntax:

    [element_expression for variable in iterable]
    


```python
list1d = [0 for _ in range(5)]

print(list1d)
# Output: [0, 0, 0, 0, 0]
```


```python
list1d = [ x**2 for x in range(5)] 

print(list1d)
# Output: [0, 1, 4, 9, 16]
```


```python
import random
list1d = [ random.randint(0,100) for _ in range(5)]

print(list1d)
# Output: Varies
```

### 2D List Comprehensions

syntax:

    [[element_expression for variable in iterable] for variable in iterable]


```python
list2d = [[0 for _ in range(5)] for _ in range(5)] 

print(list2d)
# Output: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```


```python
list2d = [[x + y for x in range(5)] for y in range(5)]

print(list2d)
# Output: [[0, 1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]
```


```python
list2d = [[random.randint(0,100) for _ in range(5)] for _ in range(5)]

print(list2d)
# Output: Varies
```

## <table><th>List Iteration: Looping</th></table>
___

It is often necessary to go through the contents of a list item by item. This is called iterating through a list.

There are several ways to iterate through a list.

We will use this list of alphanumeric characters generated using list comprehensions as an example list to iterate through.


```python
alphanumeric = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]
print(alphanumeric)
# Output:
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
#  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
#  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
#  'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
#  'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
#  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
#  'y', 'z']
```

### Looping through the indexes of a list
syntax:

    for index in range(len(list)):
        ...


```python
alphanumeric = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]

#for index in range(len(list)):
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

### Looping through the elements of a list
syntax:

    for element in list:
        ...


```python
alphanumeric = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]

# for element in list:
for char in alphanumeric:
    print(char) #prints each element of alphanumberic

# Output:
# 0
# 1
# 2
# ...
# z
```

### Looping through the elements backwards
syntax:

    for element in reversed(list):
        ...


```python
alphanumeric = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]

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

### Looping through the index and elements at the same time

syntax:

    for index, element in enumerate(list):
        ...


```python
alphanumeric = [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)]

#for index, element in enumerate(list):
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

### Combine values from multiple lists into a tuple
syntax:

    for item1, item2, ... in zip(iter1, iter2, ...):
        ...


```python
num = [x for x in range(1,27)]
upper_alpha = [chr(x) for x in range(65,91)] 
lower_alpha = [chr(x) for x in range(97,123)]

alphabet = []

#for item1, item2,... in zip(iter1,iter2,...)
for number, upper, lower in zip(num, upper_alpha, lower_alpha):
  alphabet.append((number,upper,lower))

# Output: 
# [(1, 'A', 'a'), (2, 'B', 'b'), (3, 'C', 'c'), (4, 'D', 'd'), (5, 'E', 'e'), (6, 'F', 'f'), 
#  (7, 'G', 'g'), (8, 'H', 'h'), (9, 'I', 'i'), (10, 'J', 'j'), (11, 'K', 'k'), (12, 'L', 'l'), 
#  (13, 'M', 'm'), (14, 'N', 'n'), (15, 'O', 'o'), (16, 'P', 'p'), (17, 'Q', 'q'), (18, 'R', 'r'), 
#  (19, 'S', 's'), (20, 'T', 't'), (21, 'U', 'u'), (22, 'V', 'v'), (23, 'W', 'w'), (24, 'X', 'x'), 
#  (25, 'Y', 'y'), (26, 'Z', 'z')]
```
