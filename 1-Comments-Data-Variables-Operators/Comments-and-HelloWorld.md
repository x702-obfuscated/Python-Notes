# `Comments and Hello World!`
---

<br>

Covered in this file:
1. Introduction to the Python Programming Language
2. Single/Multi Line Comments
3. First Program: Console Output
4. First Program: User Input
5. Executing Python Programs
6. You are Experiencing an Error!

<br>

---
# `Script Kiddie's First Program:`
##  `An Introduction to the Python Programming Language!`

### ***Welcome Script Kiddies, to the Python Programming Language***
*As a new programmer you might be refered to as a Script Kiddie.*   
*This is a programmer joke to describe someone who does not know much about programming*  
*Script Kiddies often use code they do not understand written by other programmers, this is ok for now as you will get better as you code more!*  

<br>

Python is a high level interpreted procedural object oriented programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability and simplicity, using significant whitespace to enhance its readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used in various domains, including web development, data analysis, artificial intelligence, scientific computing, and automation.

1994: Python 1.0
* January 1994: Python 1.0 was released, introducing new features like lambda, map, filter, and reduce functions.  

2000: Python 2.0
* October 16, 2000: Python 2.0 was released, introducing list comprehensions, garbage collection, and many other features. This version aimed to improve the language's usability and performance.

2008: Python 3.0
* December 3, 2008: Python 3.0 (also known as Python 3000 or Py3k) was released. This version was designed to rectify fundamental design flaws in the language, leading to some incompatibility with Python 2.x. Key features included:
    * Improved Unicode support.
    * New syntax for print function and integer division.
    * Simplified syntax and consistent behavior.

2020: End of Python 2 Support
* January 1, 2020: Official support for Python 2 ended, marking a significant shift towards Python 3.x.

The current python version and documentation can be found here: [https://www.python.org](https://www.python.org/)  
To install python on your computer start here: [https://www.python.org/downloads/](https://www.python.org/downloads/)


> * Python files have the (.py) extension.   
> * The python interpreter is invoked using the 'python' command on Windows  
>
> * The python interpreter is invoked using the 'python3' command on UNIX like systems (Linux, Mac) 

> * The interpreter can be envoked interactively allowing you to write and execute line by line. 

Windows command syntax ( > represents the terminal prompt and can be omitted):

    > python

Linux/MacOS command syntax ( $ represents the terminal prompt and can be omitted):

    $ python3

<br>

> * The interpreter can be envoked and provided a filepath argument in order to interpret code written in a text file (.py)  

Windows command syntax:

    > python <filepath>

Linux/MacOS command syntax:

    $ python3 <filepath>

Examples:
```
> python main.py  
```
```
$ python3 main.py
```

<br>

*NOTE: <> angle brackets indicate a variable part of the command. For example: \<filepath\> indicates any filepath*  
*NOTE: For simplicity commands with a leading **>** should be understood as Windows Commands unless otherwise specified*  
*NOTE: For simplicity commands with leading **$** should be understood to be Linux/MacOS commands unless otherwise specified*  

> * Now that you have the basics, create a new file that ends in .py, open it in your favorite text editor and let's begin learning about the Python Programming Language.
>
>    * If it is your first time programming I recommend VScode as a text editor you can get it here: [https://code.visualstudio.com/](https://code.visualstudio.com/)

*Current Python Version at the time of writting: Python3.12.4*

<br>

---
# `Single/Multi-Line Comments`

Comments are a way for programmers to make notes about thier code.
> * comments are not interpreted as code and are simply ignored by the interpreter.
> * the best programmers write easy to read and well documented (commented) code.
>
> * comments can be used to prevent code from being executed without deleting that code. 

> * use the **#** symbol to make a single line comment
>
> * use a pair of triple single quotes **'''** or triple double quotes **"""** to make a multiline comment called a docstring.

<br>

### `Single-line comments`


```python
# this is a single line comment
# use a '#' hash tag to make a single line comment in python
```

<br>

### `Multi-line comments (docstrings)`
> * Everything between the pair of triple quotes is apart of the comment


```python
'''
use three single quotes to make a multi line comment
called 
a 
docstring
'''

"""
You 
    can 
        also 
            use 
                three 
                    double 
                        quotes 
"""
```

Use Ctrl + / in editors like VScode to make a quick multi-line comment, or to comment out a single line easily

<br>

---
# `First Program: Console Output`

> * To build your first program use the built-in ***print( )*** function call to send output to console (called standard output or stdout)

 


Here we will print out "Hello World".   
Literal text must be written in quotes, and is called a string. 


```python
"Hello World"
```

To print out this text we use the built-in function call ***print( )*** with the argument "Hello World"


```python
print("Hello World")
```

<br>

---
# `First Program: User Input`


> * To handle input from a user (called standard input or stdin), use the built-in function call ***input( )***.

> * ***input( )*** stops the execution of the program, and waits for the user to type in some text, it then returns the text that was entered.

*Note: returning will show up alot in programming, when something "returns" it brings a value back to that point in the program where it can be used*

Here we will print out whatever the user, in this case you types when prompted for input.  
We will begin by calling the built-in ***input( )*** function call.


```python
input()
```

Placing a string argument inside of the ***input( )*** function call prints out a prompt to tell the user what input to provide.


```python
input("Type your input: ")
```

If you place the ***input()*** function call inside of the ***print()*** function call the user input will be output back to the console.


```python
print(input("Type your input: "))
```

<br>

---

# `Executing a Python Program`

**Congrats you have written your first python program! Now, how do you get the computer to run this 'code'?**

> * What you have just written is called scource code. Scource code refers to the human-readable set of instructions and statements written by a programmer using a programming language.  
> * While it may not seem like it the code that you have just written is not actually readable by the computer.   
> * We will need another program to translate this high-level scource code into another form of code that the computer can understand.   
>
> * For python this program is the python interpreter.   
  



|Scource Code|\>\>\>|Byte Code|\>\>\>|Machine Code|\>\>\>|Result|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|text|Python Interpreter|Bytes|Python Virtual Machine|Binary|CPU|
|stored in .py file|python.exe (Windows)python3 (Linux/MacOS)|stored in a .pyc file inside of the \_\_pycache\_\_ directory. Is platform independent|PVM|Is platform dependent||Output|  

<br>



> * Scource code like this is compiled into byte code by the python interpreter.  
>   * Windows: python.exe
>   * Linux/MacOS: python3

> * Then the python virtual machine PVM converts the bytecode into machinecode and the CPU  executes the instructions one by one.


To execute your own Python program invoke the interpreter through the command line or python shell and provide your filename as an argument. Then hit ENTER.  
Syntax:
```
> python <filename>
```
```
$ python3 <filename>
```

Examples:
```  
> python main.py 
```
``` 
$ python3 main.py
```

*NOTE: > for Windows, and $ for Linux/MacOS. These symbols should be omitted when typing the command on your computer.*  
*NOTE: If you are experiencing issued with using the python or python3 commands, make sure that the executable has been added to the system path*


<br>

## `Python on Windows`
Python is installed by default here on Windows depending on the version installed.  
    
    C:\Program Files\Python3xx  
    
&nbsp;&nbsp;&nbsp;&nbsp;*where xx indicates the installed version*   
<br>

Python may also be installed here for a specific user: 

    C:\Users\USER\AppData\Local\Programs\Python\Python3xx
<br>
    
To check the current version type the following on the command line interface

    > python --version
<br>
To execute .py files on windows type the following on the command line interface

    > python <filename>
<br>

## `Python On Linux or MacOS`
  
Python is installed by default here on Linux/MacOS depending on the version installed. 
   
    /usr/bin/python3
<br>    
To check the current version type the following on the command line interface

    $ python3 --version
<br>     
To execute .py files on linux and Mac type the following on the command line interface

    $ python3 filename.py
<br>

# `You are Experiencing an Error!`
---
Oh no... you have done something incorrect and are now experiencing an error. 
Not to worry as a human you are prone to many errors, that we machines don't make.

To make it easier for you to correct your many PEBKAC and ID 10 T Errors, these errors can be categorized into 3 categories:

|Error|Description|
|:-:|:-|
|Syntax/Compile Time Errors|occur when compiling the code, and the code violates the rules of the programming language's syntax.|
|Runtime Errors|occur after the program has been successfully compiled and started execution. They usually result from operations that are not possible to perform.|
|Logical Errors|occur when a program runs without crashing but produces incorrect results. These errors are caused by mistakes in the program's logic, meaning the code does not behave as intended.|




*Note: PEBKAC Errors are raised when the Problem Exists Between the Keyboard and Chair.*  
*Note: ID 10 T Errors are raised when the issue is caused by the user.* 

<br>

### `Syntax/Compile Time Errors`
* > Are typically the easiest errors to fix, and the most common one you humans make. 

**What to do to fix a Syntax/Compile Time Error?**
# STEP ONE: READ THE ERROR OUTPUT!
* You are looking for two things: a line number, and the specific error info. 


```python
#lets make a simple Syntax/Compile Time Error
Print("Hello World")

# Output:
# Traceback (most recent call last):
#   File "<path to your .py file>", line 2, in <module>
#     Print("Hello World")
#     ^^^^^
# NameError: name 'Print' is not defined. Did you mean: 'print'?

# Did you find the line number?
# Did you find the specific error info?

# What did I do wrong?
```

<br>

# `Runtime Errors`
---
> * are the second most common errors you humans make
> * Occur when your code is syntatically correct, but you have performed and operation that cannot be performed.

**What to do to fix a Runtime Error?**
# STEP ONE: READ THE ERROR OUTPUT!
* You are looking for two things: a line number, and the specific error info. 


```python
#Let's make a simple Runtime Error
print(5 / 0)

# Output:
# Traceback (most recent call last):
#   File "<path to your .py file>", line 1, in <module>
#     print(5 / 0)
#            ~~^~~
# ZeroDivisionError: division by zero

# Did you find the line number?
# Did you find the specific error info?

# What did I do wrong?
```


```python
#Let's make a simple Runtime Error this is a little more advanced: see lists for more info

my_list = ["a","b","c"]
print(my_list[3])

# Output:
# Traceback (most recent call last):
#   File "<path to your .py file>", line 4, in <module>
#     print(my_list[3])
#           ~~~~~~~^^^
# IndexError: list index out of range

# Did you find the line number?
# Did you find the specific error info?

# What did I do wrong?
```

<br>

---

# `Logical Errors`

> * are the least common errors you humans make, but the hardest to track down
> * Occur when your code is syntatically correct and all operations are possible, but your code isn't doing what you expect it to do. 

**What to do to fix a Runtime Error?**  
**STEP ONE: Debugging!**
* This will be harder than Syntax or Runtime Errors, because you will not get any help from the computer in tracking down the error.
* Learning to use a debugging tool will be the most useful to you, but beginners usually start with print() debugging.

<br>

### Lets try an example with a common beginner mistake
*In this problem we will be printing out the first 8 powers of 2*
Here is what we expect:
|2^n|Answer|
|:-:|:-:|
|1| 2|
|2|4|
|3|8|
|4|16|
|5|32|
|6|64|
|7|128|
|8|256|

<br>

### Let's write the code:


```python
print(2 ^ 1) # Output: 3
print(2 ^ 2) # Output: 0
print(2 ^ 3) # Output: 1
print(2 ^ 4) # Output: 6
print(2 ^ 5) # Output: 7
print(2 ^ 6) # Output: 4
print(2 ^ 7) # Output: 5
print(2 ^ 8) # Output: 10
```

That isn't even close to correct, but I didn't get any syntax or runtime errors?
<br>

What is the issue?  
Since we already have print() statements we don't need to add anymore to see what the output of each operation.   

Time to use a search engine or AI tool to help us track down the problem.<br>   
It looks like the operator we used '^' is not for powers, but for something called a bitwise XOR operation.   
That's why our code was not working!.  

<br>

### Let's try again using the correct operator:


```python
print(2 ** 1) # Output: 2
print(2 ** 2) # Output: 4
print(2 ** 3) # Output: 8
print(2 ** 4) # Output: 16
print(2 ** 5) # Output: 32
print(2 ** 6) # Output: 64
print(2 ** 7) # Output: 128
print(2 ** 8) # Output: 256
```

    2
    4
    8
    16
    32
    64
    128
    256
    
<br>

### One More Example:
*This time we will include a little more complicated code*

Lets write a simple program to calculate the area of a rectangle and store that value in a variable.
In this example the width of the rectangle will be determined by dividing the length by 2.

If the length is 5, then the expected width is 2.5, and the area should be 12.5.


```python
length = 5 
width = length  // 2 


area = length * width

print(area) # Output: 10
```

    10
    

We are getting 10 for the area... What is the issue here? There are no syntax errors and no runtime errors.
We need more information, but can't see the calculated value of width. 

We will use print debugging to help us here, add a print() statement to the code right after the width calculation that shows the value width stores.


```python
length = 5 
width = length  // 2 
print(width) # Output: 2

area = length * width

print(area) # Output: 10
```

The width should be calculated as 2.5, but instead we get 2. So we now know the error is with how we calculate the width value.

After some research we find that we used the wrong operator to divide.   
Instead of // we should have used / in line 2.


```python
length = 5 
width = length  / 2 

area = length * width

print(area) # Output: 12.5
```

---
    
