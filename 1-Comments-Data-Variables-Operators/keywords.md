*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python Keywords`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [``]()


<br>

___

<br>

# `Keywords`



| **Keyword/Soft Keyword** | **Description**                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| `False`                  | A boolean constant representing the false value.                                                    |
| `None`                   | Represents the absence of a value or null.                                                          |
| `True`                   | A boolean constant representing the true value.                                                     |
| `and`                    | A logical operator used to combine conditional statements.                                          |
| `as`                     | Used for aliasing in `import` statements or exception handling.                                     |
| `assert`                 | Used for debugging; raises an `AssertionError` if the condition is false.                           |
| `async`                  | Declares a function as asynchronous, allowing the use of `await` inside it.                         |
| `await`                  | Used to pause execution until an asynchronous operation is complete.                                |
| `break`                  | Exits a loop prematurely.                                                                           |
| `class`                  | Used to define a class.                                                                             |
| `continue`               | Skips the rest of the current loop iteration and moves to the next iteration.                       |
| `def`                    | Used to define a function.                                                                          |
| `del`                    | Deletes objects or references to objects.                                                           |
| `elif`                   | Stands for "else if," used in conditional statements.                                               |
| `else`                   | Specifies code to execute if the preceding `if` or `elif` condition is false.                      |
| `except`                 | Specifies code to execute in case of an exception in a `try` block.                                 |
| `finally`                | Specifies code to execute after a `try` block, regardless of an exception occurring or not.         |
| `for`                    | Initiates a loop that iterates over a sequence.                                                     |
| `from`                   | Specifies the module from which to import specific attributes or functions.                         |
| `global`                 | Declares a variable as global, making it accessible across the entire module.                       |
| `if`                     | Introduces a conditional statement.                                                                |
| `import`                 | Used to include a module into the current program.                                                  |
| `in`                     | Tests membership in sequences or iterables.                                                        |
| `is`                     | Tests object identity, checking if two references point to the same object.                         |
| `lambda`                 | Creates anonymous functions.                                                                        |
| `nonlocal`               | Refers to variables in the nearest enclosing scope excluding global.                                |
| `not`                    | A logical operator that negates a condition.                                                       |
| `or`                     | A logical operator used to combine conditional statements, returning true if at least one is true.  |
| `pass`                   | A null operation used as a placeholder in code.                                                    |
| `raise`                  | Triggers an exception.                                                                              |
| `return`                 | Exits a function and optionally passes back a value.                                                |
| `try`                    | Specifies a block of code to be tested for exceptions.                                              |
| `while`                  | Initiates a loop that continues as long as a condition is true.                                     |
| `with`                   | Simplifies exception handling when working with resources like files.                               |
| `yield`                  | Pauses a function and returns a value, resuming execution on subsequent calls.                      |

<br>

[Back To Top](#python-keywords)

___

<br>

# `Soft Keywords`


| **Keyword/Soft Keyword** | **Description**                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------|
| `_`                      | A soft keyword used as a placeholder or for special purposes in interactive sessions.               |
| `case`                   | Used in pattern matching within a `match` statement.                                                |
| `match`                  | Introduces a pattern-matching block for complex conditional logic.                                  |
| `type`                   | A soft keyword that may represent type annotations or pattern matching for types.                   |

<br>

[Back To Top](#python-keywords)

___

<br>

# `Displaying all Keywords`

```python
from keyword import kwlist, softkwlist

def display_keywords() -> None:
    print("Keywords:")
    for i, kw in enumerate(kwlist, start=1):
        print(f"{i:2}: {kw}")

    print("Soft Keywords:")
    for i,skw in enumerate(softkwlist, start=1):
        print(f"{i:2}: {skw}")

def main() -> None:
    display_keywords()

if __name__ == "__main__":
    main()

```

<br>

[Back To Top](#python-keywords)

___

<br>

*Created and maintained by Mr. Merritt*



