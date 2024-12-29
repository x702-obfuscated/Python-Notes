# `importlab`
The importlab is here to help you understand how to import.
> Use the packages and models to discover how to properly import, and errors that may occur.

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

\_\_init__.py: Marks the directory as a Python package. It can be empty or contain package initialization code.

<br>

[Back To Top](#importlab)

___

<br>

# `Absolute Imports Executing main.py as a script`
from .\root_package 
```
> python main.py
```
from ./root_package 
``` 
$ python3 main.py   
```

The import code is the same for each of these files. It is relative to the main script.
Keep in mind that you should not import the current module within itself.  
`main.py`
`module1.py`
`module2.py`
`module3.py`
`module4.py`
`module5.py`
`module6.py`
`module7.py`
`module8.py`

```python
import module1
import module2
from package1 import module3
from package1 import module4
from package2 import module5
from package2 import module6
from package2.package3 import module7
from package2.package3 import module8
```

<br>

[Back To Top](#importlab)

___

<br>

# `Absolute Imports Executing main.py with package context`
from ..\root_package 
```
> python -m root_package.main 
```
from ../root_package 
```
$ python3 -m root_package.main     
```

The import code is the same for each of these files. It is relative to the top level package.
Keep in mind that you should not import the current module within itself  
`main.py`
`module1.py`
`module2.py`
`module3.py`
`module4.py`
`module5.py`
`module6.py`
`module7.py`
`module8.py`
```python
from root_package import module1
from root_package import module2
from root_package.package1 import module3
from root_package.package1 import module4
from root_package.package2 import module5
from root_package.package2 import module6
from root_package.package2.package3 import module7
from root_package.package2.package3 import module8
```

<br>

[Back To Top](#importlab)

___

<br>


# `Relative imports relative to the top level package.`
from ..\root_package 
```
> python -m root_package.main 
```
from ../root_package 
```
$ python3 -m root_package.main
```

<br>

`main.py`
```python
from . import module1
from . import module2
from .package1 import module3
from .package1 import module4
from .package2 import module5
from .package2 import module6
from .package2.package3 import module7
from .package2.package3 import module8
```

`module1.py`
```python
from . import module2
from .package1 import module3
from .package1 import module4
from .package2 import module5
from .package2 import module6
from .package2.package3 import module7
from .package2.package3 import module8
```

`module2.py`
```python
from . import module1
from .package1 import module3
from .package1 import module4
from .package2 import module5
from .package2 import module6
from .package2.package3 import module7
from .package2.package3 import module8
```

`module3.py`
```python
from .. import module1
from .. import module2
from . import module4
from ..package2 import module5
from ..package2 import module6
from ..package2.package3 import module7
from ..package2.package3 import module8
```

`module4.py`
```python
from .. import module1
from .. import module2
from . import module3
from ..package2 import module5
from ..package2 import module6
from ..package2.package3 import module7
from ..package2.package3 import module8
```

`module5.py`
```python
from .. import module1
from .. import module2
from ..package1 import module3
from ..package1 import module4
from .import module6
from .package3 import module7
from .package3 import module8
```

`module6.py`
```python
from .. import module1
from .. import module2
from ..package1 import module3
from ..package1 import module4
from .import module5
from .package3 import module7
from .package3 import module8
```

`module7.py`
```python
from ... import module1
from ... import module2
from ...package1 import module3
from ...package1 import module4
from .. import module5
from .. import module6
from . import module8
```

`module8.py`
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

[Back To Top](#importlab)

___

<br>


# `Relative imports relative to the top level module.`
from root_package 
```
> python main.py
```
from root_package 
```
$ python3 main.py
```

<br>

`main.py`
```python
# ALL OF THESE RESULT IN ImportError: attempted relative import with no known parent package
from . import module1
from . import module2
from .package1 import module3
from .package1 import module4
from .package2 import module5
from .package2 import module6
from .package2.package3 import module7
from .package2.package3 import module8
```

`module1.py`
```python
# ALL OF THESE RESULT IN ImportError: attempted relative import with no known parent package
from . import module2
from .package1 import module3
from .package1 import module4
from .package2 import module5
from .package2 import module6
from .package2.package3 import module7
from .package2.package3 import module8
```

`module2.py`
```python
# ALL OF THESE RESULT IN ImportError: attempted relative import with no known parent package
from . import module1
from .package1 import module3
from .package1 import module4
from .package2 import module5
from .package2 import module6
from .package2.package3 import module7
from .package2.package3 import module8
```

`module3.py`
```python
# This will work without error
from . import module4

# THESE RESULT IN ImportError: attempted relative import beyond top-level package
from .. import module1
from .. import module2
from ..package2 import module5
from ..package2 import module6
from ..package2.package3 import module7
from ..package2.package3 import module8
```

`module4.py`
```python
# This will work without error
from . import module3

# THESE RESULT IN ImportError: attempted relative import beyond top-level package
from .. import module1
from .. import module2
from ..package2 import module5
from ..package2 import module6
from ..package2.package3 import module7
from ..package2.package3 import module8
```

`module5.py`
```python
# THESE will work without error:
from .import module6
from .package3 import module7
from .package3 import module8

# THESE RESULT IN ImportError: attempted relative import beyond top-level package
from .. import module1
from .. import module2
from ..package1 import module3
from ..package1 import module4

```

`module6.py`
```python
# THESE will work without error:
from .import module5
from .package3 import module7
from .package3 import module8

# THESE RESULT IN ImportError: attempted relative import beyond top-level package
from .. import module1
from .. import module2
from ..package1 import module3
from ..package1 import module4

```

`module7.py`
```python
# THESE will work without error:
from .. import module5
from .. import module6
from . import module8


# THESE RESULT IN ImportError: attempted relative import beyond top-level package
from ... import module1
from ... import module2
from ...package1 import module3
from ...package1 import module4

```

`module8.py`
```python
# THESE will work without error:
from .. import module5
from .. import module6
from . import module7

# THESE RESULT IN ImportError: attempted relative import beyond top-level package
from ... import module1
from ... import module2
from ...package1 import module3
from ...package1 import module4

```

<br>

[Back To Top](#importlab)

___

<br>

*Created and maintained by Mr. Merritt*

