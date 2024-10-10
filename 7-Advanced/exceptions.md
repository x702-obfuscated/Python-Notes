# `Exceptions`
---

`Covered in this file:`
1. Exceptions Defined
1. Exception Handling: Try-Except Statements

---
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


| Exception/Warning                | Description                                                                                          |
|:--------------------------------:|------------------------------------------------------------------------------------------------------|
| **BaseException**                | The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions.  |
| **BaseExceptionGroup**           | A special group class that contains all built-in exceptions.                                         |
| **GeneratorExit**                | Raised when a generator's `close()` method is called.                                                 |
| **KeyboardInterrupt**            | Raised when the user interrupts the execution of the program, typically by pressing Ctrl+C.           |
| **SystemExit**                   | Raised by the `sys.exit()` function to exit the program.                                              |
| **Exception**                    | The base class for all non-exit exceptions.                                                           |
| **ArithmeticError**              | The base class for arithmetic errors.                                                                 |
| **FloatingPointError**           | Raised when a floating-point operation fails.                                                         |
| **OverflowError**                | Raised when an arithmetic operation exceeds the limits of the current Python runtime environment.     |
| **ZeroDivisionError**            | Raised when the second operand of a division or modulo operation is zero.                             |
| **AssertionError**               | Raised when an `assert` statement fails.                                                              |
| **AttributeError**               | Raised when an attribute reference or assignment fails.                                               |
| **BufferError**                  | Raised when a buffer-related operation cannot be performed.                                           |
| **EOFError**                     | Raised when the `input()` function hits an end-of-file condition (EOF) without reading any data.      |
| **ExceptionGroup**               | A special group class that contains all non-exit exceptions.                                          |
| **ImportError**                  | Raised when the imported module is not found.                                                         |
| **ModuleNotFoundError**          | Raised when the imported module is not found.                                                         |
| **LookupError**                  | The base class for lookup errors.                                                                     |
| **IndexError**                   | Raised when a sequence subscript is out of range.                                                     |
| **KeyError**                     | Raised when a dictionary key is not found in the set of existing keys.                                |
| **MemoryError**                  | Raised when an operation runs out of memory.                                                          |
| **NameError**                    | Raised when a local or global name is not found.                                                      |
| **UnboundLocalError**            | Raised when a local variable is referenced before it has been assigned a value.                       |
| **OSError**                      | The base class for system-related errors.                                                             |
| **BlockingIOError**              | Raised when an operation would block on an object set for non-blocking operation.                     |
| **ChildProcessError**            | Raised when an error occurs in the child process during a subprocess operation.                       |
| **ConnectionError**              | The base class for connection-related errors.                                                         |
| **BrokenPipeError**              | Raised when trying to write to a pipe while the other end has been closed.                            |
| **ConnectionAbortedError**       | Raised when a connection attempt is aborted by the network.                                           |
| **ConnectionRefusedError**       | Raised when a connection attempt is refused by the peer.                                              |
| **ConnectionResetError**         | Raised when the connection is reset by the peer.                                                      |
| **FileExistsError**              | Raised when trying to create a file or directory that already exists.                                 |
| **FileNotFoundError**            | Raised when a file or directory is requested but cannot be found.                                     |
| **InterruptedError**             | Raised when a system call is interrupted by an incoming signal.                                       |
| **IsADirectoryError**            | Raised when a file operation (such as `os.remove()`) is requested on a directory.                     |
| **NotADirectoryError**           | Raised when a directory operation (such as `os.listdir()`) is requested on a file.                    |
| **PermissionError**              | Raised when trying to perform an operation without the adequate permissions.                          |
| **ProcessLookupError**           | Raised when a given process does not exist.                                                           |
| **TimeoutError**                 | Raised when a timeout occurs during a socket operation.                                               |
| **ReferenceError**               | Raised when a weak reference proxy is used to access a garbage-collected referent.                    |
| **RuntimeError**                 | The base class for runtime errors.                                                                    |
| **NotImplementedError**          | Raised when an abstract method that should be implemented in a subclass is not actually implemented.  |
| **RecursionError**               | Raised when the maximum recursion depth is exceeded.                                                  |
| **StopAsyncIteration**           | Raised by an async iterator's `anext()` method to signal the end of iteration.                        |
| **StopIteration**                | Raised by the `next()` function to indicate that there are no further items to be returned by an iterator. |
| **SyntaxError**                  | Raised when there is a syntax error in the code.                                                      |
| **IndentationError**             | Raised when indentation is not properly aligned.                                                      |
| **TabError**                     | Raised when the indentation consists of inconsistent tabs and spaces in the source code.              |
| **SystemError**                  | Raised when the interpreter encounters an internal error, which usually indicates a bug in the interpreter itself. |
| **TypeError**                    | Raised when an operation or function is applied to an object of an inappropriate type.                |
| **ValueError**                   | Raised when a built-in operation or function receives an argument with the right type but an inappropriate value. |
| **UnicodeError**                 | The base class for Unicode-related errors.                                                            |
| **UnicodeDecodeError**           | Raised when decoding Unicode fails.                                                                   |
| **UnicodeEncodeError**           | Raised when encoding Unicode fails.                                                                   |
| **UnicodeTranslateError**        | Raised when translating Unicode fails.                                                                |
| **Warning**                      | The base class for warning categories.                                                                |
| **BytesWarning**                 | Base category for bytes-related warnings.                                                             |
| **DeprecationWarning**           | Base category for warnings about deprecated features.                                                 |
| **EncodingWarning**              | Base category for warnings about encoding issues.                                                     |
| **FutureWarning**                | Base category for warnings about constructs that will change semantically in the future.              |
| **ImportWarning**                | Base category for warnings about probable mistakes in imports.                                        |
| **PendingDeprecationWarning**    | Base category for warnings about features that will be deprecated in the future.                      |
| **ResourceWarning**              | Base category for warnings about resource usage issues.                                               |
| **RuntimeWarning**               | Base category for warnings about suspicious runtime behavior.                                         |
| **SyntaxWarning**                | Base category for warnings about dubious syntax.                                                      |
| **UnicodeWarning**               | Base category for warnings about Unicode-related issues.                                              |
| **UserWarning**                  | A warning category intended for user-defined warnings.                                                |



---
# `Exception Handling: Try-Except Statements`
`Exception handling` in Python is a mechanism that allows developers to gracefully handle runtime errors, or "exceptions," without crashing the program. 
> * By catching and managing these exceptions, you can provide meaningful feedback to the user, log errors, and ensure that your program continues to run or exits cleanly when something unexpected occurs.

---
## `Try-Except`
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
    <code block that might raise and exception>
except:
    <code block to execute if any exception occurs>
```

Example:
> This is not best practice, but the basic format for a try-except block.
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

---
## `Handling Specific Errors`
Using except blocks, specific errors can be handled in specific ways.
> * The exception can be aliased as another name to be included in the handling process. This is useful for logging errors in the program. 

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

try:
    ...
except TypeError:
    ...
except ValueError:
    ...

try:
    ...
except Exception:
    ...
else:
    "Code Block to execute if no exception occurs"

try:
    ...
except Exception:
    ...
finally:
    'Code Block that always executes'



```python
'> Try-Except'
' > used for exception handling in python'

try:
    'Code Block that might raise an exception'

except:
    'Code Block to execute if the expection occurs'

#Handling specific errors

try:
    ...
except TypeError:
    ...
except ValueError:
    ...

try:
    ...
except Exception:
    ...
else:
    "Code Block to execute if no exception occurs"

try:
    ...
except Exception:
    ...
finally:
    'Code Block that always executes'
```