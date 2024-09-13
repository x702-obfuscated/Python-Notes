# `Python Variables`
Covered in this file:
1. [`Defining a Variable`](#defining-a-variable)
1. [`Creating a Variable`](#creating-a-variable)
    1. [`Assigning Multiple Variables the same value`](#assigning-multiple-variables-the-same-value)
    1. [`Assigning Multiple Variables on the same line`](#assigning-multiple-variables-on-the-same-line)
    1. [`Reassigning a Variable`](#reassigning-a-variable)
1. [`Rules For Naming Variables`](#rules-for-naming-variables)
1. [`Variables are Pointers to Locations in Memory`](#variables-are-pointers-to-locations-in-memory)
    1. [`A Lower Level Explanation of Variables`](#a-lower-level-explanation-of-variables)
    1. [`NameError: name is not defined`](#nameerror-name-is-not-defined)
1. [`Variable Aliasing`](#variable-aliasing)
    1. [`Creating Aliases`](#creating-aliases)
    1. [`Aliasing: Immutable Types`](#aliasing-immutable-types)
    1. [`Aliasing: Mutable Types`](#aliasing-mutable-types)
1. [`Type Annotations: Declaring a Variable Type`](#type-annotation-declaring-variable-type)
1. [`Variable Scope/Context`](#variable-scopecontext)
    1. [`Built-in Namespace`](#built-in-namespace)
    1. [`Global Namespace`](#global-namespace-and-scope)
    1. [`Local Namespace and Scope`](#local-namespace-and-scope)
    1. [`global keyword`](#global-keyword)
    1. [`nonlocal keyword`](#nonlocal-keyword)
    1. [`Special Scoping Errors`](#special-scoping-errors)

<br>

___

<br>

# `Defining a Variable`
Basically: `variables` are like containers that store literal data 

Specifically: `variables` are pointers that reference a location in memory where the literal data is stored
> * The data a variable points to can change

<br>

*NOTE*: 
> The distinction between the basic explaination and the specific one is important here. 
> * Variables can be thought of as containers in most cases, however this analogy does not hold for all uses of variables and it is important to understand how they actually work.*

<br>

[Back to Top](#python-variables)

___

<br>

# `Creating a Variable`
To define a variable write the name of the variable followed by a single equal sign `=`
> * a single equals sign `=` is used to assign a variable to the data it references

> * **For source code readability variable names should represent the data they store**

<br>

Variable Creation Syntax:

    variable = value

examples:

```python
switch = False
num = 10
percent = 95.61
letter = "a"
name = "Jose"
bad_passwords = ["password","123456","12345678","1234","qwerty","12345","dragon"]

```


```python
a = "Hello World"
b = 5
c = 3.14
d = False
e = ["a","b","c"]

# a, b, c, d, e are variables
```

*NOTE*: 
> In many examples I will use a single letter as a variable, while this is perfectly legal python it is bad practice to code this way.***  
> * I do this for simplicity, and because often the example variables just store example data. 
<br>
 
***TO BE CLEAR:***
- Variable names should be representative of the data that they reference

> For example: If you are keeping track of a count with a variable, name the variable count. 


```python
count = 1
```

<br>

## `Assigning Multiple Variables the same value`
Set each variable equal to the next and finally to the value they will store
>   * this also makes the variables aliases

```python
a = b = c = 1
#a, b, and c, all reference the same data --> 1
```

<br>

## `Assigning Multiple Variables on the same line`
There are two ways to assign multiple variabes on the same line.

> * perform multiple assignment statements seperated with a **;**


```python
f = 2; g = 3; h = 4
```

OR
> * assign multiple variables seperated with a **,** to multiple values seperated with a **,**


```python
i, j, k = 5, 6, 7
# i = 5, j = 6, k = 7
```

<br>

## `Reassigning a Variable`
Reassigning a variable, is changing the value the variable references (points to) in memory
> * Rewrite the name of the variable and set it to a new value with `=`
```python
num = 1
#at this point in the program num is 1

num = 2 
# at this point in the program num is 2

print(num) # Output: 2
```


[Back to Top](#python-variables)
<br>
___

<br>

# `Rules for Naming Variables`
1. They are case sensitive (a and A are not the same)
1. Must start with letter or underscore "_"
1. Cannot start with a number 
1. Can only contain a-z, A-Z, 0-9, and "_" characters
1. Cannot contain spaces
1. Variables should be named after what they store/reference

<br>

## `Example: Legal Variable Names`


```python
var = 0
_var = 0
_v_ar = 0
vAr = 0
VAR = 0
var1 = 0 
```

<br>

## `Example: Illegal Variable Names`

```python
1var = 0
v-ar = 0
v ar = 0 
!var = 0
@#$%@ = 0

#each of these will raise an error
```

[Back to Top](#python-variables)
<br>
___

<br>

# `Variables are pointers to locations in memory`

## `A Lower Level Explanation of Variables`
This following is a lower level explaination of how variables work in Python.  
>
> * The basic definition of variables will work most of the time for beginners, but to understand some higher level concepts this information is required.

<br>


What happens when you assign 10 to x:
```python
x = 10
```
1. Python allocates memory for and creates an integer object in memory with the data literal `10`.
2. The variable `x` is assigned a reference to the memory location of the integer object `10`.
    * Python maintains a table that associates variables and their assigned references
3. When you access or modify a variable, Python uses the reference(memory address) to locate the actual object in memory

<br>

We can visualize this idea using the `id()` function call
* Use the `id()` function call to return the memory location to which variable points.
* Returns a integer `<class 'int'>` that is a unique identifier for a location in memory where the data is stored.
* The number will potentially be different each time the program is executed. 


```python
memory_pointer = "Hello World"
id(memory_pointer) # Returns: 139029363861936

memory_pointer = 10
id(memory_pointer) # Returns: 139029373780496

# id() returns the memory location of the data to which a variable points 
# The value that is returned will be different from the examples above
```
<br>

## `NameError: name is not defined.`
> * if you attempt to use a variable name that was never assigned a reference, a NameError is raised


```python
print(var) #Output: NameError: name 'var' is not defined.
```


[Back to Top](#python-variables)
<br>
___

<br>

# `Variable Aliasing`

`Aliasing` is the act of assigning one variable to the same reference as another variable  
> * aliases all point to the same memory location   
> * the act of assigning one variable to another passes a reference to the memory location of the data  

<br>

## `Creating Aliases`
```python
#a, b, and c are aliases (ie they point to the same data)
a = "some text"
b = a 
c = b

print(a)     # some text
print(b)     # some text
print(c)     # some text

print(id(a)) # 125810368587504 <-- Same Memory Location
print(id(b)) # 125810368587504 <-- Same Memory Location
print(id(c)) # 125810368587504 <-- Same Memory Location
```

<br>

## `Aliasing: Immutable Types`
Changing the reference of one variable, does not change the reference of the aliases


```python
#a, b, and c are aliases (ie they point to the same data)
a = "some text"
b = a 
c = b

# Pointing the variable 'a' to a new value
a = "a was changed"

print(a)     # a was changed
print(b)     # some text
print(c)     # some text

print(id(a)) # 125810368883120 <-- New Memory Location
print(id(b)) # 125810368587504 <-- Same Memory Location
print(id(c)) # 125810368587504 <-- Same Memory Location

```


```python
#a, b, and c are aliases (ie they point to the same data)
a = "some text"
b = a 
c = b

# Pointing the variable 'a' to a new value
a = "a was changed"

# Pointing the variable 'b' to a new value
b = "b was changed"

print(a)     # a was changed
print(b)     # b was changed
print(c)     # some text

print(id(a)) # 125810368883120
print(id(b)) # 125810368882544 <-- New Memory location
print(id(c)) # 125810368587504 
```


```python
#a, b, and c are aliases (ie they point to the same data)
a = "some text"
b = a 
c = b

# Pointing the variable 'a' to a new value
a = "a was changed"

# Pointing the variable 'b' to a new value
b = "b was changed"

# Pointing the variable 'c' to a new value.
c = "c was changed"

print(a)     # a was changed
print(b)     # b was changed
print(c)     # c was changed

print(id(a)) # 125810368883120 <-- Different Memory Location
print(id(b)) # 125810368882544 <-- Different Memory Location 
print(id(c)) # 125810368880496 <-- Different Memory Location
```

<br>

## `Aliasing: Mutable Types`
Changing the value of a mutable type, changes the value for all aliases


```python
# If variables point to the same mutable data type: 
# a change in the data is reflected in all the variables. 
a = [1,2,3]
b = a
c = b

c[0] = 999

print(a)     # [999, 2, 3]
print(b)     # [999, 2, 3]
print(c)     # [999, 2, 3]

print(id(a)) # 125810368584576 <-- Same Memory Location 
print(id(b)) # 125810368584576 <-- Same Memory Location
print(id(c)) # 125810368584576 <-- Same Memory Location

```


[Back to Top](#python-variables)
<br>
___

<br>

# `Type Annotation: Declaring Variable Type`
`Type Annotation` is a way to declare the type of data the variable is expected to reference
> * This is not enforced by the interpreter
>   * Which means if the variable references a different data type an error will NOT be raised

*Many other programming languages require that you declare the type of data a variable holds.*  

*Type Annotation is an excellent way to better document your code.*

<br>

Type Annotation Syntax:

    variable: type = value

examples:
```python
boolean: bool = True

num: int = 10

flo: float = 3.14

imaginary: complex = 1j

string: str = "Hello World"

list1d: list = ["a","b","c"]

tuple1d: tuple = ("a","b","c")

set1d: set = {"a","b","c"}

dictionary: dict = {"a": 97, "b": 98, "c":99}
```


[Back to Top](#python-variables)
<br>
___

<br>

# `Variable Scope/Context`
Basically: the area within code in which a variable can be accessed and used 

Specifically: refers to the visibility and accessibility of variables, functions, and other identifiers within a program.

* Scope/Context can be `global`, `local`, or `nonlocal`
* Python looks for variables by searching from the most local scope, to the least local scope. 

`global`: The global keyword can be used to access and modify global variables

`nonlocal`: The nonlocal keyword can be used to indicate variable access one scope up

`Namespace`: a mapping of names (variables) to objects, there are built-in, global and local namespaces.


*NOTE*: 
> It is important to understand that global and local are relative terms. Depending on where you are in a program and what variable you are refering to that same variable may described as global or local. 

Try this to help with your understanding:

`local variables` are local to something
> * **when you see local think 'inside of'**
>    * example: local to a module(file), class, method, or function

`global variables` are global to something
> * **when you see global think 'outside of'**
>    * example: global to a module(file), class, method, or function

<br>

## `Built-in Namespace`
The built-in namespace contains all of the built-in names provided by defualt


*Use the dir() function to see the current local namespace*

```python
# dir() returns a list of the current local namespace
namespace = dir()
print(namespace)

# Outputs: 
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
```

> Add the \_\_builtins\_\_ argument to see the built-in namespace


```python
# dir(__builtins__) returns a list of built-in names
builtin_namespace = dir(__builtins__)
print(builtin_namespace)

#Outputs:
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 
#  'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 
#  'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 
#  'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 
#  'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 
#  'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 
#  'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
#  'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 
#  'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 
#  'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 
#  'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', 
#  '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 
#  'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 
#  'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 
#  'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 
#  'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 
#  'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

```

<br>

## `Global Namespace and Scope`
Typically any variable created inside of a file (`module`), but not inside of another construct (`function`, `method`, `class`, etc.) has a global scope.  
* Variables with globals scope are called `global variables`


```python
num = 10 #global variable

print(dir()) 
#Outputs:
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'num']
#                                                                     'num' has been added to the global scope for this module ^^^

# in this case dir() returns the local namespace for the module, but what is local to the module is global to another part of the module's code
```

*NOTE*:
> Unlike other languages, variables created inside of a Conditional, or Loop are accessible outside of that construct.

`Conditionals`
```python
#if example
if(False): 
    x = "x"
    y = "y"
    #here the if block does not execute
    # x and y are never defined

# This leads to an error:
print(x) # Output: NameError: name 'x' is not defined
print(y) # Output: NameError: name 'y' is not defined
```

```python
if(True):
    x = "x"
    y = "y"
    #here the block executes so x and y are now defined 

#Outside of the if x and y can still be printed
print(x) # x
print(y) # y
```

`While loops`
```python
i = 0
while(i<1):
    var = "while" # var is defined inside the while loop
    i += 1

#Here 'var' can be accessed and printed outside of the while loop
print(var) # Output: while
```

`For Loops`


```python
for num in range(5):
    var = "for"
    #both 'num' and 'var' have been defined inside the for loop 

#Here both 'num' and 'var' can both be accessed outside of the loop
print(num) #Output: 4
print(var) #Output: for
```

<br>

## `Local Namespace and Scope`
Variables created inside of a Function, Class, etc. are local to that construct

`Functions`
```python
def example(parameter):
    var = "inside function"
    print(parameter)  #Outputs the value of parameter
    print(var)        #Output: inside function

    print(dir()) #Output: ['parameter', 'var']
    #'parameter' and 'var' exist in this namespace (local to example)

example("argument")  # even if you call the function before 'parameter' and 'var' are not accessible


print(dir())
#Output:
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'example']
# notice that 'parameter' and 'var' do not exist in this namespace (global)


print(parameter)    #NameError: name 'parameter' is not defined
print(var)          #NameError: name 'var' is not defined
```

`Classes`


```python
class Example:
    #local to the class Example
    var = "Class" 
    print(var) # Class


    print(dir()) # Output: ['__module__', '__qualname__', 'var']
    # 'var' exists in this namespace (local to Example)




print(dir()) 
# Output: 
['Example', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# notice that 'var' does not exist in this namespace (global)



print(var) #NameError: name 'var' is not defined

#var is only accessible inside of Example, or through Example, or through an instance of Example


```

<br>

## `global keyword`
The `global` keyword is used to access and modify a global scope variable inside of a local scope


```python
text = "I am global"

def example():
    text = "I am local"

example() #function call

print(text)# Output: I am global
#prints the global 'text', not the local 'text'
```


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

<br>

## `nonlocal keyword`
Use the `nonlocal` keyword to access 1 scope up


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

<br>

## `Special Scoping Errors`
```python
x = 'global'

def example():
    print(x) # Output: global 
    # accesses 'x' 1 scope out no problem

example()
```

UnboundLocalError: local variable referenced before assignment

```python
x = "global"

def example():
    print(x) #UnboundLocalError: local variable 'x' referenced before assignment
    x = "Change global x"

#Python assumes that since you created a local 'x' you ment to print the local 'x' and not the global 'x'
example()  
```

<br>

___


[Back to Top](#python-variables)
___

<br>

*Created and maintained by Mr. Merritt* 