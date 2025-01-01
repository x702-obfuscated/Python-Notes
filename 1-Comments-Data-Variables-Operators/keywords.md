# `Python Keywords`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Keywords`](#keywords)
1. [`Soft Keywords`](#soft-keywords)
1. [`Displaying All Keywords`](#displaying-all-keywords)


<br>

___

<br>

# `Keywords`

Keywords are predefined, reserved words that have special meanings and purposes within the Python language.  
* form the syntax of Python code
* cannot be used as identifiers (names)
* are case sensitive

| **Keyword** | **Description** |
|---|---|
| `False`| A boolean constant representing the false value.|
| `None` | Represents the absence of a value or null.|
| `True` | A boolean constant representing the true value. |
| `and`| A logical operator used to combine conditional statements.|
| `as` | Used for aliasing in `import` statements or exception handling. |
| `assert` | Used for debugging; raises an `AssertionError` if the condition is false. |
| `async`| Declares a function as asynchronous, allowing the use of `await` inside it. |
| `await`| Used to pause execution until an asynchronous operation is complete.|
| `break`| Exits a loop prematurely. |
| `class`| Used to define a class. |
| `continue` | Skips the rest of the current loop iteration and moves to the next iteration. |
| `def`| Used to define a function.|
| `del`| Deletes objects or references to objects. |
| `elif` | Stands for "else if," used in conditional statements. |
| `else` | Specifies code to execute if the preceding `if` or `elif` condition is false.|
| `except` | Specifies code to execute in case of an exception in a `try` block. |
| `finally`| Specifies code to execute after a `try` block, regardless of an exception occurring or not. |
| `for`| Initiates a loop that iterates over a sequence. |
| `from` | Specifies the module from which to import specific attributes or functions. |
| `global` | Declares a variable as global, making it accessible across the entire module. |
| `if` | Introduces a conditional statement.|
| `import` | Used to include a module into the current program.|
| `in` | Tests membership in sequences or iterables.|
| `is` | Tests object identity, checking if two references point to the same object. |
| `lambda` | Creates anonymous functions.|
| `nonlocal` | Refers to variables in the nearest enclosing scope excluding global.|
| `not`| A logical operator that negates a condition. |
| `or` | A logical operator used to combine conditional statements, returning true if at least one is true.|
| `pass` | A null operation used as a placeholder in code.|
| `raise`| Triggers an exception.|
| `return` | Exits a function and optionally passes back a value.|
| `try`| Specifies a block of code to be tested for exceptions.|
| `while`| Initiates a loop that continues as long as a condition is true. |
| `with` | Simplifies exception handling when working with resources like files. |
| `yield`| Pauses a function and returns a value, resuming execution on subsequent calls.  |

<br>

[Back To Top](#python-keywords)

___

<br>

# `Soft Keywords`
`Soft Keywords`are keywords that have special meaning in certain context, but can still be used as identifiers (names)
* are not reserved
* can be used as identifiers

<br>


| **Soft Keyword** | **Description** |
|----|----|
| `_`| A soft keyword used as a placeholder or for special purposes in interactive sessions. |
| `case` | Used in pattern matching within a `match` statement.|
| `match`| Introduces a pattern-matching block for complex conditional logic.|
| `type` | A soft keyword that may represent type annotations or pattern matching for types. |

<br>

[Back To Top](#python-keywords)

___

<br>

# `Displaying all Keywords`

The function below can be used to display all of the keywords and soft keywords. 

```python
from keyword import kwlist, softkwlist

def display_keywords() -> None:
    print("Keywords:")
    for i, kw in enumerate(kwlist, start=1):
        print(f"{i:2}: {kw}")

    print("Soft Keywords:")
    for i,skw in enumerate(softkwlist, start=1):
        print(f"{i:2}: {skw}")

```
Expected Output:
```
Keywords:
 1: False
 2: None
 3: True
 4: and
 5: as
 6: assert
 7: async
 8: await
 9: break
10: class
11: continue
12: def
13: del
14: elif
15: else
16: except
17: finally
18: for
19: from
20: global
21: if
22: import
23: in
24: is
25: lambda
26: nonlocal
27: not
28: or
29: pass
30: raise
31: return
32: try
33: while
34: with
35: yield
Soft Keywords:
 1: _
 2: case
 3: match
 4: type
 ```

<br>

[Back To Top](#python-keywords)

___

<br>

*Created and maintained by Mr. Merritt*



