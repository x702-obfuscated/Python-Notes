# `Imports: Using code from other files`
---

Covered in this file:

1. Defining Modules, Packages, Libraries, and Frameworks
1. Basic Module Import
1. Import Specific Classes, Functions, and Attributes
1. Import and Entire Module
1. Module Aliasing
1. Import Classes, Functions, and Attributes with an Alias
1. Absolute and Relative Imports in a Package
1. Import Errors
1. Conditional Imports
1. The pip Package Manager

<br>

---
# `Defining Modules, Packages, Libraries, and Frameworks`

`Module`: a single Python file (.py file) that contains functions, classes, and variables. It can be imported and reused in other Python scripts.  
Examples:
* math
* random
* os
* sys
* time
* ...

`Built-in Modules`: are modules included with the Python standard library and provide a wide range of functionality without needing to install anything extra. 

`Custom Modules`: are modules written by you. 


<br>

`Package`: a collection of modules organized in directories that provide a hierarchy of modules. A package contains a special \_\_init__.py file that allows it to be treated as a module itself.  
Examples:
* numpy
* scipy
* requests

<br>


`Library`: a collection of modules and packages that provide a wide range of functionality. Libraries are often larger and more comprehensive than individual packages or modules.  
Examples:
* Pandas: A data analysis library that provides data structures and data analysis tools.
* TensorFlow: A library for machine learning and deep learning.

<br>

`Third-Party Libraries`: libraries created by the community of python developers that you can install using package management tools like `pip`.  
Examples:
* matplotlib: For plotting and data visualization.
* beautifulsoup4: For web scraping.

<br>

`Framework`: a collection of libraries, tools, and best practices for building specific types of applications. Frameworks are more comprehensive than libraries and often provide a structure for your code.  
Examples:
* Django: A high-level web framework for building web applications.
* Flask: A micro web framework for building web applications.
* PyTorch: A framework for deep learning, providing both high-level and low-level APIs.

<br>

---
# `Basic Module Importing`
The code in packages and modules can be included in your current module by using the `import` keyword. 
> * The classes, functions, and attributes of the module can then be accessed using the name of the module and dot (.) syntax.

Syntax:
```
import <module>

<module>.<class>
<module>.<method>
<module>.<variable>
```

<br>

Example
```python
import pathlib

pathlib.Path()      # pathlib Class
```
```python
import os

os.getcwd()         # os Method
os.name             # os attribute
```

<br>

---
# `Import Specific Classes, Functions, and Attributes`
*This method of importing can make your code cleaner and easier to read, but it requires careful management of your namespace to prevent unintended overrides or conflicts.*

Syntax:
```
from <module> import <class>
from <moduel> import <function>
from <moduel> import <attribute>
```
> Use a comma to seperate multiple specific imports from the same module.
```
from <module> import <class>, <function>, <attribute>
```

<br>

This syntax allows you to import specific classes, functions, or attributes from a module directly into the current namespace. 
> * After importing using this method, you can directly use the class, function, or attribute without referencing the module name.
> * This import method can lead to conflicts if the names of the imported items clash with names already defined in your code or other imports. For example, if you have a function named sqrt in your code, importing sqrt from the math module will overwrite your function.

<br>


Example:
```python
from datetime import datetime       # from datetime module import datetime class

datetime.now()
```
```python
from math import sqrt           # from math module import sqrt function

print(sqrt(16))                 # Output: 4
```
```python
from os import name

print(name)
```

<br>

Example with Conflict:
> *This will cause confusion as the imported 'sqrt' from math overrides the local function.*
```python
from math import sqrt

def sqrt(x):
    return x ** 2


result = sqrt(4)  # This will use math.sqrt, not the locally defined sqrt.
```

<br>

---
# `Import an Entire Module`
*This method of importing includes the entire module; it can make your code cleaner and easier to read. However, it requires careful management of your namespace to prevent unintended overrides or conflicts.*

Syntax: 
```
from <module> import *
```
Example:
```python
from math import * 

print(sqrt(25))
print(pi)
```

<br>

Example with Conflict:
> *This will cause confusion as the imported 'sqrt' from math overrides the local function.*
```python
from math import * 

def sqrt(x):
    return x ** 2


result = sqrt(4)  # This will use math.sqrt, not the locally defined sqrt.
```

<br>

---
# `Module Aliasing`
When importing, modules can be given an alias to shorten the name. 
> * Aliasing a module to a name that is already used elsewhere in your code can lead to conflicts. This can cause unexpected behavior if the alias shadows or overrides existing names.
> * Overuse of aliases, especially non-standard ones, can make code less readable and harder to understand for others (or even yourself) who are not familiar with the aliases.

Syntax:
```
import <module> as <name>
```

<br>

Example:
``` python
import tkinter as tk
```
<br> 

Example  of Reduced Readability:
> Using unconventional aliases may confuse readers
```python 
import matplotlib.pyplot as plt  # Common alias, generally acceptable
import numpy as np                # Common alias, generally acceptable


import datetime as dtmt
import requests as reqst
```

<br>

Example of Global Namespace Pollution and Reduced Readability:
> Using too many aliases can clutter the global namespace and make it harder to manage
```python
import math as m
import os as o
import sys as s
```

<br>

Example between Local and Imported names:
> Local variable 'js' shadows the aliased 'json' module
> Attempting to use 'js' as the module will refer to the local dictionary, not the 'json' module
```python
import json as js

js = {"name": "John"}  

data = js.loads('{"age": 30}')  # Returns: AttributeError: 'dict' object has no attribute 'loads'
```

<br>

---
# `Import Classes, Functions, Attributes with an Alias`
Multiple Classes, Functions, and/or Attributes can be imported and given an alias.

Syntax:
```
from <module> import <class> as <name>, <function> as <name>, <attribute> as <name>
```
Example:
```python
from math import sqrt as square_root, pi as pie

print(square_root(100)) 
print(pie)
```

<br>

---
# `Absolute and Relative Imports in a Package`
This project structure will be used to illustrate the concepts of absolute and relative importing in python. 
```
root_package/
├── __init__.py
├── main.py
├── module1.py
├── module2.py

├── package1/
    ├── __init__.py
    ├── module3.py
    └── module4.py

└── package2/
    ├── __init__.py
    ├── module5.py
    ├── module6.py

    └── package3/
        ├── __init__.py
        ├── module7.py
        └── module8.py
```

## *SEE ./import_lab for a complete list of all imports for this package structure, and to test different import combinations.*

<br>

When designing a project structure is it necessary to define an entrypoint for your code. 
An `entry point` in the context of software development is a specific point in a program where execution begins. 
> * It serves as the initial place where the program starts running or where control is passed when the program is invoked. 
> * The concept of an entry point can vary slightly depending on the context, such as in programming languages, containers, or executable files

*Here main.py will be used as the entrypoint for our example project*

*\_\_init__.py is used by Python to mark the directory as a Python package. It can be empty or contain package initialization code.*
 
Syntax for exectuing basic scripts and small projects:
```
> python <file>.py
```
```
$ python3 <file>.py
```
Example:
```
> python main.py
```
```
$ python3 main.py
```
<br> 

In order for Python to recognize the package containing the entrypoint,and for relative imports to work correctly we must revise our method of executing our scripts.
> * If you execute the entrypoint without specifying its containing package Python will not recoginize the entrypoint's containing directory as a package. This will cause relative import errors. 

Syntax for executing more complex projects:
```
> python -m <root_package>.<subpackage>.<...>.<entrypoint>
```
```
$ python3 -m <root_package>.<subpackage>.<...>.<entrypoint>
```
Example:
> Executed from the directory containing 'root_package'  
> from ..\root_package
```
> python -m root_package.main
```
> from ../root_package
```
$ python3 -m root_package.main
```
<br>

Note:
> * Dots (.): Separate the package names and modules. They represent the hierarchy in your directory structure.
> * Root Package: Refers to the top-level package (in this case, root_package).
> * Sub-Packages: Refer to nested directories within the root package that also contain an __init__.py file, making them packages (e.g., package1, package2, package3).
> * Modules: Python files (with the .py extension) that contain functions, classes, or variables.

<br>

## `Absolute Imports`
Absolute imports in Python allow you to import modules by specifing the full path from the root of the project. 

Syntax:
```
from <root_package>.<package1>.<package2>.<...> import <module>

from <root_package>.<package1>.<package2>.<...>.<module> import <class,function,attribute>
```
Example:
```python
from root_package import module1
```
```python
from root_package.package1 import module3
```
```python
from root_package.package2.package3 import module7
```
```python
from root_package.package2.package3.module8 import function
```

<br>

## `Relative Imports`
Relative imports in Python allow you to import modules relative to the position of the current module within the package hierarchy. 
> They are particularly useful in large projects with complex directory structures, as they make it easier to manage imports within a package without specifying the full path from the top-level directory.

<br>

* Single dot (.): Refers to the current package. Used to import a module from the same package.
* Double dots (..): Refers to the parent package. Used to import from a higher-level package.
* Triple dots (...): Refers to the grandparent package, and so on.

<br>

Syntax:
```
from <dots> import <module>

from <dots><package> import <module>

from <dots><package>.<module> import <class, function, attribute>
```
Example:
> Entrypoint: root_package/main.py  
> Current Module Path: root_package/package2/package3/module8.py  
> * from ..\\root_package > `python -m root_package.main` 
> * from ../root_package $ `python3 -m root_package.main`   
```python
from ... import module1
from ... import module2
from ...package1 import module3
from ...package1 import module4
from .. import module5
from .. import module6
from . import module7
```

<br>


## *SEE ./import_lab for a complete list of all imports for this package structure, and to test different import combinations.*

---
# `Import Errors`

### `ModuleNotFoundError`
This error occurs when Python cannot find the module or package you are trying to import. It might be due to a typo in the module name, an incorrect path, or the module not being installed or available in the environment.

<br>

### `ImportError: attempted relative import beyond top-level package`
This error occurs when you attempt to use a relative import that tries to go above the top-level package in your project's directory structure.   
Python uses the current module's location to determine the package hierarchy, and relative imports are meant to navigate within this hierarchy.   
If you try to move "upwards" beyond the root package using multiple dots (e.g., from ... import something), Python will raise this error because it's not allowed to go beyond the top-level package.

<br>

### `ImportError: attempted relative import with no known parent package`
This error occurs when you attempt to use a relative import in a module that Python doesn't recognize as part of a package. Python expects relative imports to be used only within a package, which means that the module should be executed as part of the package, not as a standalone script.

<br>

### `SyntaxError`
A SyntaxError may occur during an import if the imported module contains invalid syntax. This is not strictly an import error, but it can surface when you try to import a module that has syntax issues.

<br>

### `AttributeError`
This error occurs when you try to import an attribute (such as a function or class) that does not exist within a module.

<br>

### `ValueError: Attempted relative import beyond top-level package`
This error occurs when you use relative imports that attempt to go beyond the top level of the package hierarchy. Relative imports are only valid within packages.

<br>

### `Circular Imports`
Circular imports happen when two or more modules attempt to import each other. This can lead to an infinite loop or partial imports where the module has not finished being defined when it's needed.

<br>

---
# `Conditional Imports`
Imports can be made conditionally by combining conditional statements and import statements.

Example:
```python
need_math = True

if need_math:
    import math
```


---
# `The pip Package Manager`

`Package Manager`: a tool that automates the process of installing, upgrading, configuring, and removing software packages from a computer system or a development environment. 
> * In the context of programming languages, a package manager handles the downloading, installation, and management of libraries, modules, or frameworks that a project might depend on.
Examples:
* Operating Systems:
>   * apt (Advanced Package Tool) for Debian-based Linux distributions like Ubuntu.
>   * yum or dnf for Red Hat-based distributions like Fedora and CentOS.
>   * choco (Chocolatey) or winget (Windows Package Manager) for Windows
>   * Homebrew for macOS.
* Programming Languages:
>   * pip for Python.
>   * npm (Node Package Manager) for Node.js.
>   * gem for Ruby.
>   * cargo for Rust.
>   * composer for PHP.
Applications:
>   * Docker Compose for managing Docker containers.
>   * Helm for managing Kubernetes applications.

<br>

---
`Pip Installs Packages (pip)`: is the default package manager for Python. 
> * It allows you to install, manage, and uninstall Python packages and libraries from the Python Package Index (PyPI) and other repositories.

Installing pip:
```
> python -m ensurepip --upgrade

> python3 -m ensurepip --upgrade
```

<br>

*NOTE: Ensure that pip is included in the path environment variable on your system. If it is not you can still invoke pip using the python interpreter.*
Invoking pip with the python interpreter:
```
> python -m pip
```
```
$ python3 -m pip
```

<br>

Package Installation Syntax:
```
pip install <package_name>

pip install <package_name>==<version>
```
Example:
```
pip install matplotlib

pip install matplotlib==3.9.2
```

<br>

Package Uninstall Syntax:
```
pip uninstall <package_name>
```
Example:
```
pip uninstall matplotlib
```

<br>


## `Dependency Management`
pip automatically installs dependencies required by the packages you are installing.

List all Installed Packages:
```
pip list
```

<br>

Project dependencies can be specified in a 'requirements.txt' file and then installed using pip.
Install depedencies in requirements.txt:
```
pip install -r requirements.txt
```

<br>







