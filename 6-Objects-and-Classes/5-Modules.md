# `Python Modules`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Modules Defined`](#modules-defined)
1. [`Modules as Objects`](#modules-as-objects)
1. [`Importing Modules`](#importing-modules)
1. [`The Path`](#the-path)
1. [`if __name__ == "__main__":`](#if-__name__--__main__)
1. [`Built-in Modules`](#built-in-modules)

<br>

___

<br>

# `Modules Defined`

Basically: `Modules` are files containing Python code. 

Specifically: A `Module` is a Python (.py) file that contains attributes including: classes, functions, variables, etc, and is used to organise, modularise, and reuse python code.

```
<module_name>.py
```

<br>

`Modules can contain classes, functions, and variables that can be accessed when importing the module to other files`
```python
#in module (file) --> code.py

class Example_Class():
    pass

def example_function():
    pass

example_variable = None
```

To create your own module, simply create any python file (.py).

<br>

[Back To Top](#python-decorators)

___

<br>

# `Modules as Objects`
Modules in Python are objects, instances of class 'module', with their own attributes.

Some of these are dunder attributes that contain special information about the module.
| Attribute | Description|
|-------------------|----------------------------------------------------------------------------------------------|
| `__annotations__` | A dictionary storing variable type hints in the module (empty if no annotations are present).|
| `__builtins__`| A reference to the built-in namespace available in the module. |
| `__cached__`| The path to the compiled version of the module (e.g., `.pyc` file), if created.|
| `__doc__` | The docstring of the module, or `None` if no docstring is provided.|
| `__file__`| The path to the module file from which it was loaded.|
| `__loader__`| The loader object used to import the module. |
| `__name__`| The name of the module. If run as the main script, this will be `"__main__"`.|
| `__package__` | The package name of the module, or `None` if the module is not part of a package.|
| `__spec__`| The import specification (an instance of `ModuleSpec`) for the module. |


To see the currently accessible attributes of a module use `dir()` 
```python
print(dir())
# Output: ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
#Note this output is the result of an empty module.
```

<br>

To see the attributes of an imported module use `dir(module)`
```python
import code

print(dir(code))
#Output will vary depending on the module
```

<br>

To access and use the attributes from an imported module use `.` dot syntax.
```python
import code

code.Class_Example()
code.function_example()
code.variable_example
```
Alternatively use the `from <module> import <attribute>` syntax
* be aware this adds the names from the imported module to the current namespace, which may cause issues.
```python
from code import *

Class_Example()
function_example()
variable_example
```


<br>

[Back To Top](#python-decorators)

___

<br>

# `Importing Modules`
See [7-Advanced/Importing-Code/0-Importing-Overview/importing.md](../7-Advanced/Importing-Code/0-Importing-Overview/importing.md) for a more detailed explaination.

### `Basic Import`
```python
import code

code.Class()
code.function()
code.variable
```

<br>

### `Import and Alias`
```python
import code as c

c.Class()
c.function()
c.variable
```

<br>

### `Import Specific Attributes`
```python
from code import Class

Class()
```
```python
from code import function

function()
```
```python
from code import variable

variable
```
```python
from code import Class, function, variable

Class()
function()
variable
```

<br>

### `Import All`
```python
from code import *

Class()
function()
variable
```

<br>

[Back To Top](#python-decorators)

___

<br>

# `The Path`
The Path is a list of directories where Python wil looke for modules when the `import` statement is invoked. 
* The search path is controlled by the sys.path list which contains:
    * The directory of the currently running script (or "" when running interactively)
    * Directories in the PYTHONPATH environment variable (if set)
    * Default directories defined by Python (e.g, the standard library)

<br>

### `To See the PYTHONPATH environment variable`
```
Windows CMD
> echo %PYTHONPATH%
```
```
Windows Powershell
> echo $env:PYTHONPATH
```
```
Linux, MacOS
$ echo $PYTHONPATH
```

<br>

### `To see the Path`
```python
import sys

print(sys.path)
```




<br>

[Back To Top](#python-decorators)

___

<br>

# `if __name__ == "__main__":`
```python
if __name__ == "__main__":
    ...
```
is a commonly used conditional when working with models. 
1. When a module is imported the code within that module is executed exactly once. 
1. If there is code not contained within a Class, function, or variable, then it will executed as if the module was ran as a script. 
1. `if __name__ == "__main__":` is used to prevent executing unwanted code when importing.

<br>

`__name__` is a special dunder attribute of a module object.
* When a module is executed as a script `__name__` is assigned the value `"__main__"`
* When a module is imported `__name__` is assigned the name of the file without the .py extension


```python
print(__name__) #Output: __main__
```

```python
import code

print(code.__name__) #Output: code
```


<br>

```python
class Class_Example():
    pass

def function_example():
    pass

variable_example = None

print("When this module is imported the code inside is executed exactly once.")
```
```python
class Class_Example():
    pass

def function_example():
    pass

variable_example = None

if __name__ == "__main__":
    print("When this module is imported this code will not execute.")
```

<br>

[Back To Top](#python-decorators)

___

<br>

# `Built-in Modules`

To list the available modules use the `help()` function
```python
print(help("modules"))
#Output will vary
```

The output will include modules from the Python Standard Library, Third Party Modules, and even installed user created modules. 

<br>

[Back To Top](#python-decorators)

___

<br>

*Created and maintained by Mr. Merritt*











