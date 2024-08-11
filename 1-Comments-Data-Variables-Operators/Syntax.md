# `Python Syntax`
___
Covered in this file
1. General Syntax 
2. Every Open Needs a Close: '', "", (), [], {}
3. Indentation is required in Python
4. Python Programming Style Guide
5. Two Univeral Programming Truths

<br>

# `General Syntax`
___

> * Syntax: rules for writing a language
> * Code is executed from top to bottom, left to right, line by line.
<pre>
Python code is executed from top to bottom, left to right, and line by line.   
1 Top,Left >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Top,Right>  
2     V  
3        V  
4            V  
5                V  Python  
6                    V  Requires  
7                        V  Indentation  
8                            V  In Its  
9                                V  Syntax  
10                                   V   
11                                       V  
12                                            V  
13                                                 V  
14                                                     V  
15                                                         V  
16                                                             V  
17                                                                 V  
18 Bottom,Left >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Bottom,Right> 
</pre> 
<br>

# `Every Opening Needs a Closing: '', "", (), [], {}`
___
> * In general most symbols in python come in pairs, every opening symbol requires a closing symbol


```python
'' # single quotes
"" # double quotes
() # parenthesis
[] # square brackets
{} # curly braces
```
<br>

# `Indentation is required in Python:`
___ 
## if, elif, else, while, for, def, class, etc.
> * Indentation is used to define scope or context of blocks of code and is required for python syntax.


```python
... # > used as place holder
```


```python
'Conditionals'
if(...):
    ... #indented code block
    
#unindent to exit scope
elif(...):
    ... #indented code block

#unindent to exit scope
else:
    ... #indented code block

#unindent to exit scope
```


```python
'While Loops'
while(...):
    ... #indented code block
    
#unindent to exit scope
```


```python
'For Loops'
for _ in ...:
    ... #indented code block
    
#unindent to exit scope

```


```python
'Function Definitions'
def function():
    ... #indented code block
    
#unindent to exit scope
```


```python
'Class Definitions'
class foo():
    ... #indented code block
    
#unindent to exit scope
```
<br>

# `Python Programming Style Guide`
___

> * The Python Programming Style Guide, commonly known as PEP 8, is a document that provides conventions for writing Python code. 
> * It aims to improve the readability and consistency of Python code, making it easier to maintain and collaborate on projects. 

To see the full style guide: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

## Here are the most important take aways:
* Use 4-space indentation, and no tabs. Editors like VSCode automatically covert for you.  
    * 4 spaces are a good compromise between small indentation (allows greater nesting depth) and large indentation (easier to read). 
    * Tabs introduce confusion, and are best left out.  

* Wrap lines so that they don't exceed 79 characters.  

* Use blank lines to separate functions and classes, and larger blocks of code inside functions.  

* When possible, put comments on a line of their own.  

* Use docstrings to document functions and classes.  

* Use spaces around operators and after commas, but not directly inside bracketing constructs:  
    * Example: a = f(1, 2) + g(3, 4)
    
* Name your classes and functions consistently; the convention is to
    * UpperCamelCase for classes
    * lower_snake_case for functions and methods.
    * Always use ***self*** as the name for the first method argument

<br>

# `Two Universal Programming Truths`
___
## 1. Code is either perfectly written or it is wrong.
## 2. All software is broken.
