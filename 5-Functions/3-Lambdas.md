# `Python Lambdas`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

___

Covered in this file:
1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Python Indentation and Code Blocks`](#python-indentation-and-code-blocks)
1. [`Lambda Expressions: Shorthand Functions`](#lambda-expressions-shorthand-functions)
1. [`Lambdas as function templates`](#lambdas-as-function-templates)
1. [`Lambdas can be used to pass a small function as an argument`](#lambdas-can-be-used-to-pass-a-small-function-as-an-argument)
1. [`Lambdas and map()`](#lambdas-and-map)
1. [`Lambdas and filter()`](#lambdas-and-map)
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

### `Abstract vs. Real Examples`
In this file there are two types of examples, `abstract` and `real`. 

`Abstract` examples are a generalized, simplified representation that highlights the core concept or principle without including unnecessary details or specific instances. 

`Real` Examples are specific instances that illustrate the concept, principle, or method by providing concrete details. 

<br>

[Back to Top](#python-lambdas)

___

<br>



# `Python Indentation and Code Blocks`
Python syntax uses `indentation` to define the scope of blocks of code.

`Code blocks` are groups of statements that are executed together as a unit.
> Each indentation level represents a higher level of code structure (conditionals, loops, functions, classes)

> All statements within the same block must have the same level of indentation.

> Indent 4 spaces to create a code block.  

> The end of a block is indicated by the decrease in indentation level. 

*Note*:   
`Scope/Context` is the area of a program in which a block of code exists and executes.

<br>

*Notes:*  
> *`Indentation` is typically achieved using spaces or tabs.* 

> *Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior.*  

> *Python 3 disallows mixing tabs and spaces for indentation in the same source file.* 

> *If you are using an editor like VScode using the tab key, and spaces is not a problem.*

<br>

### `Python Indentation Examples:`
```python
condition = True or False

if(condition):
    #--> start of the if code block (scope/context)
    print("Inside the if statement")                    
                                                        
#<-- end of the if code block (scope/context)
```
```python
condition = True or False

while(condition):
    #--> start of the while code block (scope/context)
    print("Inside the while loop")

#<-- end of the while code block (scope/context)
```
```python
for _ in range(10):
    #--> start of the for code block (scope/context)
    print("Inside the for loop")

#<-- end of the for code block (scope/context)
```
```python
def function():
    #--> start of the function definition code block (scope/context)
    print("Inside of the function definition")

#<-- end of the function definition code block (scope/context)
```
```python
class Example():
    #--> start of the Class definition code block (scope/context)

    def __init__(self):
        #--> start of the Class Constructor Definition code block (scope/context)
        print("Inside the Class, inside the constructor")

    #<-- end of the Class Constructor Definition code block (scope/context)
#<-- end of the Class Definition code block (scope/context)
```

<br>

## `Nested Indentation: Blocks inside of Blocks`
`Indentation` defines the level of the code block when nesting constructs.

*Note*: 
> Most code editors like VS Code will provide a line to help you keep track of the beginning and end of your code blocks

```python
class Example():
    def example_():
        for _ in range(5):
            while(condition):
                if(condition):
                    print("So many indents!")
```
```python
class Example():
    #--> start of class code block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def function():                                                     #
        #--> start of function code block###########################    #
        for _ in range(5):                                         #    #
            #--> start of for code block++++++++++++++++++++++#    #    #
            while(condition):                                 #    #    #
                #--> start of while code block============#   #    #    #      
                if(condition):                            #   #    #    #
                    #--> Start of if code block ------#   #   #    #    #
                    print("So many indents!")         #   #   #    #    #
                #<-- end of if code block-------------#   #   #    #    #
            #<-- end of while code block==================#   #    #    #
        #<-- end of for code block++++++++++++++++++++++++++++#    #    #
    #<-- end of function code block#################################    #
#<-- end of class code block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
```

<br>

[Back to Top](#python-lambdas)

___

<br>


# `Lambda Expressions: Shorthand Functions`
Basically: `Lambdas` are shorthand functions

Specifically: `Lambdas` are small, anonymous functions defined with a single expression used for creating functions on the fly without needing to formally define them using the def keyword.

`Lambda's take any number of arguments, but can only have one expression`

`The result of a lambda expression is automatically returned.`

syntax
```
lambda argument, ... : expression
```
abstract example:
```python
lambda_function = lambda a,b,c : a + b + c 
lambda_function(1,2,3)      # Returns: 6
```

*The PEP 8 style guide for Python states that lambdas should not be assigned to variables, rather they should be defined as functions*
```python
'''Instead of This'''
function = lambda name :  "Hello " + name

'''Do this'''
def function(x): 
    return "Hello " + name
```
This is because defining functions using `lambdas` and then binding them to a variable duplicates the functionality of the `def` statement. 
* This is also ok, because it is not generally, how programmers will use `lambdas`.

<br>

# `Lambdas as function templates`
Lambdas can be used to create function templates with variables that can be applied later. 

 
```python
def returns_lambda(n):
    return lambda a : a ** n        # This function returns a lamda

# Variables are then assigned the lambda by calling the function and passing arguments
squared = returns_lambda(2)         # Returns and Assigns:  lambda a : a ** 2
cubed = returns_lambda(3)           # Returns and Assigns:  lambda a : a ** 3
pow_4 = returns_lambda(4)           # Returns and Assigns:  lambda a : a ** 4

# The variables are now called like any function:
squared(2)                          # Returns: 4
cubed(2)                            # Returns: 8
pow_4(2)                            # Returns: 16
```

<br>


# `Lambdas can be used to pass a small function as an argument`
Lambdas can be use to pass a small function that determines and returns the value to be passed as an argument. 

```python
pairs = [(1, 'one'), (2, 'two'), (4, 'four'), (3, 'three') ]

# list.sort(key=None, reverse=False)
pairs.sort(key=lambda pair: pair[1]) 
# The lambda returns the 2nd element, in this case the words not the numbers.
# This means that 'pairs' will be sorted based on the words


print(pairs)
# Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

# `Lambdas and map()`
`map()` is a built-in function of Python that applies a function to each item of an iterable, and returns a map iterator object (see [iterators.md](../4-Iteration/5-Iterators.md))

Syntax
```
map(func, iter1, ...)
```
```python
numbers = [1, 2, 3, 4, 5]
result = map(lambda x : x * 2, numbers)   # result references the iterator object returned by map()

# Converted to list
print(list(result)) # Output: [2, 4, 6, 8, 10]
```
```python
numbers = [1,2,3,4,5]

#looping through results items
for e in map(lambda x : x * 2, numbers):
    print(e, end = " ")
```

Remember, that `iterators`:
* generate one element at a time
* once an item is returned it cannot be returned again
* once the iterator has returned all values it is 'empty' (ie. cannot be iterated again.)
---

<br>

# `Lambdas and filter()`
`filter()` is a built-in function that filters items of an iterable based on conditions defined in a function, and returns a filter iterable object.


Syntax
```
filter(function, iterable)
```
```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)

# Convert to a list
print(list(result))  # Output: [2, 4, 6]
```

Remember, that `iterators`:
* generate one element at a time
* once an item is returned it cannot be returned again
* once the iterator has returned all values it is 'empty' (ie. cannot be iterated again.)
---

`Removing Falsey values with filter(None, iterable)`
```python
values = [0, 1, None, 2, "", 3, False, 4]
result = filter(None, values)

print(list(result))  # Output: [1, 2, 3, 4]
```

Remember:  
`Truthiness` refers to the evaluation of an object's value in a boolean context, ie. determining whether it is considered true or false.*
* Truthy values are `True`
* Falsey values are `False`

|Data Type| Truthiness|
|:-:|:-:|
|`Integers`, `Floats`|Any non-zero number (integer, float) is evaluated as True|
|`Strings`, `Lists`, `Tuples`, `Sets`, `Dictionaries`|Any non-empty string, list, tuple, set, or dictionary, is evaluated as True|
|`Functions`, `Methods`, `Lambdas`, `Classes`|Any function, method, lambda or class is evaluated as True|
|`Objects`|By default objects are evaluated True, but how an object is evaluated can be changed|

---

<br>

[Back to Top](#python-lambdas)

___

<br>

*Created and maintained by Mr. Merritt*













































