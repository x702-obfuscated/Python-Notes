# `Python Functions`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

___

Covered in this file:
1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Python Indentation and Code Blocks`](#python-indentation-and-code-blocks)
1. [`Functions Defined`](#functions-defined)
1. [`def Defining a function`](#def-defining-a-function)
1. [`Function Calling`](#function-calling)
    1. [`What happens when a function is called`](#what-happens-when-a-function-is-called)
1. [`Definition vs Calling`](#definition-vs-calling)
1. [`return Return a value`](#return-returning-a-value)
1. [`Returning multiple values`](#returning-multiple-values)
1. [`Parameter are function variables`](#parameters-are-function-variables)
    1. [`Default Parameter Values`](#default-parameter-values)
1. [`Arguments are values given to parameters`](#arguments-are-values-given-to-parameters)
1. [`Positional Parameters vs Keyword Parameters`](#positional-parameters-vs-keyword-parameters)
1. [`Positional Parameters and Arguments`](#positional-parameters-and-arguments)
    1. [`Unpacking Postional Arguments`](#unpacking-positional-arguments)
    1. [`Forcing Postional Arguments`](#forcing-positional-arguments)
1. [`Keyword Parameters and Arguments`](#keyword-parameters-and-arguments)
    1. [`Unpacking Keyword Arguments`](#unpacking-keyword-arguments)
    1. [`Forcing Keyword Arguments`](#forcing-keyword-arguments)
1. [`Putting it together Postional and Keyword`](#putting-it-together-positional-and-keyword)
1. [`Arbitrary Arguments Lists: (*args, **kwargs)`](#arbitrary-arguments-lists-args-kwargs)
    1. [`*args`](#args)
    1. [`**kwargs`](#kwargs)
1. [`Putting it all together *args and **kwargs`](#putting-it-all-together-args-and-kwargs)
1. [`Variable Scope and Functions`](#variable-scope-and-functions)
1. [`Builtin Function Calls`](#builtin-function-calls)
    1. [`The built-in help() function`](#the-built-in-help-function)
1. [`Lambda Expressions: Shorthand Functions`](#lambda-expressions-shorthand-functions)
    1. [`Lambdas as function templates`](#lambdas-as-function-templates)
    1. [`Lambdas can be used to pass a small function as an argument`](#lambdas-can-be-used-to-pass-a-small-function-as-an-argument)
1. [`Documentation: doc strings`](#documentation-doc-strings)
1. [`Function Annotations`](#function-annotations)
1. [`Some Function Examples`](#some-function-examples)

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

<br>

Some Vocabulary Related to Functions:

`Function Name`: identifier given to the function definition.

<br>

`Function Header`: the first line of a function definition, that indicates a function is being defined and includes the `def` keyword, function name, parenthesis `()`, parameters(optional), and a colon `:`.
```
def function_name(parameter, ...):
```
```python
def say_message(message):
```

<br>

`Function Body`: the block of code that is indented under the function header.

```
def function_name(parameter, ...):
    <function body>
```
```python
def say_message(message):
    print(message)
```

<br>

`Function Call (caller)`: how you execute or `invoke` a function using its name, parenthesis, and arguments.
```
function_name(argument, ...)
```
```python
say_message("Functions are fun")
```

<br>

[Back to Top](#python-functions)

___

<br>
   
# `def Defining a function`
Functions are created by using the keyword `def` and then defining what the function needs and does.
* `Functions must be defined before they are called (used).`
* `Functions must be called to execute its code.`
* `Functions should be named after the task they are intended to perform`  

<br>

simple function definition syntax:
```
def function_name():
    <Code Block to be Executed>
    ...
```
```python
def function_name():# Function Header
    #--> Indent to enter the function definition
    ...
#<-- unindent to exit the function definition
```          
example:
```python
def say_hello():
    print("Hello World!")

# There is no output, because the function was defined but not called.
```
```python
def countdown():
    for i in range(3, 0, -1):
        print(i)
    print("Go!")

# There is no output, because the function was defined but not called.
```
```python
def display_menu():
    print("1. Start Game")
    print("2. Load Game")
    print("3. Exit")

# There is no output, because the function was defined but not called.
```

<br>

general function definition syntax:
```
def function_name(parameter, ...):
    ...
    return <value>
```
> `parameters` are optional  
> `return` is optional

example:
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
# And because the function returns, it does not print output. 
```
```python
def light_switch(switch, color):
    if(switch):
        print("The light is ON", color)
    else:
        print("The light is OFF")

# There is no output, because the function was defined but not called. 
```

<br>

There are alot more concepts to cover in functions. Below is the full abstracted function definition syntax that we will fully cover throughout this file. 
```
def function_name(pos1, pos2, ..., /, pos_or_kwd, *, kwd1, kwd2, ...):
    <function body>
    ...
```
```
def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
    <function body>
    ...
```

<br>

[Back to Top](#python-functions)

___

<br>

# `Function Calling`
Basically: A `function call` is the process of asking the computer to perform a function that has already be defined. 

Specifically: A `function call` is the process of transferring control from the main execution flow to a previously defined function or subroutine. This involves pushing the current state onto the call stack, passing any necessary arguments, executing the function's code, and then resuming execution after the function has completed.

<br>

A function is called using a `caller` it includes the function name, and any arguments enclosed in parenthesis . 

`Functions must be defined before they are called.`

<br>

simple caller syntax:
```
function_name()
```
example:
```python
say_hello()
```
```python
count_down()
```
```python
display_menu()
```

<br>

general caller syntax:
> a function call includes one Argument for each parameter in the function definition. 
```
function_name(argument, ...)
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

## `What happens when a function is called`
When a function is called a new stack frame is created on the call stack to keep track of the function's execution context (parameters, variables, return address). If arguments are passed they are assigned to the function's parameters. The function's body is then executed line by line. When a new function is called a new frame is added to the call stack. If there is a return value, that value is returned to the return address of the caller(where the function was called). The program then continues execution from the point after the call. 

<br>

[Back to Top](#python-functions)

___

<br>


# `Definition vs Calling`
Understanding the relationship between `function definition` and `function calling` is essential to using functions effectively.

`Function definition` is like teaching the computer how to do something. 
> * Just because you know how to do something doesn't mean you automatically do it.  

`Function calling` is like asking the computer to do something it knows how to do.   
  
> * You cannot do something you do not know how to do. 

For example:

`Function Definition:`  
Do you know how to count? Probably yes, but how do you know how to count? Someone probably defined (taught) how to count to you. Now in python:
```python
def count_to(number):
    for n in range(number):
        print(n+1, end = " ")
```
<br>

`Function Call:`  
Are you currently counting? Most likely no, but if I asked you to count would you be able too? Would it help if I gave you a number to count to? 

Count to 10. (function call with an argument)

Now in python:
```python
count_to(10)

#Output: 1 2 3 4 5 6 7 8 9 10
``` 

<br>

[Back to Top](#python-functions)

___

<br>

# `return Returning a value`
___
The `return` keyword is used to return the result of a function back to its caller.
* The value to the right of `return` defines what the function returns
* Multiple values can be returned using a collection
* returning does not send output to std.out. (ie it does not print out)

<br>

abstract example:
```python
def function_name():        # Function Definition
    return "Hello World"    # Returning exits the function, and sends the result to the caller


function_name()             # Returns: Hello World

print(function_name())      # Output: Hello World

result = function_name()    # assigns the return value to 'result'
```
real example:
```python
def is_even(num):
    return num % 2 == 0

is_even(5) # Returns: False
is_even(6) # Returns: True

```

<br>

`When a function returns it immediately ends the function, skipping any code after the return.`
```python
def light_switch(switch):
    if(switch):
        return "ON"
        # if this return executes then the function ends here.

    print("The switch is OFF")
    return "OFF"
```

<br>

`If no return is defined, 'None' is returned by default.`
```python
def slope(m,x,b):
    y = m*x + b

print(slope(2,3,4)) # Output: None
```

<br>

[Back to Top](#python-functions)

___

<br>

# `Returning multiple values`
Functions can return multiple values as a tuple or other collection

abstract example:
```python
def return_multiple():
    return "a", "b", "c"                        # multiple return values are seperated with a comma

first, second, third = return_multiple()        # Unpacks and assigns the values

print(first)                                    # Outputs: a
print(second)                                   # Outputs: b
print(third)                                    # Outputs: c
```
real example:
```python
def calculate(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b

    if(b != 0):
        quotient = a / b 
    else:
        quotient = "undefined"

    return sum_result, difference, product, quotient


sum_total, diff, prod, quot = calculate(10, 5) #Unpack and assign

#OR assign a single value with subscript notation [index]

sum_total = calculate(10,5)[0]

print(sum_total, diff, prod, quot)
```   
<br>



# `Parameters are function variables`
Basically: `Parameters` aka formal parameters are named variables that only exist inside of the function

Specifically: `Parameters` aka formal formal parameters are  named variables that are used to pass information into functions, procedures, or methods that act as placeholders for the actual values (called arguments) that will be passed when the function is called.

<br>

`Parameters and function definitions go together`

<br>

`Parameters`:
* are listed in the parenthesis `()` of a function definition  
* represent unknown literal values  
* there can be 0,1 or more parameters seperated by a comma  
* are assigned a value by arguments when the function is called  
* are local to the function definition     
* can be assigned default values with `=`  

<br>

syntax:
```
def function_name(parameter1, parameter2, ...):
    ...
```
```python
def function_name(parameter1,parameter2, ... ):      
  #--> indent into the function definition           
  ...                                                
#<--unindent to exit the function definition
```

abstract example:
```python
# Function Definition: parameters are defined here
def has_parameters(parameter_1,parameter_2):                                   
    print(parameter_1)                                                              
    print(parameter_2)                                                      

# Function Caller: parameters are passed argument values here
has_parameters("Hello", "World")        
# Output: 
# Hello
# World
```

real example:
```python
# Function Definition: parameters are defined here
def calc_product(x,y):  
    product = x * y
    return product


# Function Caller: parameters are passed argument values
calc_product(4,3)        here
```

<br>

[Back to Top](#python-functions)

___

<br>




## `Default Parameter Values`
When defining a function, parameters can be given default values using the `=` operator
* parameters with a default values can be provided an argument when calling the function, but do not require one (optional)
* default values are evaluated when the function is defined.
* mutable default values are shared between all calls

syntax:
```
def function_name(parameter = default_value):
    ...
```
abstract example:
```python
def has_defaults(p1,p2 = "p2 is default",p3 = "p3 is default"):    
    return p1,p2,p3

first, second, third = has_defaults("p1 is required", "p2 is optional")

print(first)  # Output: p1 is required
print(second) # Output: p2 is optional
print(third)  # Output: p3 is default
```

<br>

`Default values are evaluated when the function is defined`
```python
number = 5
def example(param = number):    # default values are evaluated when the function is defined.
    print(param)

number = 6
example()                       # Output: 5
```


```python
def greet(name, message = "Hello"):
    print(f"{message}, {name}!")

greet("Alice")                  # Output: Hello, Alice!
greet("Bob", "Goodbye")         # Output: Goodbye, Bob!
```

<br>

`Mutable default values are shared between all calls`
```python
def add_to_list(value, list1d = []):
    list1d.append(value)
    return list1d


print(add_to_list("Each"))         # list1d = ['Each']
print(add_to_list("value"))        # list1d = ['Each', 'value']
print(add_to_list("is"))           # list1d = ['Each', 'value', 'is']
print(add_to_list("added"))        # list1d = ['Each', 'value', 'is', 'added']
print(add_to_list("to"))           # list1d = ['Each', 'value', 'is', 'added', 'to']
print(add_to_list("the"))          # list1d = ['Each', 'value', 'is', 'added', 'to', 'the']
print(add_to_list("default"))      # list1d = ['Each', 'value', 'is', 'added', 'to', 'the', 'default']
print(add_to_list("list."))        # list1d = ['Each', 'value', 'is', 'added', 'to', 'the', 'default', 'list.']
```

`To avoid the mutable default issue use 'None' instead of an empty value`
```python
def add_to_list(value, list1d=None):
    if list1d is None:
        list1d = []
    list1d.append(value)
    return list1d


print( add_to_list("Each"))         # list1d = ['Each']
print( add_to_list("value"))        # list1d = ['value']
print( add_to_list("is"))           # list1d = ['is']
print( add_to_list("added"))        # list1d = ['added']
print( add_to_list("to"))           # list1d = ['to']
print( add_to_list("the"))          # list1d = ['the']
print( add_to_list("default"))      # list1d = ['default']
print( add_to_list("list."))        # list1d = ['list.']
```

<br>

[Back to Top](#python-functions)

___

<br>

# `Arguments are values given to parameters`
___
Basically: `Arguments` are the values given (passed) to a parameter when a function is called.

Specifically: `Arguments` are a specific value or reference that is passed to a function or method when it is called.

<br>

`Arguments and Function Calls go together`

<br>

Arguments
* are listed in parenthesis `()` as apart of a function call
* each argument is seperated with a comma'
* are required for each parameter without a default value
* can be a passed as reference from a variable 

<br>

syntax:
```
function_name(argument1, argument2, ...)
```
abstract example
```python
def accepts_arguments(parameter_1,parameter_2):     # Function Definition with Parameters                           
    print(parameter_1)                                                      
    print(parameter_2)                                                      


# function_name(argument1,argument2,...)
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

<br>

`Arguments are required for parameters without a default value`
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

[Back to Top](#python-functions)

___

<br>

# `Positional Parameters vs Keyword Parameters`
`Positional Parameter` are assigned argument values based on the order in which the parameters are defined

`Keyword Parameters` are assigned argument values based on the name of the parameter. 

<br>


full abstract syntax (fully explained throughout this file):
```
def function_name(pos1, pos2, ..., /, pos_or_kwd, *, kwd1, kwd2, ...):
    ...

def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
    ...
```

<br>

[Back to Top](#python-functions)

___

<br>


# `Positional Parameters and Arguments`
Values from arguments are assigned to `postional parameters` based on the order in which the parameters are defined.

abstract example:
```python
#position        1       2      3
def positional(first, second, third):
    print(first)
    print(second)
    print(third)

#postion    1    2    3
positional("a", "b" ,"c")   #(first = "a", second = "b", third = "c")
# Output
# a
# b
# c
```

<br>


## `Unpacking Positional Arguments`
* The `*` character is used to unpack list like iterables as arguments
* Each argument is assigned based on position
* This is similar to the `*args` parameter

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

## `Forcing Positional Arguments`
Use `/` to force arguments to be assigned by position only
* Arguments appearing before the `/` are forced
* Arguments appearing after the `/` are not

<br>

*Typically it is best to use positional-only arguments if the name of parameters do not matter, or the names should not be available to the user.*  

<br>

abstract example:
```python
def position_forced(p1,p2,/):
    return p1, p2

position_forced(p2 = "World", p1 = "Hello")
# TypeError: position_forced() got some positional-only arguments passed as keyword arguments: 'p1, p2'
```

<br>

[Back to Top](#python-functions)

___

<br>


# `Keyword Parameters and Arguments`
Values from arguments are assigned based on their association with `keyword parameter` names

abstract example:
```python
def keyword(name, age, grade, school):
    return f"Hello {name}, you are {age} years old, in grade {grade}, and attend {school}"

# instead of positional assignment
keyword("Sam", 16, 11, "LWM Academy")

# Arguments can be assigned by name, in any order
keyword(grade = 11, name = "Sam", school = "LWM Academy", age = 16)
```

<br>

## `Unpacking Keyword Arguments`
Keyword arugments can be unpack from dictionaries using `**` 
* Each value is assigned based on the key in the dictionary
* This is similiar to the `**kwargs` parameter.

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

<br>


## `Forcing Keyword Arguments`
Keyword Arguments are forced with the `*` character in the function header.
* Arguments appearing after the `*` are forced
* Arguments apperaing before the `*` are not

<br>

*Typically it is best to use keyword-only when the names of parameters have meaning, or you want to prevent users from using positional parameters.*

abstract example:
```python
# The * forces name, age, grade, and school to keyword only
def forced_keywords(*,name, age, grade, school):                
    return f"Hello {name}, you are {age} years old, in grade {grade}, and attend {school}"

forced_keywords("Logan",18, 12, "Xavier's School for Gifted Youngsters")
# TypeError: forced_keywords() takes 0 positional arguments but 4 were given
```

<br>

[Back to Top](#python-functions)

___

<br>

# `Putting it together Positional and Keyword` 
abstract syntax diagram:

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
*This diagram illustrates the different types of parameters you can define in a Python function. The parameters to the left of the `/` (like `pos1` and `pos2`) are positional-only, meaning they must be provided in the correct order when calling the function and cannot be specified by keyword. The parameters between `/` and `*` (like `pos_or_kwd`) can be provided either positionally or as keyword arguments. Finally, the parameters to the right of the `*` (like `kwd1` and `kwd2`) are keyword-only, meaning they must be explicitly provided by keyword during the function call, not positionally. This function signature allows for precise control over how arguments are passed, ensuring clarity and flexibility in how the function can be used.*

<br>

`General Tips`:
* Use positional-only if you want the name of the parameters to not be available to the user.  

* Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.  

* For an application programming interface `API`, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future

<br>

[Back to Top](#python-functions)

___

<br>

# `Arbitrary Arguments Lists: (*args, **kwargs)`
Using unpacking notation programmers can create variables that accept varying numbers of arguments for the same function

* Use `*` for varying length positional arguments (tuple unpacking). 

* Use `**` for varying length keyword arguments  (dictionary unpacking)

*It is convention in python to use `*args` for variable length positional arguments and `**kwargs` for variable length keyword arguments.* 


<br>


`*args, and **kwargs can be used together and can accept any number of arguments(including 0)`

abstract syntax 
```
def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
    ...             
```
example:
```python
def display_info(*args, **kwargs):
    print("Positional arguments (*args):")
    for arg in args:
        print(arg)
    
    print("\nKeyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(1, 2, 3, name="Alice", age=30, location="New York")
# Output:
# Positional arguments (*args):
# 1
# 2
# 3

# Keyword arguments (**kwargs):
# name: Alice
# age: 30
# location: New York
```

<br>

## `*args`
`*args`(pronounced "star-args"), also known as variable-length argument lists, collects all positional arguments passed to the function into a tuple.

* `*` allows you to assign a variable number of positional arguments
* parameters after `*args` are keyword only
* `*args` is not a required name, just a programming convention
* `*args` is of type <class 'tuple'>

syntax:
```
def function_name(*args):
    ...
```
abstract example:
```python
def arbitrary_arguments(*args):         # Parameters after *args must be keyword
    print(args)

arbitrary_arguments()                   # Output: () 
arbitrary_arguments(1)                  # Output: (1,)
arbitrary_arguments(1,2)                # Output: (1, 2)
arbitrary_arguments(1,2,3)              # Output: (1, 2, 3)
```
real example:
```python
def concat(*args, sep = "/"):  # Parameters after *args are keyword only
    return sep.join(args)

print(concat("","home","$USER","Desktop"))
# Output:
# /home/$USER/Desktop
```

<br>

## `**kwargs`
`**kwargs` (pronounced "star-star-kwargs"), also known as variable-length keyword argument lists, collects all keyword arguments passed to the function into a dictionary.

* `**` allow you to assign a variable number of keyword arguments
* `**kwargs` is not a required name, just a programming convention
* `**kwargs` is of type <class 'dict'>

syntax:
```
def function_name(**kwargs):
    ...
```

abstract example:
```python
def arbitrary_keywords(**kwargs):       # any positional args must come before **kwargs
    print(kwargs)

arbitrary_keywords()                                                    
# Output: {}

arbitrary_keywords(name = "sam")                                        
# Output: {'name': 'sam'}

arbitrary_keywords(name = "sam", age = "40")                            
# Output: {'name': 'sam', 'age': '40'}

arbitrary_keywords(name = "sam", age = "40", phone = "123-456-7890") 
# {'name': 'sam', 'age': '40', 'phone': '123-456-7890'}
``` 
real example:
```python
def greet_user(**kwargs):
    if 'name' in kwargs and 'age' in kwargs:
        print(f"Hello {kwargs['name']}, you are {kwargs['age']} years old.")
    elif 'name' in kwargs:
        print(f"Hello {kwargs['name']}!")
    else:
        print("Hello, guest!")

# Example usage:
greet_user(name="Zula", age=25)
# Output: Hello Zula, you are 25 years old.


greet_user(name="Blake")
# Output: Hello Blake!

greet_user()
# Output: Hello, quest!
```

<br>

[Back to Top](#python-functions)

___

<br>

# `Putting it all together *args and **kwargs` 
```
                                    Keyword only --> 
                                    |
def function_name(pos1, pos2, ..., *args, kwd1, kwd2, ..., **kwargs):
                                                            |
                              <-- Other Keyword and Postional       
```
*This diagram illustrates a Python function signature that uses a mix of positional arguments, `*args`, keyword-only arguments, and `**kwargs`. The parameters before `*args` (like `pos1`, `pos2`, etc.) can be passed as positional arguments, meaning they are provided in the exact order during the function call. The `*args` collects any additional positional arguments into a tuple. After `*args`, the parameters like `kwd1` and `kwd2` are keyword-only arguments, meaning they must be specified by name when calling the function. Finally, `**kwargs` captures any additional keyword arguments in the form of a dictionary. This function design allows for flexibility, accepting a variable number of both positional and keyword arguments, while ensuring certain arguments must be passed by keyword.*

`The format above doesn't usually make much practical sense.` 

<br>

`The format below is simpler and more practical.`
```
def function_name(*args, **kwargs):
    ...
```

<br>

[Back to Top](#python-functions)

___

<br>

# `Variable Scope and Functions`
Basically: `Scope/Context` is the area within code in which a variable can be accessed and used.  

Specifically: `Scope/Context` refers to the visibility and accessibility of variables, functions, and other identifiers within a program.

* `Parameters are always local to the function.`  
* `Variables defined in the function are local to the function`  
* Variables defined outside the function defintion are non local  
* In order to use variables that are non local to the function use the `nonlocal` keyword  
* In order to use variables that are global use the `global` keyword.   
* Watch out for `UnboundLocalErrors (Compile Time)` 

<br>

abstract example:
```python
text = "I am global"

def example():
    text = "I am local"

example() #function call

print(text)# Output: I am global
#prints the global 'text', not the local 'text'
```

`global` usage
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

`nonlocal` usage
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
`accessing 1 scope up`
```python
x = 'global'

def example():
    print(x) 
    # accesses 'x' 1 scope out no problem

example() # Output: global 
```

`Unbound Local Errors`
```python
x = "global"

def example():
    print(x)      #UnboundLocalError: local variable 'x' referenced before assignment
    x = "Change global x"


example()  

#Python assumes that since you created a local 'x' 
# you ment to print the local 'x' and not the global 'x'.
# Even though you created the local `x` after the print() statement
```

<br>

# `Builtin Function Calls`
Python, like most programming languages,  has a built-in library of code called the `Python Standard Library`.

The standard library has pre-defined (`builtin`) functions that you can automatically access in your programs.

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

*Notice that when you use these you are just calling the function, you did not need to define it first.*

`This is because the Standard Library defines these functions for you. `

<br>

The following is a list of builtin function calls provided by the `Python Standard Library`:
| Function| Description|
|:-:|:-|
| `abs()` | Returns the absolute value of a number.|
| `aiter()`| Returns an iterator object.|
| `all()` | Returns True if all elements of an iterable are true. |
| `anext()`| Retrieves the next item from an iterator.|
| `any()` | Returns True if any element of an iterable is true.|
| `ascii()`| Returns a string containing a printable representation of an object. |
| `bin()` | Converts an integer to a binary string.|
| `bool()`| Returns the boolean value of an object.|
| `breakpoint()`| Enters the debugger at the specified line.|
| `bytearray()`| Returns a new array of bytes.|
| `bytes()`| Returns an immutable bytes object.|
| `callable()` | Returns True if the object appears callable.|
| `chr()` | Returns the string representing a character whose Unicode code point is the integer. |
| `classmethod()` | Returns a class method for the given function.|
| `compile()`| Compiles the source into a code or AST object.|
| `complex()`| Returns a complex number with the value real + imag*1j. |
| `copyright()`| Prints the copyright statement.|
| `credits()`| Prints the list of contributors.|
| `delattr()`| Deletes the attribute of an object. |
| `dict()`| Returns a new dictionary object.|
| `dir()` | Returns the list of names in the current local scope or namespace.|
| `divmod()` | Returns the quotient and remainder of the division of two numbers.|
| `enumerate()`| Returns an enumerate object. |
| `eval()`| Evaluates the specified expression. |
| `exec()`| Executes the specified dynamically created code. |
| `exit()`| Exits the Python interpreter.|
| `filter()` | Constructs an iterator from elements of an iterable for which a function returns true. |
| `float()`| Returns a floating-point number constructed from a number or string. |
| `format()` | Formats a specified value.|
| `frozenset()`| Returns a new frozenset object.|
| `getattr()`| Returns the value of the specified attribute of an object. |
| `globals()`| Returns the current global symbol table as a dictionary.|
| `hasattr()`| Returns True if the object has the specified attribute. |
| `hash()`| Returns the hash value of an object.|
| `help()`| Invokes the built-in help system. |
| `hex()` | Converts an integer to a hexadecimal string.|
| `id()`| Returns the identity of an object.|
| `input()`| Reads a line from input, converts it to a string, and returns it. |
| `int()` | Returns an integer object.|
| `isinstance()`| Returns True if the specified object is an instance of the specified class.|
| `issubclass()`| Returns True if the specified class is a subclass of another class.|
| `iter()`| Returns an iterator object.|
| `len()` | Returns the length (the number of items) of an object.|
| `license()`| Prints the Python Software Foundation License.|
| `list()`| Returns a list. |
| `locals()` | Returns the current local symbol table as a dictionary. |
| `map()` | Applies a function to all items in an input iterable. |
| `max()` | Returns the largest item in an iterable or the largest of two or more arguments. |
| `memoryview()`| Returns a memory view object.|
| `min()` | Returns the smallest item in an iterable or the smallest of two or more arguments. |
| `next()`| Retrieves the next item from an iterator.|
| `object()` | Returns a new featureless object. |
| `oct()` | Converts an integer to an octal string.|
| `open()`| Opens a file and returns a corresponding file object. |
| `ord()` | Returns an integer representing the Unicode character.|
| `pow()` | Returns x to the power of y. |
| `print()`| Prints objects to the text stream file.|
| `property()` | Returns a property attribute.|
| `quit()`| Exits the Python interpreter.|
| `range()`| Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. |
| `repr()`| Returns a string containing a printable representation of an object. |
| `reversed()` | Returns a reverse iterator.|
| `round()`| Returns the rounded value of a number to the specified number of decimals. |
| `set()` | Returns a new set object. |
| `setattr()`| Sets the value of the specified attribute of an object. |
| `slice()`| Returns a slice object. |
| `sorted()` | Returns a sorted list from the specified iterable. |
| `staticmethod()`| Returns a static method for the specified function.|
| `str()` | Returns a string object.|
| `sum()` | Sums the items of an iterable. |
| `super(None)`| Returns a proxy object that delegates method calls to a parent or sibling class. |
| `tuple()`| Returns a tuple.|
| `type()`| Returns the type of an object. |
| `vars()`| Returns the `__dict__` attribute of the given object. |
| `zip()` | Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables. |

For more pre-defined functions programmers will look for code `libraries` written and maintained by other programmers.

`Libraries` are just how they sound, they store code for a specific function. 


<br>

## `The built-in help() function`
The `help()` function in Python is a built-in utility that provides interactive help for modules, classes, functions, and methods. When called with an object, `help()` returns documentation about that object, displaying useful information such as its docstring, available methods, and attributes. It can be a helpful tool for beginners, and remember everything in python is an object.
```python
help(1)
help(str)
help(print)
help("text")
help(dict)
help(complex)
```




<br>

[Back to Top](#python-functions)

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

<br>

## `Lambdas as function templates`
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


## `Lambdas can be used to pass a small function as an argument`
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

<br>

# `Documentation: doc strings`
`docstrings`(short for documentation strings) in Python are a type of comment used to explain the purpose and usage of a function, class, method, or module.

* docstrings use triple quotes *`'''`* or *`"""`*  
* docstrings are typically the first statement within a function, class, or module.  
* The first line should always be a short, concise summary of the object’s purpose.  
  * For brevity, it should not explicitly state the object’s name or type, since these are available by other means (except if the name happens to be a verb describing a function’s operation).  
  * This line should begin with a capital letter and end with a period.  

* If there are more lines in the documentation string, the second line should be blank, visually separating the summary from the rest of the description.  
>
* The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc. 

* docstrings can be accessed programmatically using the `__doc__` attribute 

<br>

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
`Function`
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
`Class`
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
`Module`
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

[Back to Top](#python-functions)

___

<br>

# `Function Annotations` 
Basically: `Function Annotations` are a way to document/provide type hints

Specifically: `Function Annotations` a way of attaching `metadata` to the parameters of a function and its return value. 

Function and Type Annotations show up very often when working with 

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

<br>

[Back to Top](#python-functions)

___

<br>

# `Some Function Examples`
Functions can include all kinds of different code including other functions.
Conditionals, While Loops, For loops, etc. can all be used inside of functions.

Here are just a few examples:

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


```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found
```
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target is not found
```

<br>

[Back to Top]()

___

*Created and maintained by Mr. Merritt*













































