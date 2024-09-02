# `Basic Imports: Using code from other files`
---

Covered in this file:

1. Defining Modules, Packages, Libraries, and Frameworks
1. The pip Package Manager
1. Basic Module Import
1. Import Specific Functions or Classes
1. Import All Functions and Variables
1. Import a Module with an Alias
1. Import Specific Functions or Classes with an Alias
1. Relative Imports in a Package
1. Conditional Imports
1. Dynamic Imports with 'importlib'

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
# `Import and Entire Module`
*This method of importing includes the entire module; it can make your code cleaner and easier to read. However, it requires careful management of your namespace to prevent unintended overrides or conflicts.*

Syntax: 
```
from <module> import *
```

<br>

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
# `Relative Imports in a Package`
Relative imports in Python allow you to import modules relative to the position of the current module within the package hierarchy. 
> They are particularly useful in large projects with complex directory structures, as they make it easier to manage imports within a package without specifying the full path from the top-level directory.


This project structure will be used to illustrate the concepts of relative importing in python. 
```
root_package/
├── __init__.py
├── module1.py
├── module2.py

├── package1/
    ├── __init__.py
    ├── module3.py
    └── module4.py

├── package2/
    ├── __init__.py
    ├── module5.py
    ├── module6.py

    ├── package3/
        ├── __init__.py
        ├── module7.py
        └── module8.py
```

---
# `Conditional Imports`

---
# `Dynamic Imports with 'importlib'`


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







