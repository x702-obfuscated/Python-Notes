# `Python Functions`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

___

Covered in this file:
1. Python Indentation and Code Blocks
2. Function Definition
3. Function Calling
4. Returning a value: return 
>   1. Returning multiple values
5. Parameters: function variables
>   1.  Default Parameter values
6. Arguements: parameter values
7. Positional Arguments vs Keyword Arguments
>   1. Unpacking Arguments
>   2. Forcing Keyword Arguments
>   3. Forcing Positional Arguments
8. Arbitrary Argument Lists (*args, **kwargs)
9. Function Scope
10. Builtin Function Calls
11. Lambda Expressions
12. Documentation Strings
13. Function Annotations
14. Function Examples Including Control Structures

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

[Back to Top](#python-functions)

___

<br>

# `Functions Defined`
Basically: A `function` is a block of reusable code that performs a specific task

Specifically: A `function` is a self contained block of code tha performs a specific task and can be reused throughout the program. They contribute to the abstraction, modularity, reusability, and organization of scource code.

> *NOTE: Procedure, Function, Method, Subroutine are terms that are often used interchangeably*

`Functions` are essential to abstracting the complexity of programming.
   
# `Defining a function`
Functions are created by using the keyword `def` and then defining what the function needs and does.
* Functions must be defined before they are called (used).
* Functions must be called to execute its code.
* Functions should be named after the task they are intended to perform  

<br>

basic syntax:
```
def function_name(parameter, ...):
    <Code Block to be Executed>
    ...
```
```python
#Function  Definition--------------------------------#
def function_name(parameter1,parameter2, ... ):      #
  #--> indent into the function definition           #
  ... # What the function does                       #
  return # answer/result of the function             #
#<--unindent to exit the function definition---------#
```

real examples:
```python
def say_hello():
   print("Hello World")

# There is no output, because the function was defined but not called.
```
```python
def count_to(number):
   for num in range(1,number+1):
      print(num, end = " ")

# There is no output, because the function was defined but not called.
```

```python
def sum_list(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

# There is no output, because the function was defined but not called. 
# And the since the function returns, it does not print output.
```

<br>

full abstracted syntax (fully explained throughout this file):
```
def function_name(pos1, pos2, ..., /, pos_or_kwd, *, kwd1, kwd2, ...):
    ...

def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
    ...
```

*NOTE*:  
*Understanding the relationship between function definition and function calling is essential to using functions effectively.* 

`Function definition` is like teaching the computer how to do something. 
> * Just because you know how to do something doesn't mean you automatically do it.  

`Function calling` is like asking the computer to do something it knows how to do.   
  
> * You cannot do something you do not know how to do. 

<br>

# `Function Calling`
Basically: A `function call` is the process of asking the computer to perform a function that has already be defined. 

Specifically: A `function call` is the process of transferring control from the main execution flow to a previously defined function or subroutine. This involves pushing the current state onto the call stack, passing any necessary arguments, executing the function's code, and then resuming execution after the function has completed.

`Functions must be defined before they are called.`

A function is called using the name of the function, and any arguments enclosed in parenthesis

<br>

basic caller syntax:
```
function_name(argument, ...)
```

```python
#General Function Call Syntax
#Variables that store some value
argument1 = ...; argument2 = ... #just examples

#Function Call---------------------------#
function_name(argument1,argument2, ...)  #
#----------------------------------------#
#calling the function and providing values to assign to the parameters.
```

real examples:
```python
def say_hello():                # Function Defintion
    print("Hello World")

def count_to(n):                # Function Definition
    for x in range(1,n+1):
        print(x, end = " ")

def sum_list(nums):             # Function Definition
    sum = 0
    for num in nums:
        sum += num
    return sum


say_hello()                 # Function Call 
count_to(10)                # Function Call
sum_list([1,2,3,4,5])       # Function Call, returns doesn't print

# Output:
# Hello World
# 1 2 3 4 5 6 7 8 9 10
```
```python
def count_to(n):                # Function Definition
    for x in range(1,n+1):
        print(x, end = " ")


num = 5
count_to(num)               #Function Call
# Output: 1 2 3 4 5
```

<br>

## `Returning a value: return`
___
## return
> * The *return* keyword is used to return the result of a function back to its caller
> * All function in Python return *None* (NULL) by default, if no return is defined
> * The value to the right of *return* defines what the function returns
> * Multiple values can be returned using a collection
> * returning does not send output to std.out. (ie it does not print out)
> * When a function returns it immediately ends, skipping any code after the return.

abstract example:
```python
def function_name():        # Function Definition
    return "Hello World"    # Returning exits the function, and sends the result to the caller


function_name()             # Returns: Hello World

print(function_name())      # Output: Hello World

result = function_name()    # assigns the return value to 'result'
```


## Returning multiple values
> * Functions can return multiple values as a tuple or other collection

abstract example:
```python
def return_multiple():
    return "a", "b", "c"                        # multiple return values are seperated with a comma

first, second, third = return_multiple()        # Unpacks and assigns the values

print(first)                                    # Outputs: a
print(second)                                   # Outputs: b
print(third)                                    # Outputs: c
```
    
<br>



## `Parameters: function variables`
___
## Parameters
> * basically: named variables that only exist inside of the function
> * specifically: named variables that are used to pass information into functions, procedures, or methods that act as placeholders for the actual values (called arguments) that will be passed when the function is called.

> * are listed in the parenthesis of a function definition  
> * represent unknown literal values  
> * there can be 0,1 or more parameters seperated by a comma  
> * are assigned a value by arguments when the function is called  
> * are local to the function definition  
> * parameters and function definitions go together    
> * can be assigned default values with =  

syntax:
```
def function_name(parameter1, parameter2, ...):
    ...
```

abstract example:
```python
def has_parameters(parameter_1,parameter_2):    # Function Definition: parameters are defined here                               
    print(parameter_1)                                                              
    print(parameter_2)                                                      


has_parameters("Hello", "World")                # Function Caller: parameters are passed argument values here
# Output: 
# Hello
# World
```

```python
def calc_product(x,y):          # Function Definition: parameters are defined here
    product = x * y
    return product

calc_product(4,3)               # Function Caller: parameters are passed argument values here
```

<br>


## `Default Parameter Values`
___
> * parameters can be given default values using the = operator
> * parameters with a default values can be provided an argument, but do not require one (optional)
> * default values are evaluated when the function is defined.
> * mutable default values are shared between all calls

abstract example:
```python
def has_defaults(p1,p2 = "p2 is defualt",p3 = "p3 is defualt"):    
    return p1,p2,p3

first, second, third = has_defaults("p1 is required", "p2 is optional")

print(first)  # Output: p1 is required
print(second) # Output: p2 is optional
print(third)  # Output: p3 is defualt
```

```python
number = 5
def example(arg = number):  # default values are evaluated when the function is defined.
    print(arg)

number = 6
example() # Output: 5
```

Default values are evaluated when the function is defined
```python
def greet(name, message = "Hello"):
    print(f"{message}, {name}!")

greet("Alice")      # Output: Hello, Alice!
greet("Bob", "Goodbye")        # Output: Goodbye, Bob!
```

Mutable default values are shared between all calls
```python
def add_to_list(value, list1d = []):
    list1d.append(value)
    return list1d


print( add_to_list("Each"))         # ['Each']
print( add_to_list("value"))        # ['Each', 'value']
print( add_to_list("is"))           # ['Each', 'value', 'is']
print( add_to_list("added"))        # ['Each', 'value', 'is', 'added']
print( add_to_list("to"))           # ['Each', 'value', 'is', 'added', 'to']
print( add_to_list("the"))          # ['Each', 'value', 'is', 'added', 'to', 'the']
print( add_to_list("default"))      # ['Each', 'value', 'is', 'added', 'to', 'the', 'default']
print( add_to_list("list."))        # ['Each', 'value', 'is', 'added', 'to', 'the', 'default', 'list.']
```

To avoid the mutable default issue
```python
def add_to_list(value, list1d=None):
    if list1d is None:
        list1d = []
    list1d.append(value)
    return list1d


print( add_to_list("Each"))         # ['Each']
print( add_to_list("value"))        # ['value']
print( add_to_list("is"))           # ['is']
print( add_to_list("added"))        # ['added']
print( add_to_list("to"))           # ['to']
print( add_to_list("the"))          # ['the']
print( add_to_list("default"))      # ['default']
print( add_to_list("list."))        # ['list.']
```

<br>

## `Argument: parameter values`
___
## Arguments
> * basically: the value given to a parameter when a function is called
> * specifically: a specific value or reference that is passed to a function or method when it is called

> * Arguements and Function Calls go together
> * are listed in parenthesis as apart of a function call
> * each argument is seperated with a comma'
> * are required for each parameter without a default value
> * can be a passed a reference from a variable 


abstract example
```python

def accepts_arguments(parameter_1,parameter_2):     # Function Definition with Parameters                           
    print(parameter_1)                                                      
    print(parameter_2)                                                      




#   function_name(argument1,argument2,...)
accepts_arguments("Hello", "World")                 # Function Call with Arguments
# Output:
# Hello
# World
```

real example:
```python
def calc_product(x,y):  # Function Definition with Parameters  
    product = x * y
    return product

calc_product(4,3)       # Function Call with Arguments
# Returns: 12
```

Arguments are required for parameters without a default value
```python
def increment(counter, amount = 1):
    counter += amount


count = 0

increment()
# Error Output:
# Traceback (most recent call last):
#   File "<filepath>, line 7, in <module>
#     increment()
# TypeError: increment() missing 1 required positional argument: 'counter'

increment(count)        # No Error

increment(count, 2)     # No Error
```

<br>

## `Positional Arguments vs Keyword Arguments`
___
## Positional vs Keyword Arguments
> * Positional argument values are assigned based on the order in which the parameters are defined
> * Keyword argument values are assigned based on their association with parameter names

full abstract syntax (fully explained throughout this file):
```
def function_name(pos1, pos2, ..., /, pos_or_kwd, *, kwd1, kwd2, ...):
    ...

def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
    ...
```
<br>

### Positional Arguments
> * Values from arguments are assigned based on the order in which the parameters are defined
* Unpacking Positional Arguments
* Forcing Positional Arguments

abstract example:
```python
#position        1       2      3
def positional(first, second, third):
    print(first)
    print(second)
    print(third)

#postion    1    2    3
positional("a", "b" ,"c")
# Output
# a
# b
# c
```

<br>

Unpacking Positional Arguments
> * The \* character is used to unpack list like iterables as arguments
> * Each argument is assigned based on position
> * This is similar to the *args parameter

abstract example:
```python
def unpack_positional(a,b,c,d,e):
    return [a,b,c,d,e]

arguments = (1,2,3,4,5)
result = unpack_positional(*arguments)  
# The elements of 'arguments' are unpacked to the positional parameters.
# ie. --> a = 1, b = 2, c = 3, d = 4 , e = 5

print(result)       # Output: [1,2,3,4,5]
```

```python
#example
print(list(range(2,9)))     # Output: [2,3,4,5,6,7,8]

nums = [1,10]
print(list(range(*nums)))   # Output: [1,2,3,4,5,6,7,8,9]
#                * unpacks the args list
```

<br>

Forcing Positional Arguments ( / )
> * Use / to force arguments to be assigned by position only
> * Arguments appearing before the / are forced
> * Arguments apperaing after the / are not
> * typically use positional-only if the name of parameters do not matter, or the names should not be available to the user.  

abstract example:
```python
def position_forced(p1,p2,/):
    return p1, p2

position_forced(p2 = "World", p1 = "Hello")
# TypeError: position_forced() got some positional-only arguments passed as keyword arguments: 'p1, p2'
```

### Keyword Arguments
> * Values from arguments are assigned based on their association with parameter names
* Unpacking Keyword Arguments
* Forcing Keyword Arguments

abstract example:
```python
def keyword(name, age, grade, school):
    return f"Hello {name}, you are {age} years old, in grade {grade}, and attend {school}"

# instead of positional assignment
keyword("Sam", 16, 11, "LWM Academy")

# Arguments can be assigned by name, in any order
keyword(grade = 11, name = "Sam", school = "LWM Academy", age = 16)
```

Unpacking Keyword Arguments
> * Keywords from dictionaries can be unpacked using \*\* 
> * Each value is assigned based on the key in the dictionary
> * This is similiar to the **kwargs parameter.

abstract example:
```python
def unpack_keyword(name, age, grad, school):
    return f"Hello {name}, you are {age} years old, you are in {grad} school, and attend {school}"

#Dictionary containing the arguments 
keyword_args = {
    "school": "MIT",
    "name" : "Sam",
    "age" : 20, 
    "grad" : "undergraduate"
}

# The keys from 'keyword_args' map to the parameters in the function call
unpack_keyword(**keyword_args)   
# Returns: Hello Sam, you are 20 years old, you are in undergraduate school, and attend MIT
```

```python
def display_data(name, force = 0, mass = 0 , acceleration = 0):
    print("Hello", name)
    print("The amount of force is" +" ", force)
    print("The mass of the object is" + " ", mass)
    print("The acceleration is" + " ", acceleration)
    
data = {"mass": 2, "acceleration": 5, "name": "Programmer", "force": 10 }

display_data(**data) # The keys from 'data' map to the parameters in the function call
# Output:
# Hello Programmer
# The amount of force is  10 
# The mass of the object is  2
# The acceleration is  5
```


Forcing Keyword Arguments
> * Keyword Arguements are forced with the \* character 
> * Arguments appearing after the * are forced
> * Arguments apperaing before the * are not
> * Typically use keyword-only when the names of parameters have meaning, or you want to prevent users from using positional parameters.


```python
# The * forces name, age, grade, and school to keyword only
def forced_keywords(*,name, age, grade, school):                
    return f"Hello {name}, you are {age} years old, in grade {grade}, and attend {school}"

forced_keywords("Logan",18, 12, "Xavier's School for Gifted Youngsters")
# TypeError: forced_keywords() takes 0 positional arguments but 4 were given
```




Putting it together:

```
           <--Positional Forced              Keyword Forced-->
                              |              |
def function_name(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
                  -----------    ----------     ----------
                    |                |               |
                    |      Positional or Keyword     |
                    |                              Keyword only
              Positional only
```

General Tips:
> * Use positional-only if you want the name of the parameters to not be available to the user. 
>
> * Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.  
>
> * For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future

<br>

## `Arbitrary Arguments Lists: (*args, **kwargs)`
___
> * Using unpacking notation programmers can create variables that accept varying numbers of arguments for the same function
> * Use \* for varying length positional arguments (tuple unpacking)
> * Use \*\* for varying length keyword arguments  (dictionary unpacking)
> * *args, and **kwargs can be used together and accept any number of arguments(including 0)'

full abstract syntax (fully explained throughout this file):
```
def function_name(pos1, pos2, ..., /, pos_or_kwd, *, kwd1, kwd2, ...):
    ...

def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
    ...
```

## *args
> * (pronounced "star-args"), also known as variable-length argument lists
> * allow you to assign a variable number of positional arguments
> * parameters after *args are keyword only
> * *args is not a required name, just a programming convention
> * *args is of type <class 'tuple'>

abstract example:
```python
def arbitrary_arguments(*args):         # Parameters after *args must be keyword
    print(args)

arbitrary_arguments()                   # Output: () 
arbitrary_arguments(1)                  # Output: (1,)
arbitrary_arguments(1,2)                # Output: (1, 2)
arbitrary_arguments(1,2,3)              # Output: (1, 2, 3)
```

```python
def concat(*args, sep = "/"):           # Parameters after *args are keyword only
    return sep.join(args)
```

## **kwargs
> * (pronounced "star-star-kwargs"), also known as variable-length keyword argument lists
> * allow you to assign a variable number of keyword arguments
> * **kwargs is not a required name, just a programming convention
> * **kwars is of type <class 'dict'>

abstract example:
```python
def arbitrary_keywords(**kwargs):       # any positional args must come before **kwargs
    print(kwargs)

arbitrary_keywords()                                                    # {}
arbitrary_keywords(name = "sam")                                        # {'name': 'sam'}
arbitrary_keywords(name = "sam", age = "40")                            # {'name': 'sam', 'age': '40'}
arbitrary_keywords(name = "sam", age = "40", phone = "123-456-7890") 
# {'name': 'sam', 'age': '40', 'phone': '123-456-7890'}
``` 

Putting it all together:
```
                                    Keyword only --> 
                                    |
def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
                                                            |
                              <-- Other Keyword and Postional       
```
`The format above doesn't usually make much practical sense.` `The format below is simpler and more practical.`
```
def function_name(*args, **kwargs):
    ...
```

<br>

## `Function Scope`
___
> * Parameters are local to the function  
> * Variables defined in the function are local to the function  
> * Variables defined outside the function defintion are non local  
> * In order to use variables that are non local to the function use the nonlocal keyword  
> * In order to use variables that are global use the global keyword.   
> * Look out for UnboundLocalErrors (Compile Time)  

abstract example:
```python
text = "I am global"

def example():
    text = "I am local"

example() #function call

print(text)# Output: I am global
#prints the global 'text', not the local 'text'
```

global
```python
text = "I am global"

def example():
    global text #access the global 'text'

    text = "Made a local change"
    # this 'text' is the global 'text'
    

print(text) # Output: I am global

example()   # Changes only occur after the function has been called. 

print(text) # Output: Made a local change
```

nonlocal
```python
text = "I am global"

def outer():
    text = "I am nonlocal to inner"

    def inner():
        nonlocal text
        text ="Changed the nonlocal text"

    inner()

    print(text) #Output: Changed the nonlocal text

outer()

print(text) # Output: I am global
```
```python
x = 'global'

def example():
    print(x) # Output: global 
    # accesses 'x' 1 scope out no problem

example()
```

Unbound Local Errors
```python
x = "global"

def example():
    print(x)                    #UnboundLocalError: local variable 'x' referenced before assignment
    x = "Change global x"

#Python assumes that since you created a local 'x' you ment to print the local 'x' and not the global 'x'
example()  
```

<br>

## `Builtin Function Calls`
___
> * Python has a built-in library of code called the Standard Library.
> * The standard library has pre-defined (builtin) functions that you can automatically access in your programs.

builtins you may have already used
```python
print()
input() 
range() 
len()
float()
int()
str()
type()
```
> Notice that when you use these you are just calling the function, you do not need to define it.  
> This is because the Standard Library defines these functions for you. 

The following is a list of builtin function calls in provided by the Python Standard Library:
```python
abs()           # Returns the absolute value of a number.
aiter()         # Returns an iterator object.
all()           # Returns True if all elements of an iterable are true.
anext()         # Retrieves the next item from an iterator.
any()           # Returns True if any element of an iterable is true.
ascii()         # Returns a string containing a printable representation of an object.
bin()           # Converts an integer to a binary string.
bool()          # Returns the boolean value of an object.
breakpoint()    # Enters the debugger at the specified line.
bytearray()     # Returns a new array of bytes.
bytes()         # Returns an immutable bytes object.
callable()      # Returns True if the object appears callable.
chr()           # Returns the string representing a character whose Unicode code point is the integer.
classmethod()   # Returns a class method for the given function.
compile()       # Compiles the source into a code or AST object.
complex()       # Returns a complex number with the value real + imag*1j.
copyright()     # Prints the copyright statement.
credits()       # Prints the list of contributors.
delattr()       # Deletes the attribute of an object.
dict()          # Returns a new dictionary object.
dir()           # Returns the list of names in the current local scope or namespace.
divmod()        # Returns the quotient and remainder of the division of two numbers.
enumerate()     # Returns an enumerate object.
eval()          # Evaluates the specified expression.
exec()          # Executes the specified dynamically created code.
exit()          # Exits the Python interpreter.
filter()        # Constructs an iterator from elements of an iterable for which a function returns true.
float()         # Returns a floating-point number constructed from a number or string.
format()        # Formats a specified value.
frozenset()     # Returns a new frozenset object.
getattr()       # Returns the value of the specified attribute of an object.
globals()       # Returns the current global symbol table as a dictionary.
hasattr()       # Returns True if the object has the specified attribute.
hash()          # Returns the hash value of an object.
help()          # Invokes the built-in help system.
hex()           # Converts an integer to a hexadecimal string.
id()            # Returns the identity of an object.
input()         # Reads a line from input, converts it to a string, and returns it.
int()           # Returns an integer object.
isinstance()    # Returns True if the specified object is an instance of the specified class.
issubclass()    # Returns True if the specified class is a subclass of another class.
iter()          # Returns an iterator object.
len()           # Returns the length (the number of items) of an object.
license()       # Prints the Python Software Foundation License.
list()          # Returns a list.
locals()        # Returns the current local symbol table as a dictionary.
map()           # Applies a function to all items in an input iterable.
max()           # Returns the largest item in an iterable or the largest of two or more arguments.
memoryview()    # Returns a memory view object.
min()           # Returns the smallest item in an iterable or the smallest of two or more arguments.
next()          # Retrieves the next item from an iterator.
object()        # Returns a new featureless object.
oct()           # Converts an integer to an octal string.
open()          # Opens a file and returns a corresponding file object.
ord()           # Returns an integer representing the Unicode character.
pow()           # Returns x to the power of y.
print()         # Prints objects to the text stream file.
property()      # Returns a property attribute.
quit()          # Exits the Python interpreter.
range()         # Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
repr()          # Returns a string containing a printable representation of an object.
reversed()      # Returns a reverse iterator.
round()         # Returns the rounded value of a number to the specified number of decimals.
set()           # Returns a new set object.
setattr()       # Sets the value of the specified attribute of an object.
slice()         # Returns a slice object.
sorted()        # Returns a sorted list from the specified iterable.
staticmethod()  # Returns a static method for the specified function.
str()           # Returns a string object.
sum()           # Sums the items of an iterable.
super(None)     # Returns a proxy object that delegates method calls to a parent or sibling class.
tuple()         # Returns a tuple.
type()          # Returns the type of an object.
vars()          # Returns the __dict__ attribute of the given object.
zip()           # Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
```
> For more pre-defined functions programmers will look for code libraries.  
> Libraries are just how they sound, they store code for a specific function. 

<br>

## `Lambda Expressions: Shorthand Functions`
___
## Lambda Functions
> * basically: shorthand functions
> * specifically: small, anonymous functions defined with a single expression used for creating functions on the fly without needing to formally define them using the def keyword.

> * Lambda's take any number of arguments, but can only have one expression
> * The result of a lambda expression is automatically returned.

syntax
```
lambda argument, ... : expression
```
abstract example:
```python
lambda_function = lambda a,b,c : a + b + c 
lambda_function(1,2,3)      # Returns: 6
```

Creating a function template with lambda
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


lambdas can be used to pass a small function as an arguement
```python
pairs = [(1, 'one'), (2, 'two'), (4, 'four'), (3, 'three') ]

# list.sort(key=None, reverse=False)
pairs.sort(key=lambda pair: pair[1]) 
# The lambda returns the 2nd element, in this case the words not the numbers.
# This means that 'pairs' will be sorted based on the words


print(pairs)
# Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

<br>

## `Documentation: doc strings`
## docstrings
> * (short for documentation strings) in Python are a type of comment used to explain the purpose and usage of a function, class, method, or module.

> * docstrings use triple quotes *'''* or *"""*  
> * docstrings are typically the first statement within a function, class, or module.  
> * The first line should always be a short, concise summary of the object’s purpose.  
>   * For brevity, it should not explicitly state the object’s name or type, since these are available by other means (except if the name happens to be a verb describing a function’s operation).  
>   * This line should begin with a capital letter and end with a period.  
> 
> * If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.  
>
> * The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc. 
> 
> * docstrings can be accessed programmatically using the \_\_doc\_\_ attribute 

```python
def multi_line_docstring():
    """ This line is a summary of the function.

    The above line should be blank. The rest describes the
    calling conventions, side effects, and etc."""
    pass
    
#The dunder attribute __doc__ returns the docstring of a function
print(multi_line_docstring.__doc__)
```

abstract examples:
Function
```python
def add(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of a and b.

    Example:
    >>> add(2, 3)
    5
    """
    return a + b
```
Class
```python
class Dog:
    """
    A class to represent a dog.

    Attributes:
    name (str): The name of the dog.
    age (int): The age of the dog.

    Methods:
    bark(): Prints a bark sound.
    """

    def __init__(self, name, age):
        """
        Constructs all the necessary attributes for the dog object.

        Parameters:
        name (str): The name of the dog.
        age (int): The age of the dog.
        """
        self.name = name
        self.age = age

    def bark(self):
        """
        Prints a bark sound.
        """
        print("Woof!")
```
Module
```python
"""
This module provides basic arithmetic operations.

Functions:
- add(a, b): Returns the sum of a and b.
- subtract(a, b): Returns the difference of a and b.
"""

def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b

# access docstrings with __doc__
print(add.__doc__)
print(subtract.__doc__)
```

<br>

## `Function Annotations`
## Function Annotations
> * basically:  are a way to document/ provide type hints
> * specifically: a way of attaching metadata to the parameters of a function and its return value. 

syntax:
```
def function(parameter: type) -> return_type:
    ...
```

real examples:
```python
def sum_ints(a: int, b: int) -> int:
    return a + b
#expects integer arguments, integer return
```
```python
def sum_floats(x:float, y:float) -> float:
    return x + y
#expects float arguments, float return
```
```python
def sum_list(list1d: list[int]) -> int:
    total = 0
    for elem in list1d:
        total += elem

    return total
#expects float arguments, float return
```
```python
def sum_dict(dict1d: dict[str, int]) -> int:
    total = 0
    for key in dict1d:
        total += dict1d[key]

    return total

#expects a dictionary argument with str keys and int values, returns int
```

## `Function Examples Including Conditionals, While Loops, and For Loops`
> functions can include all kinds of different code
> Conditionals, While Loops, and For loops can all be used inside of functions.

```python
def add(a,b):
    answer = a + b
    return answer

def calc_velocity(distance, time):
    velocity = distance / time
    return velocity

def calc_slope(x1,y1,x2,y2):
    slope = ((y2-y1)/(x2-x1))
    return slope

def get_quadratic(x, a, b):
    #where (x + a) (x + b) == x**2 + (a+b)x + ab
    #where x is a string
    return f"{x}^2 + {a+b}x + {a*b}"

print(get_quadratic("x",3,4))
```
```python
def even_or_odd(num):
    if(num % 2 == 0):
        print("num is even")
    else:
        print("num is odd")

#calls
even_or_odd(1)
even_or_odd(2)
even_or_odd(3)
even_or_odd(4)
```
```python
def count_up(start, stop, step):
    count = start
    while (count <= stop):
        print(count, end= " ")
        count += step
    print()

#calls
count_up(1,10,1)
count_up(50,100,10)
count_up(0,24,8)
count_up(5,500,5)
count_up(40,60,2)
``` 
```python
def count_for(start, stop, step):
    for count in range(start, stop, step):
        print(count, end = " ")
    print()

#calls
count_for(0,-36,-1)
count_for(10,21,2)
count_for(-10,-6,1)
count_for(-5,16,5)
```
```python
def count_vowels(sentence):
    vowels = "aeiou"
    vowel_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
    
    return vowel_count

print(count_vowels("The quick brown fox jumps over the lazy dog."))
```

```python
def get_sum(alist):
    total = 0
    for num in alist:
        total = total + num 
        #total += num
    return total

list1d = [1,2,3,4,5,6,7,8,9]
print(get_sum(list1d))
```
```python
def get_max(alist):
    max_num = alist[0]
    for num in alist:
        if num > max_num:
            max_num = num
    return max_num

list1d = [0,5,2,20,8,6,1,10,19]
print(get_max(list1d))
```
```python
def count_vowels(alist):
    count = 0
    vowels = "aeiou"
    for elem in alist:
        if elem in vowels:
            count +=1
    return count

letters = ["a","b","c","d","e"]
print(count_vowels(letters))
```

<br>

[Back to Top]()

___

*Created and maintained by Mr. Merritt*













































