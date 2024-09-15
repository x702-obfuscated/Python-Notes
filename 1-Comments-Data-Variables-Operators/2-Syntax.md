# `Python Syntax`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file
1. [`General Syntax`](#general-syntax) 
1. [`Every Open Needs a Close: '', "", (), [], {}`](#every-opening-needs-a-closing-----)
1. [`Indentation is required in Python`](#indentation-is-required-in-python)
1. [`Python Programming Style Guide`](#python-programming-style-guide)
1. [`Univeral Programming Truths`](#universal-programming-truths)

<br>

[Back to Top](#python-syntax)
___
# `General Syntax`


> * Syntax: rules for writing a language
> * Source Code is executed from top to bottom, left to right, line by line.
```
Python code is executed from top to bottom, left to right, and line by line.   
1 Top,Left >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Top,Right>  
2     >  
3        >  
4            >  
5                >  Python  
6                    >  Requires  
7                        >  Indentation  
8                            >  In Its  
9                                >  Syntax  
10                                   >   
11                                       >  
12                                           >  
13                                               >  
14                                                   >  
15                                                       >  
16                                                           >  
17                                                               >  
18 Bottom,Left >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Bottom,Right> 
``` 
<br>

[Back to Top](#python-syntax)
___
# `Every Opening Needs a Closing: '', "", (), [], {}`

> * In general most symbols in python come in pairs, every opening symbol requires a closing symbol


```python
'' # single quotes
"" # double quotes
() # parenthesis
[] # square brackets
{} # curly braces
```
<br>

[Back to Top](#python-syntax)
___
# `Indentation is required in Python:`
 
## if, elif, else, while, for, def, class, etc.
> * Indentation is used to define scope or context of blocks of code and is required for python syntax.


```python
... # used as place holder
```
```python
'Conditionals'
if(...):
    ... # > indented code block
    
# < unindent to exit scope
elif(...):
    ... # > indented code block

# < unindent to exit scope
else:
    ... # > indented code block

# < unindent to exit scope
```
```python
'While Loops'
while(...):
    ... # > indented code block
    
# < unindent to exit scope
```
```python
'For Loops'
for _ in ...:
    ... # > indented code block
    
# < unindent to exit scope

```
```python
'Function Definitions'
def function():
    ... # > indented code block
    
# < unindent to exit scope
```
```python
'Class Definitions'
class foo():
    ... # > indented code block
    
# < unindent to exit scope
```
<br>

[Back to Top](#python-syntax)
___
# `Python Programming Style Guide`

The Python Programming Style Guide, commonly known as PEP 8, is a document that provides conventions for writing Python code. 
> * It aims to improve the readability and consistency of Python code, making it easier to maintain and collaborate on projects. 

To see the full style guide: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

<br>

## `Important takeaways`
* Use 4-space indentation, and no tabs. *Editors like VSCode automatically convert for you.*
>    * 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). 
>    * Tabs introduce confusion, and are best left out.  

* Wrap lines so that they don't exceed 79 characters.  

* Use blank lines to separate functions and classes, and larger blocks of code inside functions.  

* When possible, put comments on a line of their own.  

* Use docstrings to document functions and classes.  

* Use spaces around operators and after commas, but not directly inside bracketing constructs:  
    * Example: 
    
    `a = f(1, 2) + g(3, 4)`
    
* Name your classes and functions consistently; the convention is to
    * `UpperCamelCase` for classes
    * `lower_snake_case` for functions and methods.
    * Always use `self` as the name for the first method argument

<br>

[Back to Top](#python-syntax)
___
# `Universal Programming Truths`

## 1. Syntax is either perfectly written or it is wrong.
## 2. All software is broken.


---
[Back to Top](#python-syntax)

---
*Created and maintained by Mr. Merritt*  