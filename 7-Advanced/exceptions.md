# `Python Exceptions`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

___

`Covered in this file:`
1. [`Exceptions Defined`](#exceptions-defined)
1. [`Raising Exceptions`](#raising-exceptions)
1. [`Exception Handling: Try-Except Statements`](#exception-handling-try-except-statements)
1. [`Try-Except`](#try-except)
1. [`Handling Specific Exceptions`](#handling-specific-exceptions)
1. [`Handling Multiple Exception Types Identically`](#handling-multiple-exception-types-identically)
1. [`Else`](#else)
1. [`Finally`](#finally)
1. [`Nested try Blocks`](#nested-try-blocks)
1. [`Custom Exceptions`](#custom-exceptions)

<br>

___

<br>

# `Exceptions Defined`

In Python, `Exceptions` are events that occur during the execution of a program that disrupt the normal flow of the program's instructions. 
> Exceptions are run time errors


Common Exceptions:
| **Exception Type** | **Exception** | **Description** |
|:-:|:-:|:--|
| **General Exceptions**| `Exception`| The base class for most built-in exceptions.|
|| `BaseException`| The base class for all built-in exceptions. |
| **Arithmetic Exceptions** | `ArithmeticError`| The base class for all arithmetic-related exceptions. |
|| `ZeroDivisionError`| Raised when attempting to divide by zero. |
|| `OverflowError`| Raised when a numerical result is too large to be represented.|
|| `FloatingPointError` | Raised when a floating-point operation fails. |
| **Lookup Exceptions** | `LookupError`| The base class for exceptions raised when a key or index is not found. |
|| `IndexError` | Raised when a sequence index is out of range. |
|| `KeyError` | Raised when a dictionary key is not found.|
| **Type and Value Exceptions**| `TypeError` | Raised when an operation or function is applied to an object of inappropriate type.|
|| `ValueError` | Raised when a function receives an argument of the correct type but inappropriate value.|
|| `AttributeError` | Raised when an attribute reference or assignment fails. |
| **Input/Output Exceptions** | `IOError`| Raised when an I/O operation fails. (Alias of `OSError` in Python 3.) |
|| `FileNotFoundError`| Raised when an attempt to open a file that does not exist is made. |
|| `IsADirectoryError`| Raised when a file operation is requested on a directory. |
|| `NotADirectoryError` | Raised when a directory operation is requested on a non-directory.|
|| `EOFError` | Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data.|
| **Operating System Exceptions**| `OSError`| The base class for all exceptions that occur due to operating system-related errors. |
|| `FileExistsError`| Raised when trying to create a file or directory that already exists.|
|| `PermissionError`| Raised when trying to perform an operation without the required permissions. |
|| `TimeoutError` | Raised when a system function times out.|
| **Import Exceptions** | `ImportError`| Raised when an import fails.|
|| `ModuleNotFoundError`| Raised when a module or package is not found. |
| **Name Exceptions** | `NameError`| Raised when a local or global name is not found.|
|| `UnboundLocalError`| Raised when a local variable is referenced before it has been assigned. |
| **Assertion Exceptions**| `AssertionError` | Raised when an `assert` statement fails.|
| **Memory Exceptions** | `MemoryError`| Raised when an operation runs out of memory.|
| **Runtime Exceptions**| `RuntimeError` | Raised when an error is detected that doesn’t fall into any specific category. |
|| `NotImplementedError`| Raised when an abstract method that should be implemented in a subclass is not actually implemented.|
|| `RecursionError` | Raised when the maximum recursion depth is exceeded.|
| **System Exceptions** | `SystemError`| Raised when the interpreter detects an internal error.|
|| `SystemExit` | Raised by the `sys.exit()` function to exit the program.|
|| `KeyboardInterrupt`| Raised when the user interrupts the program’s execution, typically by pressing `Ctrl+C`.|
| **Connection Exceptions** | `ConnectionError` | The base class for all connection-related exceptions. |
|| `BrokenPipeError`| Raised when trying to write to a pipe while the other end has been closed.|
|| `ConnectionAbortedError` | Raised when a connection attempt is aborted by the network. |
|| `ConnectionRefusedError` | Raised when a connection attempt is refused by the peer.|
|| `ConnectionResetError` | Raised when the connection is reset by the peer.|
| **Warning Categories**| `Warning`| The base class for all warnings.|
|| `DeprecationWarning` | Raised when a feature is marked as deprecated.|
|| `FutureWarning`| Raised when a feature that will change in the future is used. |
|| `UserWarning`| Raised by `warnings.warn()` to issue a generic warning. |
|| `SyntaxWarning`| Raised for suspicious syntax. |
|| `RuntimeWarning` | Raised for suspicious runtime behavior. |
|| `ImportWarning`| Raised when an import might fail. |




Exception Hierarchy in Python:
```
BaseException
 ├── BaseExceptionGroup
 ├── GeneratorExit
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ExceptionGroup [BaseExceptionGroup]
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    └── RecursionError
      ├── StopAsyncIteration
      ├── StopIteration
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      └── Warning
           ├── BytesWarning
           ├── DeprecationWarning
           ├── EncodingWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── PendingDeprecationWarning
           ├── ResourceWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UnicodeWarning
           └── UserWarning
```


| Exception/Warning| Description|
|-:|:-|
| **BaseException**| The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions.|
| **BaseExceptionGroup** | A special group class that contains all built-in exceptions. |
| **GeneratorExit**| Raised when a generator's `close()` method is called. |
| **KeyboardInterrupt**| Raised when the user interrupts the execution of the program, typically by pressing Ctrl+C. |
| **SystemExit** | Raised by the `sys.exit()` function to exit the program.|
| **Exception**  | The base class for all non-exit exceptions. |
| **ArithmeticError**| The base class for arithmetic errors. |
| **FloatingPointError** | Raised when a floating-point operation fails. |
| **OverflowError**| Raised when an arithmetic operation exceeds the limits of the current Python runtime environment. |
| **ZeroDivisionError**| Raised when the second operand of a division or modulo operation is zero. |
| **AssertionError** | Raised when an `assert` statement fails.|
| **AttributeError** | Raised when an attribute reference or assignment fails. |
| **BufferError**| Raised when a buffer-related operation cannot be performed. |
| **EOFError** | Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data.|
| **ExceptionGroup** | A special group class that contains all non-exit exceptions.|
| **ImportError**| Raised when the imported module is not found.         |
| **ModuleNotFoundError**  | Raised when the imported module is not found. |
| **LookupError**| The base class for lookup errors. |
| **IndexError** | Raised when a sequence subscript is out of range. |
| **KeyError** | Raised when a dictionary key is not found in the set of existing keys.|
| **MemoryError**| Raised when an operation runs out of memory.|
| **NameError**| Raised when a local or global name is not found.|
| **UnboundLocalError**| Raised when a local variable is referenced before it has been assigned a value. |
| **OSError**| The base class for system-related errors. |
| **BlockingIOError**| Raised when an operation would block on an object set for non-blocking operation. |
| **ChildProcessError**| Raised when an error occurs in the child process during a subprocess operation. |
| **ConnectionError**| The base class for connection-related errors. |
| **BrokenPipeError**| Raised when trying to write to a pipe while the other end has been closed.|
| **ConnectionAbortedError** | Raised when a connection attempt is aborted by the network. |
| **ConnectionRefusedError** | Raised when a connection attempt is refused by the peer.|
| **ConnectionResetError** | Raised when the connection is reset by the peer.|
| **FileExistsError**| Raised when trying to create a file or directory that already exists. |
| **FileNotFoundError**| Raised when a file or directory is requested but cannot be found. |
| **InterruptedError** | Raised when a system call is interrupted by an incoming signal. |
| **IsADirectoryError**| Raised when a file operation (such as `os.remove()`) is requested on a directory. |
| **NotADirectoryError** | Raised when a directory operation (such as `os.listdir()`) is requested on a file.|
| **PermissionError**| Raised when trying to perform an operation without the adequate permissions.|
| **ProcessLookupError** | Raised when a given process does not exist. |
| **TimeoutError** | Raised when a timeout occurs during a socket operation. |
| **ReferenceError** | Raised when a weak reference proxy is used to access a garbage-collected referent.|
| **RuntimeError** | The base class for runtime errors.|
| **NotImplementedError**      | Raised when an abstract method that should be implemented in a subclass is not actually implemented.  |
| **RecursionError** | Raised when the maximum recursion depth is exceeded.|
| **StopAsyncIteration** | Raised by an async iterator's `anext()` method to signal the end of iteration.|
| **StopIteration**| Raised by the `next()` function to indicate that there are no further items to be returned by an iterator. |
| **SyntaxError**| Raised when there is a syntax error in the code.|
| **IndentationError** | Raised when indentation is not properly aligned.|
| **TabError** | Raised when the indentation consists of inconsistent tabs and spaces in the source code.|
| **SystemError**| Raised when the interpreter encounters an internal error, which usually indicates a bug in the interpreter itself. |
| **TypeError**| Raised when an operation or function is applied to an object of an inappropriate type.|
| **ValueError** | Raised when a built-in operation or function receives an argument with the right type but an inappropriate value. |
| **UnicodeError** | The base class for Unicode-related errors.|
| **UnicodeDecodeError** | Raised when decoding Unicode fails. |
| **UnicodeEncodeError** | Raised when encoding Unicode fails. |
| **UnicodeTranslateError**| Raised when translating Unicode fails.|
| **Warning**| The base class for warning categories.|
| **BytesWarning** | Base category for bytes-related warnings. |
| **DeprecationWarning** | Base category for warnings about deprecated features. |
| **EncodingWarning**| Base category for warnings about encoding issues. |
| **FutureWarning**| Base category for warnings about constructs that will change semantically in the future.|
| **ImportWarning**| Base category for warnings about probable mistakes in imports.|
| **PendingDeprecationWarning**| Base category for warnings about features that will be deprecated in the future.|
| **ResourceWarning**| Base category for warnings about resource usage issues. |
| **RuntimeWarning** | Base category for warnings about suspicious runtime behavior. |
| **SyntaxWarning**| Base category for warnings about dubious syntax.|
| **UnicodeWarning** | Base category for warnings about Unicode-related issues.|
| **UserWarning**| A warning category intended for user-defined warnings.|

___

<br>

[Back To Top](#python-exceptions)

___

<br>

# `Raising Exceptions`
The `raise` statement in Python is used to explicitly trigger an exception.
* `raise` can re raise and existing exception or raise a custom exception to indicate an error


Syntax:

`re-raise a previous exception`
```
raise
```
```python
try:
    print(5/0)

except ZeroDivisionError:
    print("Division by 0 is undefined")
    raise
```

<br>

`raise a specific exception`
```
raise <ExceptionType>
```
```python
raise AssertionError
```
<br>

`raise a specific exception with an error message`
```
raise <ExceptionType>("error message")
```
```python
raise NameError("NAME NOT FOUND")
```


<br>

[Back To Top](#python-exceptions)

___

<br>

# `Exception Handling: Try-Except Statements`
`Exception handling` in Python is a mechanism that allows developers to gracefully handle runtime errors, or "exceptions," without crashing the program. 
> * By catching and managing these exceptions, you can provide meaningful feedback to the user, log errors, and ensure that your program continues to run or exits cleanly when something unexpected occurs.

<br>

[Back To Top](#python-exceptions)

___

<br>

# `Try-Except`
`Try-Except` statements are used for handling exceptions gracefully during the execution of a program.

try block:
> * The code inside the try block is executed first.
> * If no exceptions occur, the except block is skipped.

except block:
> * If an exception occurs in the try block, the code in the except block is executed.
> * The program then continues executing after the except block.
> * You can catch specific exceptions by specifying the exception type after except.
> * Using except without specifying an error, will catch all errors. (This is not best practice)

<br>

Syntax:
```
try:
    <code block that might raise an exception>
except:
    <code block to execute if any exception occurs>
```

Example:
> This is not best practice, but the basic format for a try-except block.
> Best practice is to handle specific exceptions in order to avoid hiding bugs. 
```python
try:
    x = 10 / 0
except:
    print(f"Error occured")
```

```python
try:
    letters = ["a","b","c"]
    print(letters[3])
except:
    print(f"Error occured")
```

<br>

[Back To Top](#python-exceptions)

___

<br>

# `Handling Specific Exceptions`
Using except blocks, specific errors can be handled in specific ways.
> * The exception output can be aliased as another name to be included in the handling process. This is useful for logging errors in the program. 

Syntax:
```
try:
    ...
except <ExceptionType>:
    ...
except <ExceptionType> as <name>:
    ...
...
```
Examples:
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("That's not a valid number!")

except ZeroDivisionError:
    print("You can't divide by zero!")

except Exception as e:
    print(f"An error occured.\n{e}")
```



<br>

[Back To Top](#python-exceptions)

___

<br>


# `Handling Multiple Exception Types Identically`
Multiple Exceptions can be handled in the same manner when combining them as a tuple.

Syntax:
```
try:
    ...
except (<ExceptionType>,<ExceptionType>,...):
    ...
except (<ExceptionType>,<ExceptionType>,...) as <name>:
    ...
...
```

```python
try:
    print("Division Calculator\n")

    x = int(input("Type a number: "))
    y = int(input("Type another number: "))

    print(x / y)

except (ValueError, ZeroDivisionError) as e:
    print("Please enter 2 valid numbers to divide")
```

<br>

[Back To Top](#python-exceptions)

___

<br>

# `Else`

An `else` block executes if no exception occurs. 
* > The `else` block requires both a `try`, and `except` block


Syntax:
```
try:
    ...
except <ExceptionType>:
    ...
except <ExceptionType> as <name>:
    ...
else:
    ...
...
```


```python
try:
    user_input = float(input("Enter a number:\n"))
except ValueError:
    print("Please enter a valid number.")
else:
    print(f"You entered {user_input}")
```


<br>

[Back To Top](#python-exceptions)

___

<br>


# `Finally`
A `finally` block executes every time regardless of what happens before it. 
> * Placing recursive function calls inside of a `finally` block can result in `RecursionError`
> * The `finally` block will execute even when a `KeyboardInterrupt` occurs. 
> * `finally` does NOT require an `except` or `else` block. 

*`finally is particularly useful for cleanup tasks, or tasks that need to occur even if an error happens`*

Syntax:
```
try:
    ...
finally:
    ...
...
```
```
try:
    ...
except <ExceptionType>:
    ...
except <ExceptionType> as <name>:
    ...
else:
    ...
finally:
    ...
...
```

```python
import tempfile
import os

try:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(b"Temporary data")
    temp_file.close()
    print(f"Temporary file created at {temp_file.name}")
    # Simulates processing where an error occurs
    raise RuntimeError("Something went wrong!")
except RuntimeError as e:
    print(f"Runtime error occurred: {e}")
finally:
    print("Cleaning up the temporary file...")
    if os.path.exists(temp_file.name):
        os.remove(temp_file.name)
        print("Temporary file deleted.")
```


<br>

[Back To Top](#python-exceptions)

___

<br>


# `Nested try Blocks`
`try` blocks can be nested for more granular control, or to handle errors inside of an except block. 

Syntax:
```
try:
    try:
        ...
    except <ExceptionType>:
        ...
except <ExceptionType>:
    ...
```
```
try:
    ...
except <ExceptionType>:
    try:
        ...
    except <ExceptionType>:
        ...
```
<br>

```python
try:
    # Outer try: Handles file access
    with open("data.txt", "r") as file:
        try:
            # Inner try: Handles parsing errors
            data = file.read()
            numbers = [int(x) for x in data.split()]  # Assume file contains space-separated integers
            print("Parsed numbers:", numbers)
        except ValueError as e:
            print(f"Error parsing file content: {e}")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied!")
```

<br>

[Back To Top](#python-exceptions)

___

<br>


# `Custom Exceptions`
The complete implementation of Python's built-in Exception class is written in C as part of Python's core source code, so it's not directly available in Python's standard library as Python code. However, the following python code is a representation of the class implementation in Python.

```python
class Exception(BaseException):
    """Base class for all exceptions."""
    
    def __init__(self, *args):
        # Store arguments in the `args` attribute
        self.args = args

    def __str__(self):
        # Return a string representation
        if len(self.args) == 1:
            return str(self.args[0])
        return str(self.args)
```

<br>


## `Creating custom exceptions`
Custom Exceptions can be created by defining a custom exception class that inherits from the Exception class.

<br>

```python
class UserError(Exception):
    '''Custom Error caused by the User.'''

    def __init__(self,code="ID10T"):
        self.code = code
        super().__init__(f"An expected error has occured\nError Code: {self.code}")




def user_input():
    raise UserError()


try:
    user_input()

except UserError as e:
    print(e)
```
```python
class ID10TError(Exception):
    '''Custom Error caused by ID10Ts'''
    pass

try:
    raise ID10TError("You Broke It...")
except ID10TError as e:
    print(f"An error has occured, see output:\n{e}")
```
<br>

```python
class PEBKAC(Exception):
    '''Custom Error from between keyboard and chair'''
    pass

try: 
    raise PEBKAC("Problem Exists Between Keyboard And Chair")
except PEBKAC as e:
    print(f"An error has occured, see output:\n{e}")

```


<br>

[Back To Top](#python-exceptions)

___

<br>

*Created and maintained by Mr. Merritt*


