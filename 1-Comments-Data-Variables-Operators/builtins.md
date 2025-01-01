
# `Python builtins`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Defining Built-ins`](#defining-built-ins)
    1. [`How to see built-in attributes`](#how-to-see-built-in-attributesa)
    1. [`How to see built-in modules`](#how-to-see-built-in-modules)
1. [`Built-in Constants`](#built-in-warnings)
1. [`Dunder Built-ins`](#dunder-built-ins)
1. [`Built-in Functions`](#built-in-functions)
1. [`Built-in Error and Exception Classes`](#built-in-error-and-exception-classes)
1. [`Built-in Warnings`](#built-in-warnings)
1. [`Built-in Modules`](#built-in-modules)



<br>

___

<br>

# `Defining Built-ins`
`built-ins` refer to the set of functions, exceptions, constants , and other objects that are available by default in the Python interpreter.
* They are always accessible and do not require importing any additional libraries or modules. 
* Built-in functions and objects are an integral part of the Python programming language and serve as the core tools that you can use for various tasks 

<br>

| **Category** | **Description** | **Examples** |
|--|--|--|
| **Built-in Types**| Basic data types provided by Python. | `int`, `str`, `float`, `list`, `dict`, `tuple`, `set`|
| **Built-in Constants**| Constants predefined in Python that represent certain values. | `True`, `False`, `None`, `Ellipsis`|
| **Built-in Functions**| Functions that are always available for use in Python. | `print()`, `len()`, `sum()`, `min()`, `max()`, `abs()`|
| **Dunder Methods**| Special methods (magic methods) used to customize object behavior in certain operations. | `__init__`, `__str__`, `__repr__`, `__len__`, `__add__`, `__getitem__` |
| **Built-in Exceptions** | Standard exceptions available to handle errors in Python.| `TypeError`, `ValueError`, `IndexError`, `KeyError`, `IOError` |
| **Built-in Modules**| Modules that provide core functionality for various tasks like file I/O, system operations, math, etc.| `os`, `sys`, `math`, `random`, `datetime`, `json`, `re`, `subprocess`|

<br>

## `How to see built-in attributesa`
The built-in `dir()` function when passed the `__builtins__` constant will return a list of all built in attributes.

*The `__builtins__` object contains all of Python's built-in functions, exceptions, and other objects.*
*`__builtins__` is intentionally kept separate from itself to avoid infinite recursion. If `__builtins__` were present inside itself, it could lead to an infinite loop or recursive references when trying to access or modify its contents.*

syntax:
```
dir(__builtins__)
```

```python
print(dir(__builtins__))

#Output: 
# [
#     'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 
#     'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
#     'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 
#     'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 
#     'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 
#     'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 
#     'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 
#     'PendingDeprecationWarning', 'PermissionError','ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 
#     'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 
#     'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 
#     'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 
#     'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__debug__', 
#     '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 
#     'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 
#     'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 
#     'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 
#     'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 
#     'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 
#     'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'
# ]
```

<br>

## `How to see built-in modules`
importing the `sys` module and printing `sys.built_module_names` will output a tuple of all built-in modules.


```python
import sys
print(sys.builtin_module_names)

#Output: 
# (
#     '_abc', '_ast', '_bisect', '_blake2', '_codecs', 
#     '_codecs_cn', '_codecs_hk', '_codecs_iso2022', 
#     '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', 
#     '_contextvars', '_csv', '_datetime', '_functools', '_heapq', 
#     '_imp', '_interpchannels', '_interpqueues', '_interpreters', 
#     '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', 
#     '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', 
#     '_sha3', '_signal', '_sre', '_stat', '_statistics', '_string', 
#     '_struct', '_symtable', '_sysconfig', '_thread', '_tokenize', 
#     '_tracemalloc', '_typing', '_warnings', '_weakref', '_winapi', 
#     'array', 'atexit', 'binascii', 'builtins', 'cmath', 'errno', 
#     'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 
#     'msvcrt', 'nt', 'sys', 'time', 'winreg', 'xxsubtype', 'zlib'
# )
```

<br>

<br>

[Back To Top](#python-builtins)

___

<br>

# `Built-in Constants`
`Builtin constants `in Python are special, predefined objects or values that have specific meanings and are used throughout the language. These constants are available globally and can be directly accessed in Python code.

| **Special Constant**   | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| `False`                | Boolean value representing `False`.                                             |
| `None`                 | A special constant representing the absence of a value or null.                 |
| `True`                 | Boolean value representing `True`.                                              |
| `Ellipsis (...)`         | The special object `Ellipsis` is used in slices and other places for readability.|
| `NotImplemented`       | A placeholder constant used to indicate that a method or function is not implemented. |


<br>

[Back To Top](#python-builtins)

___

<br>

# `Dunder Built-ins`

`Dunder builtins` (short for "double underscore") are special methods and attributes in Python that are used internally by the Python interpreter. 
* These methods and attributes are part of the object model in Python and enable objects to interact with the built-in language features, such as operators, iteration, and function calls.

| **Special Attribute** | **Description**                                                                                  |
|--------------------------------|--------------------------------------------------------------------------------------------------|
| `__build_class__`             | Internal function used to create a new class. Invoked by the `class` keyword                       |
| `__debug__`                   | A constant that is `True` when Python is not running with the `-O` (optimize) flag. Used by the `import` statement.|
| `__doc__`                     | A special attribute that stores the documentation string for a module, class, or function.       |
| `__import__`                  | A built-in function used for dynamic import of modules.                                          |
| `__loader__`                  | An attribute used in module loading mechanisms.                                                 |
| `__name__`                    | A special variable that is set to the name of the module or script.                              |
| `__package__`                 | Used to determine the package of a module when running a program as part of a package.           |
| `__spec__`                    | An attribute that contains module import metadata.                                              |


<br>

[Back To Top](#python-builtins)

___

<br>

# `Built-in Functions`
`built-in functions` in Python are pre-defined functions provided by the Python interpreter, meaning they are always available for call without requiring an explicit import. 

Here is a complete list of available built-in functions:

| **Builtin**      | **Description**                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| `abs`            | Returns the absolute value of a number.                                                          |
| `aiter`          | Returns an asynchronous iterator from an object.                                                 |
| `all`            | Returns `True` if all elements of an iterable are true.                                          |
| `anext`          | Returns the next item from an asynchronous iterator.                                             |
| `any`            | Returns `True` if any element of an iterable is true.                                            |
| `ascii`          | Returns a string containing a printable representation of an object, with non-ASCII characters escaped. |
| `bin`            | Converts an integer to a binary string.                                                          |
| `bool`           | Converts a value to a boolean (`True` or `False`).                                               |
| `breakpoint`     | Invokes the debugger at the current point in the program.                                        |
| `bytearray`      | Returns a new bytearray object.                                                                  |
| `bytes`          | Converts an object to bytes.                                                                     |
| `callable`       | Checks if an object appears callable (e.g., a function or method).                               |
| `chr`            | Returns a string representing a character for a given Unicode code point.                       |
| `classmethod`    | Converts a method to a class method, bound to the class rather than an instance.                 |
| `compile`        | Compiles source code into a code object.                                                         |
| `complex`        | Creates a complex number from a real and imaginary part.                                         |
| `copyright`      | Returns copyright information for the Python interpreter.                                        |
| `credits`        | Returns credits for contributors to Python.                                                     |
| `delattr`        | Deletes an attribute from an object.                                                             |
| `dict`           | Creates a new dictionary.                                                                       |
| `dir`            | Returns a list of attributes and methods of an object.                                           |
| `divmod`         | Returns a tuple of the quotient and remainder of a division operation.                          |
| `enumerate`      | Returns an iterator that produces pairs of an index and an item from an iterable.               |
| `eval`           | Executes a Python expression within a given context.                                            |
| `exec`           | Executes a Python program dynamically.                                                          |
| `exit`           | Exits the Python interpreter.                                                                   |
| `filter`         | Filters elements of an iterable based on a function.                                            |
| `float`          | Converts a value to a floating-point number.                                                    |
| `format`         | Formats a string based on template syntax.                                                      |
| `frozenset`      | Returns a new frozenset object.                                                                 |
| `getattr`        | Retrieves an attribute of an object, with a default value.                                      |
| `globals`        | Returns the global namespace as a dictionary.                                                   |
| `hasattr`        | Checks if an object has a specified attribute.                                                  |
| `hash`           | Returns the hash value of an object.                                                            |
| `help`           | Invokes the built-in help system for interactive assistance.                                    |
| `hex`            | Converts an integer to a hexadecimal string.                                                   |
| `id`             | Returns the identity of an object.                                                              |
| `input`          | Reads input from the user.                                                                      |
| `int`            | Converts a value to an integer.                                                                 |
| `isinstance`     | Checks if an object is an instance of a specified class.                                        |
| `issubclass`     | Checks if a class is a subclass of another.                                                     |
| `iter`           | Returns an iterator from an iterable.                                                           |
| `len`            | Returns the length of an object.                                                                |
| `license`        | Returns the licensing information for Python.                                                  |
| `list`           | Converts an iterable to a list.                                                                |
| `locals`         | Returns the local namespace as a dictionary.                                                   |
| `map`            | Applies a function to all items in an iterable.                                                |
| `max`            | Returns the largest item in an iterable.                                                       |
| `memoryview`     | Creates a memory view object.                                                                   |
| `min`            | Returns the smallest item in an iterable.                                                      |
| `next`           | Retrieves the next item from an iterator.                                                      |
| `object`         | Creates a new object instance.                                                                  |
| `oct`            | Converts an integer to an octal string.                                                        |
| `open`           | Opens a file.                                                                                  |
| `ord`            | Returns the Unicode code point for a single character.                                         |
| `pow`            | Returns the result of raising a base to a power, with optional modulus.                        |
| `print`          | Prints objects to the console.                                                                 |
| `property`       | Creates a managed attribute.                                                                   |
| `range`          | Creates a sequence of numbers.                                                                 |
| `repr`           | Returns a string representation of an object.                                                  |
| `reversed`       | Returns a reversed iterator.                                                                   |
| `round`          | Rounds a number to a specified number of digits.                                               |
| `set`            | Creates a new set object.                                                                      |
| `setattr`        | Sets an attribute of an object.                                                                |
| `slice`          | Creates a slice object.                                                                        |
| `sorted`         | Returns a sorted list from an iterable.                                                        |
| `staticmethod`   | Converts a method to a static method.                                                          |
| `str`            | Converts an object to a string.                                                                |
| `sum`            | Returns the sum of an iterable.                                                                |
| `super`          | Calls a method from a parent class.                                                            |
| `tuple`          | Converts an iterable to a tuple.                                                               |
| `type`           | Returns the type of an object or creates a new type.                                           |
| `vars`           | Returns the attributes of an object as a dictionary.                                           |
| `zip`            | Returns an iterator that combines elements from multiple iterables.                            |


<br>

[Back To Top](#python-builtins)

___

<br>

# `Built-in Error and Exception Classes`
`Built-in error and exception classes` in Python represent various types of problems that can occur during the execution of a program. 
* These classes are part of the exception handling system in Python and provide the mechanism to raise, catch, and handle errors.

<br>

`Exceptions` in Python are objects derived from the `BaseException` class, and each class represents a specific type of error. When an error occurs, Python raises an exception, which can either be caught and handled or propagated up the call stack.

<br>

The `traceback` in Python refers to the detailed report generated when an exception is raised during the execution of a program. 
* It provides a stack trace, which includes information about the function calls that led to the exception. 
* This allows the programmer to trace the sequence of events that resulted in the error, helping to diagnose and fix the problem.

1. File Name: The name of the file where the exception occurred.
1. Line Number: The specific line number in the file where the exception was raised.
1. Function Name: The function (or method) in which the exception occurred.
1. Error Message: The message associated with the exception, describing what went wrong.
1. Stack Trace: The traceback will display the sequence of function calls leading up to the point where the exception occurred.

example:
```python
def example():
    x = 5/0

example()

# Output: 
# Traceback (most recent call last):
#   File "/path/to/file.py", line 4, in <module>
#     example()
#     ~~~~~~~^^
#   File "/path/to/file.py", line 2, in example 
#     x = 5/0
#         ~^~
# ZeroDivisionError: division by zero
```

<br>



| **Exception**                  | **Description**                                                                                         |
|--------------------------------|---------------------------------------------------------------------------------------------------------|
| `ArithmeticError`              | Base class for errors in numerical calculations (e.g., division by zero).                              |
| `AssertionError`               | Raised when an `assert` statement fails.                                                               |
| `AttributeError`               | Raised when an attribute reference or assignment fails.                                                |
| `BaseException`                | The base class for all built-in exceptions.                                                            |
| `BaseExceptionGroup`           | A base class for a group of exceptions, used in exception handling.                                    |
| `BlockingIOError`              | Raised when an operation would block on an object (e.g., I/O operation).                               |
| `BrokenPipeError`              | Raised when attempting to write to a pipe or socket that is closed.                                    |
| `BufferError`                  | Raised when a buffer-related operation cannot be performed.                                            |
| `ChildProcessError`            | Raised when a child process fails in a system call.                                                    |
| `ConnectionAbortedError`       | Raised when a connection is aborted (e.g., network communication failure).                             |
| `ConnectionError`              | Base class for all connection-related errors.                                                          |
| `ConnectionRefusedError`       | Raised when a connection is refused.                                                                   |
| `ConnectionResetError`         | Raised when a connection is reset.                                                                     |
| `EOFError`                     | Raised when the `input()` function hits an end-of-file condition.                                      |
| `EnvironmentError`             | Base class for errors related to the operating environment (e.g., files, directories).                 |
| `Exception`                    | The base class for all non-exit exceptions.                                                            |
| `ExceptionGroup`               | A class used to represent a group of exceptions, typically for parallelism or async contexts.          |
| `FileExistsError`              | Raised when trying to create a file or directory that already exists.                                  |
| `FileNotFoundError`            | Raised when trying to open a file that does not exist.                                                 |
| `FloatingPointError`           | Raised for errors in floating-point calculations.                                                      |
| `GeneratorExit`                | Raised when a generator's `close()` method is called.                                                  |
| `IOError`                      | Raised when an I/O operation (e.g., file read/write) fails.                                            |
| `ImportError`                  | Raised when an import fails (e.g., module not found).                                                  |
| `IndentationError`             | Raised when there is an incorrect indentation level in the source code.                                |
| `IndexError`                   | Raised when trying to access an element of a sequence by index, and the index is out of range.         |
| `InterruptedError`             | Raised when an operation is interrupted (e.g., during sleep or I/O operations).                        |
| `IsADirectoryError`            | Raised when a file operation is attempted on a directory.                                              |
| `KeyError`                     | Raised when trying to access a dictionary with a key that does not exist.                              |
| `KeyboardInterrupt`            | Raised when the user interrupts the execution with a keyboard signal (Ctrl+C).                        |
| `LookupError`                  | Base class for all errors raised when a key or index lookup fails.                                     |
| `MemoryError`                  | Raised when an operation runs out of memory.                                                           |
| `ModuleNotFoundError`          | Raised when an import fails due to a module not being found.                                           |
| `NameError`                    | Raised when a local or global name is not found.                                                       |
| `NotADirectoryError`           | Raised when a directory operation is performed on a file.                                              |
| `NotImplementedError`          | Raised when an abstract method or unimplemented feature is called.                                     |
| `OSError`                      | Raised when a system-related operation fails (e.g., file access).                                      |
| `OverflowError`                | Raised when the result of an arithmetic operation is too large to be represented.                      |
| `PermissionError`              | Raised when trying to perform an operation without sufficient privileges.                              |
| `ProcessLookupError`           | Raised when a process is requested that does not exist.                                                |
| `RecursionError`               | Raised when the maximum recursion depth is exceeded.                                                   |
| `ReferenceError`               | Raised when a weak reference is used to access an object that has been garbage-collected.              |
| `RuntimeError`                 | Raised when an error occurs that doesn’t fall into another category.                                   |
| `StopAsyncIteration`           | Raised to signal that an asynchronous iterator has completed.                                          |
| `StopIteration`                | Raised to signal that an iterator has no more items to return.                                         |
| `SyntaxError`                  | Raised when the Python code is incorrect or malformed.                                                 |
| `SystemError`                  | Raised when the Python interpreter detects an internal error.                                          |
| `SystemExit`                   | Raised when the `sys.exit()` function is called.                                                       |
| `TimeoutError`                 | Raised when a timeout occurs (e.g., in networking or multithreading).                                  |
| `TypeError`                    | Raised when an operation or function is applied to an object of inappropriate type.                    |
| `UnboundLocalError`            | Raised when a local variable is referenced before it has been assigned.                                |
| `UnicodeDecodeError`           | Raised when a byte sequence is unable to be decoded into a Unicode string.                             |
| `UnicodeEncodeError`           | Raised when a Unicode string is unable to be encoded into a byte sequence.                             |
| `UnicodeError`                 | A base class for all Unicode-related errors.                                                           |
| `UnicodeTranslateError`        | Raised when a Unicode string is unable to be translated into a different encoding.                     |
| `WindowsError`                 | Raised for Windows-specific errors related to system calls (deprecated in Python 3.x).                 |
| `ZeroDivisionError`            | Raised when a division or modulo operation is performed with zero as the divisor.                      |


<br>

[Back To Top](#python-builtins)

___

<br>

# `Built-in Warnings`
`Warnings` in Python are a mechanism used to notify developers about potential issues or conditions in the code that do not necessarily cause the program to crash, but may lead to undesirable behavior, inefficiency, or future problems. 


| **Warning**                | **Description**                                                                               |
|----------------------------|-----------------------------------------------------------------------------------------------|
| `BytesWarning`             | Issued for cases where bytes-related warnings are needed.                                     |
| `DeprecationWarning`       | Raised when a feature or behavior is deprecated and will be removed in future Python releases.|
| `EncodingWarning`          | A warning related to encoding issues in text operations.                                      |
| `FutureWarning`            | Raised to indicate that something may change in future Python releases.                      |
| `ImportWarning`            | Issued when there are issues with importing modules (e.g., deprecated features).             |
| `PendingDeprecationWarning`| Raised for features that will be deprecated in the future, but not yet.                      |
| `ResourceWarning`          | Raised to indicate resource-related warnings (e.g., unclosed files).                         |
| `RuntimeWarning`           | A warning raised during runtime for issues like performance.                                 |
| `SyntaxWarning`            | A warning about a possible syntax issue or style guide violation.                            |
| `UnicodeWarning`           | Raised for potential issues with Unicode data.                                               |
| `UserWarning`              | A warning raised by user code, typically for non-critical issues.                            |



<br>

[Back To Top](#python-builtins)

___

<br>

# `Built-in Modules`

A `module` in Python is a file containing Python code that defines classes, functions, and variables, and can include executable code.


`Built-in modules` in Python are modules that are included with the Python installation (The Standard Library), providing a wide range of functionality such as file I/O, system operations, math functions, and more, without needing to be installed separately.

<br>

| **Module**| **Description** |
|--|--|
| `_abc`| Provides tools for working with abstract base classes (ABCs).|
| `_ast`| Handles the Abstract Syntax Tree, useful for code parsing and compilation. |
| `_bisect` | Implements algorithms for maintaining sorted lists.|
| `_blake2` | Provides the BLAKE2 cryptographic hash function. |
| `_codecs` | Supports base codec functionality for encoding and decoding. |
| `_codecs_cn`| Provides codecs for Chinese encodings. |
| `_codecs_hk`| Provides codecs for Hong Kong encodings. |
| `_codecs_iso2022` | Provides codecs for ISO-2022 encodings.|
| `_codecs_jp`| Provides codecs for Japanese encodings.|
| `_codecs_kr`| Provides codecs for Korean encodings.|
| `_codecs_tw`| Provides codecs for Taiwanese encodings. |
| `_collections`| Implements the underlying machinery for Python's `collections` module. |
| `_contextvars`| Provides support for context variables used in asynchronous programming. |
| `_csv`| Implements underlying functionality for CSV file handling. |
| `_datetime` | Implements core date and time functionality for the `datetime` module. |
| `_functools`| Provides optimized implementations of functions used in `functools`. |
| `_heapq`| Provides the underlying implementation for the heap queue algorithms.|
| `_imp`| Supports Python's import machinery. |
| `_interpchannels` | Provides mechanisms for communication between interpreters (in multi-interpreter setups).|
| `_interpqueues` | Adds support for message passing between interpreters. |
| `_interpreters` | Implements multi-interpreter support for isolated execution contexts.|
| `_io` | Implements the core I/O functionality in Python.|
| `_json` | Provides optimized implementations for JSON encoding and decoding. |
| `_locale` | Supports locale-based internationalization features. |
| `_lsprof` | Provides functionality for Python's profiler. |
| `_md5`| Implements the MD5 hashing algorithm. |
| `_multibytecodec` | Provides support for multi-byte character encodings.|
| `_opcode` | Exposes low-level opcode constants used in Python bytecode. |
| `_operator` | Implements core functionality for the `operator` module.|
| `_pickle` | Provides optimized implementations for the `pickle` serialization module. |
| `_random` | Implements the core pseudo-random number generator. |
| `_sha1` | Provides the SHA-1 cryptographic hash function. |
| `_sha2` | Provides the SHA-2 cryptographic hash function. |
| `_sha3` | Provides the SHA-3 cryptographic hash function. |
| `_signal` | Provides signal-handling support. |
| `_sre`| Implements the core regular expression engine.|
| `_stat` | Supports `os.stat` and related operations.|
| `_statistics` | Implements optimized mathematical functions for the `statistics` module. |
| `_string` | Provides basic support for string operations. |
| `_struct` | Implements the core functionality for `struct` module's data packing and unpacking. |
| `_symtable` | Provides access to the symbol table used by the compiler. |
| `_sysconfig`| Provides configuration information about the Python installation. |
| `_thread` | Implements the low-level threading support. |
| `_tokenize` | Implements the core functionality for Python's tokenizer. |
| `_tracemalloc`| Implements memory allocation tracing for debugging memory leaks. |
| `_typing` | Provides internal support for Python's type hints.|
| `_warnings` | Implements Python's warning system. |
| `_weakref`| Provides support for weak references to objects.|
| `_winapi` | Provides access to low-level Windows API functionality. |
| `array` | Supports efficient arrays of numeric data.|
| `atexit`| Provides a mechanism to register functions to be called upon interpreter exit.|
| `binascii`| Provides tools for binary and ASCII conversions.|
| `builtins`| Contains Python's built-in objects and functions. |
| `cmath` | Provides mathematical functions for complex numbers.|
| `errno` | Defines symbolic error codes from the C `errno` variable. |
| `faulthandler`| Enables debugging of Python crashes by dumping tracebacks on a fault. |
| `gc`| Provides access to garbage collection facilities. |
| `itertools` | Implements fast, memory-efficient iterators.|
| `marshal` | Supports serialization of Python objects into a binary format.|
| `math`| Provides mathematical functions and constants.|
| `mmap`| Allows memory-mapped file access. |
| `msvcrt`| Provides Windows-specific console I/O operations.              |
| `nt`| Provides functionality for interacting with the Windows operating system. |
| `sys` | Provides access to Python's runtime environment and system variables. |
| `time`| Provides time-related functions and utilities.|
| `winreg`| Provides access to the Windows Registry.|
| `xxsubtype` | Includes examples of C extensions for Python developers.|
| `zlib`| Supports compression and decompression using the zlib library.|


<br>



[Back To Top](#python-builtins)

___

<br>




*Created and maintained by Mr. Merritt*













