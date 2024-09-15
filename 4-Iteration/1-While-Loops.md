# `Python While Loops`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Control Flow Statements`](#control-flow-statements)
1. [`Iteration Defined`](#iteration-defined)
1. [`Python Indentation and Code Blocks`](#python-indentation-and-code-blocks)
1. [`While Loop Syntax`](#while-loop-syntax)
1. [`The control variable`](#the-control-variable)
    1. [`Using i as a control variable`](#using-i-as-a-control-variable)
1. [`Counting with while loops`](#counting-with-while-loops)
    1. [`Ascending: Counting Up by 1 and by multiples`](#ascending-counting-up-by-1-and-by-multiples)
    1. [`Descending: Counting Down by 1 and by multiples`](#descending-counting-down-by-1-and-by-multiples)
1. [`Common Logical Errors: Infinite Loops and Off by 1 Errors`](#common-logical-errors-infinite-loops-and-off-by-1-errors)
    1. [`Infinite Loops`](#infinite-loops)
    1. [`Off by One Errors`](#off-by-one-errors)
1. [`Unique to Python: While-Else`](#unique-to-python-while-else)
1. [`Nested While Loops`](#nested-while-loops)
1. [`Break Statement`](#break-statement)
1. [`Continue Statement`](#continue-statement)
1. [`Pass Statement`](#pass-statement)
1. [`Combining Control Flow Statements`](#combining-control-flow-statements)
s

<br>

___

<br> 

# `Note on symbols used in this file`:
Symbols appearing in python blocks should be treated as Python syntax.  
`...` is used as a placeholder in Python. 
```python 
... 
```

<br>

### `Variable Information`
> Text inside of `<>` should be treated as a place holder for variable information
```
  <text>    
```

<br>

### `CLI Commands`
> The `>` indicates commands to be executed in the Windows Powershell prompt
```
  > command flags arguments 
```

<br>


> The `$` indicates commands to be executed in the Linux or Mac command line interface
```
  $ command flags arguments
```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Control Flow Statements`
`Control flow statements` are constructs in programming languages that control the order in which instructions or statements are executed.

### `Control Flow Statements in Python`
1. Conditional Statements: `if`, `elif`, `else`
1. Looping: `for`, `while`
1. Loop Control: `break`, `continue`, `pass`
1. Function Control: `return`
1. Exception Handling: `try`, `except`, `finally`, `raise`
1. Context Management: `with`
1. Assertions: `assert`

| Control Flow Statement | Description                                                                 |
|:-:|:-|
| `if`                   | Executes a block of code if a specified condition is true.                   |
| `elif`                 | Checks another condition if the previous `if` condition is false.            |
| `else`                 | Executes a block of code if all preceding conditions are false.              |
| `for`                  | Iterates over a sequence (like a list, tuple, string, etc.).                 |
| `while`                | Repeats a block of code as long as a condition is true.                      |
| `break`                | Exits the nearest enclosing loop immediately.                               |
| `continue`             | Skips the current iteration of the loop and continues with the next one.     |
| `pass`                 | Does nothing; used as a placeholder for future code.                        |
| `return`               | Exits a function and optionally returns a value.                            |
| `try`                  | Defines a block of code to test for errors during execution.                 |
| `except`               | Catches and handles exceptions (errors) that occur in the `try` block.       |
| `finally`              | Executes code whether or not an exception occurred in the `try` block.       |
| `raise`                | Manually raises an exception.                                                |
| `with`                 | Used to wrap the execution of a block of code within context management.     |
| `assert`               | Tests a condition, and if it's false, raises an `AssertionError`.            |

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Iteration Defined`
Basically: `Iterate` means to loop or repeat

Specifically: `Iteration` is the process of repeating a set of instructions or operations in a sequence, typically within a loop

<br>

`Iterables` are data types that can return their values one at a time


Iterable Types include, but are not limited too:
| Type        | Class/Definition                                       |
|-------------|--------------------------------------------------------|
| Strings     | `<class 'str'>`                                        |
| Lists       | `<class 'list'>`                                       |
| Tuples      | `<class 'tuple'>`                                      |
| Sets        | `<class 'set'>`                                        |
| Dictionaries| `<class 'dict'>`                                       |
| Iterators   | Classes that implement the `__iter__` method           |
| Generators  | A function that returns an iterator                    |

Example of other iterable types in Python:
|Type|
|:-|
|range  |
|bytes |
|bytearray  |
|frozenset  |
|collections.deque  |
|collections.namedtuple  |
|collections.OrderedDict  |
|collections.defaultdict  |
|collections.ChainMap  |
|collections.Counter  |
|collections.UserDict  |
|collections.UserList  |
|collections.UserString  |
|files (file objects)  |
|generator objects |

<br>

Instead of this:
```python
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
```

Try these:

`While Loops (Iteration)`
```python
num = 1
while (num <= 10):
    print(num, end = " ")
    num += 1

#Output: 1 2 3 4 5 6 7 8 9 10 
```

`For Loops (Iteration)`
```python
for num in range(1,11,1):
    print(num, end = " ")

#Output: 1 2 3 4 5 6 7 8 9 10 
```

`Functions (Recursion)`
```python
def count(num, stop, step = 1): #Function Definition
    if num <= stop:
        print(num)
        num += 1
        count(num,stop,step)
    return

count(1,10) #Function Call

#Output: 1 2 3 4 5 6 7 8 9 10 
```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Python Indentation and Code Blocks`
Python syntax uses `indentation` to define the scope of blocks of code.

`Code blocks` are groups of statements that are executed together as a unit.
> Each indentation level represents a higher level of code structure (conditionals, loops, functions, classes)

> All statements within the same block must have the same level of indentation.

> Indent 4 spaces to create a code block.  

> The end of a block is indicated by the decrease in indentation level. 

*Note*:   
`Scope/Context` is the area of a program in which a block of code exists and executes.

<br>

*Notes:*  
> *`Indentation` is typically achieved using spaces or tabs.* 

> *Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior.*  

> *Python 3 disallows mixing tabs and spaces for indentation in the same source file.* 

> *If you are using an editor like VScode using the tab key, and spaces is not a problem.*

<br>

### `Python Indentation Examples:`
```python
condition = True or False

if(condition):
    #--> start of the if code block (scope/context)
    print("Inside the if statement")                    
                                                        
#<-- end of the if code block (scope/context)
```
```python
condition = True or False

while(condition):
    #--> start of the while code block (scope/context)
    print("Inside the while loop")

#<-- end of the while code block (scope/context)
```
```python
for _ in range(10):
    #--> start of the for code block (scope/context)
    print("Inside the for loop")

#<-- end of the for code block (scope/context)
```
```python
def function():
    #--> start of the function definition code block (scope/context)
    print("Inside of the function definition")

#<-- end of the function definition code block (scope/context)
```
```python
class Example():
    #--> start of the Class definition code block (scope/context)

    def __init__(self):
        #--> start of the Class Constructor Definition code block (scope/context)
        print("Inside the Class, inside the constructor")

    #<-- end of the Class Constructor Definition code block (scope/context)
#<-- end of the Class Definition code block (scope/context)
```

<br>

## `Nested Indentation: Blocks inside of Blocks`
`Indentation` defines the level of the code block when nesting constructs.

*Note*: 
> Most code editors like VS Code will provide a line to help you keep track of the beginning and end of your code blocks*


```python
class Example():
    #--> start of class code block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def function():                                                     #
        #--> start of function code block###########################    #
        for _ in range(5):                                         #    #
            #--> start of for code block++++++++++++++++++++++#    #    #
            while(condition):                                 #    #    #
                #--> start of while code block============#   #    #    #      
                if(condition):                            #   #    #    #
                    #--> Start of if code block ------#   #   #    #    #
                    print("So many indents!")         #   #   #    #    #
                #<-- end of if code block-------------#   #   #    #    #
            #<-- end of while code block==================#   #    #    #
        #<-- end of for code block++++++++++++++++++++++++++++#    #    #
    #<-- end of function code block#################################    #
#<-- end of class code block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
```

<br>

[Back to Top](#python-while-loops)

___

<br>


# `While Loop Syntax`
Basically: `While Loops` are a block of code that repeats while a condition is True

Specifically: `While Loops` are a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. 
> * While loops are typically used when the number of iterations is not fixed.

The `while` keyword defines the start of a while loop.
> each new `while` is independent

<br>


while loop syntax:
```
while(condition):
    <Code Block to Repeat>
    ...
```
```python
condition = True or False

while(condition):
    #--> indent 4 spaces to be inside of the loop block (scope/context)
    'repeat this code block'
#<-- unindent 4 spaces to exit the loop block (scope/context)
```
```python
condition = True or False
#------------------------------------#
while(condition): #-------------#    #
    'repeat this code block'    #    #
    #---------------------------#    #
#------------------------------------#
```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `The control variable`
Basically: A `control variable` is a variable used to determine when the loop stops

Specifically: A `control variable` is a variable that is used to regulate the execution flow of a loop or a conditional statement within a program


> * A `control variable` is used to control the number of loops

> * While loops commonly result in a logical error called an `infinite loop`, where the loop continues indefinitely.

> * While loops also commonly deal with runtime and logical `off by one errors`.

```python
count = 0 #this is the control variable

while count < 5: #stops the loop when count is >= 5
    'repeat this code'
    count = count + 1 #increases count each time the loop occurs

#pay attention to the indentation
```
```python
count = 0 #this is the control variable

while count < 5: #stops the loop when count is >= 5
    'repeat this code'
    count += 1 # shorthand for count = count + 1

#pay attention to the indentation
```

<br>

## `Using i as a control variable`
The use of the letter `i` as a control variable in loops is a long-standing convention in programming.   

> * This practice dates back to early computing and mathematical notation, where `i` often represents an index or iterator.

These following letters are commonly used as control variables:
> * `i`
> * `j`
> * `k`
> * `n`

<br>

example:
```python
i = 0 

while(i < 10):
    print(i, end = " ")
    i += 1

#Output: 0 1 2 3 4 5 6 7 8 9
```
```python
i = 0
while(i < 2):

    j = 0
    while(j < 2):

        k = 0
        while(k < 2):
            print(i,j,k, end = ", ")
            k += 1
        j += 1
    i +=1
    print()

# Output:
# 0 0 0, 0 0 1, 0 1 0, 0 1 1, 
# 1 0 0, 1 0 1, 1 1 0, 1 1 1, 
```

<br>

[Back to Top](#python-while-loops)

___

<br>


# `Counting with while loops`
It is often important to keep track of what loop the `while loop` is currently on, in order to control how many times the loop executes. This loop count can also be used within the loop itself. 

Use a `control variable`, and define the start, stop, and step of the loop. This will control the number of times the `while loop` executes before stoping. 

```python
start = ...    # start: where to start counting
stop =  ...    # stop: where to stop counting
step =  ...    # step: how much to increase or decrease by each time


count = start
while(count < stop):        #can be > < >= or <= step

    count = count + step    # can be + - * / % ...

```

```python
start = ...    # start: where to start counting
stop =  ...    # stop: where to stop counting
step =  ...    # step: how much to increase or decrease by each time


count = start
while(count < stop):        #can be > < >= or <= step

    count += step           #can be += -= *= /= ... 
    # using compound assignment operators
```

example:
```python 
count = 1
while(count < 10):
    print(count, end = " ")
    count += 1

#Output: 1 2 3 4 5 6 7 8 9
```

<br>

## `Ascending: Counting Up by 1 and by multiples`
examples:
```python
'From 0 to Positive By 1s'
i = 0                       # start at 0
while(i < 5):               # stop when i is 5  (i <= 4)
    print(i, end = " ")     #print out i with a space at the end
    i += 1                  # step  increment i by 1

# Output: 0 1 2 3 4 
```
```python
'From 0 to Positive By Multiples'
i = 0                       # start at 0
while(i < 5):               # stop when i is 5  (i <= 4)
    print(i, end = " ")     #print out i with a space at the end
    i += 2                  # step  increment i by 2

# Output: 0 2 4 
```
```python
'From 1 to Positive by 1s'
#From 1 to positive
i = 1                       # start 
while (i < 6):              # stop (i <= 5)
    print(i, end = " ")
    i += 1                  # step  increment i by 1

# Output: 1 2 3 4 5 
```
```python
'From 1 to Positive by Multiples'
i = 1                       # start 
while (i < 6):              # stop (i <= 5)
    print(i, end = " ")
    i += 3                  # step  increment i by 3

# Output: 1 4 
``` 
```python
'From Positive to Positive by 1s'
i = 10                      # start
while( i < 21):             # stop (i <= 20)
    print(i, end = " ")
    i+=1                    # step  increment i by 1

# Output: 10 11 12 13 14 15 16 17 18 19 20 
```
```python
'From Positive to Positive by Mutliples'
i = 10                      # start
while( i < 21):             # stop (i <= 20)
    print(i, end = " ")
    i+=5                    # step increment i by 5

# Output: 10 15 20 
```  
```python
'From Negative to 0 by 1s'
i = -5                      # start
while(i < 1):               # stop (i <= 0)
    print(i, end = " ")
    i+=1                    # step increment i by 1

# Output: -5 -4 -3 -2 -1 0 
```
```python
'From Negative to 0 by Multiples'
i = -5                      # start
while(i < 1):               # stop (i <= 0)
    print(i, end = " ")
    i+=3                    # step increment i by 3

# Output: -5 -2 
```
```python
'From Negative to Negative by 1s'
i = -10                     # start
while(i < -4):              # stop (i <= -5)
    print(i, end = " ")
    i+=1                    # step increment i by 1

# Output: -10 -9 -8 -7 -6 -5 
```
```python
'From Negative to Negative by Multiples'
i = -10                     # start
while(i < -4):              # stop (i <= -5)
    print(i, end = " ")
    i+= 3                   # step increment i by 3

# Output: -10 -7 
```
```python
'From Negative to Positive by 1s'
i = -3                      # start
while(i < 4):               # stop (i <= 3)
    print(i, end = " ")
    i+=1                    # step increment i by 1

# Output: -3 -2 -1 0 1 2 3 
```

```python
'From Negative to Positive by Multiples'
i = -3                      # start
while(i < 4):               # stop (i <= 3)
    print(i, end = " ")
    i+= 2                   # step increment i by 2

# Output: -3 -1 1 3
```  

<br>

## `Descending: Counting Down by 1 and by multiples`
```python
'From Positive to 0 by 1s'
i = 10                      # start
while(i > -1):              # stop (i >= 0)
    print(i, end = " ")
    i -= 1                  # step
# Output: 10 9 8 7 6 5 4 3 2 1 0 
```
```python
'From Positive to 0 by Multiples'
i = 10                      # start
while(i > -1):              # stop (i >= 0)
    print(i, end = " ")
    i -= 3                  # step
# Output: 10 7 4 1 
``` 

```python
'From Positive to Positive by 1s'
i = 50                      # start
while(i > 39):              # stop (i >= 40)
    print(i, end = " ")
    i -= 1                  # step
# Output: 50 49 48 47 46 45 44 43 42 41 40 
```
```python
'From Positive to Positive by Multiples'
i = 50                      # start
while(i > 39):              # stop (i >= 40)
    print(i, end = " ")
    i -= 3                  # step
# Output: 50 47 44 41 
```
```python
'From Positive to Negative by 1s'
i = 5                       # start
while(i > -2):              # stop (i >= -1)
    print(i, end = " ")
    i -= 1                  # step
# Output: 5 4 3 2 1 0 -1 
```
```python
'From Positive to Negative by Multiples'
i = 5                       # start
while(i > -2):              # stop (i >= -1)
    print(i, end = " ")
    i -= 4                  # step
# Output: 5 1 
```
```python
'From 0 to Negative by 1s'
i = 0                       # start
while(i > -7):              # stop (i >= -6)
    print(i, end = " ")
    i -= 1                  # step
# Output: 0 -1 -2 -3 -4 -5 -6 
```
```python
'From 0 to Negative by Multiples'
i = 0                       # start
while(i > -7):              # stop (i >= -6)
    print(i, end = " ")
    i -= 3                  # step
# Output: 0 -3 -6 
```
```python
'From Negative to Negative by 1s'
i = -6                      # start
while(i > -15):             # stop (i >= -14)
    print(i, end = " ")
    i -= 1                  # step
# Output: -6 -7 -8 -9 -10 -11 -12 -13 -14 
```
```python
'From Negative to Negative by Multiples'
i = -6                      # start
while(i > -15):             # stop (i >= -14)
    print(i, end = " ")
    i -= 4                  # step
# Output: -6 -10 -14 
```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Common Logical Errors: Infinite Loops and Off by 1 Errors`

<br>

## `Infinite Loops`
Basically: `Infinite Loops` occur when the condition never becomes False.

Specifically An `Infinite Loop` is a loop that continues to execute indefinitely because the terminating condition is never met or because there is no condition that ends the loop.

<br>

*Infinite Loops are considered logical errors, because the syntax of the code is correct, but the code does not work as intended.*


Examples:
```python
condition = True
while (condition):
    print("This is an infinite loop!")
```

```python
i = 0
while (i < 10):
    print("This is an infinite loop")
```
```python
i = 5
while( i > 0):
    print("This is an infinite loop")
    i+=1

# Output: 5 6 7 8 9 .....
```

<br>


## `Off by One Errors`
Basically: `Off by One Errors` result from counting 1 to many or 1 to few times


Specifically: `Off by One Errors` occur when an iterative loop executes one too many or one too few times typically due to incorrect indexing or boundary conditions.

*Off by One Errors are considered logical errors, but often cause runtime errors such as `IndexError: list index out of range`.*

<br>

Examples:
```python
# count from 0 to 5
i = 0
while (i < 5):
    print(i, end = " ")
    i+=1

# Output: 0 1 2 3 4 
# Off by 1, only counts from 0 to 4
```

<br>

[Back to Top](#python-while-loops)

___

<br>


# `Unique to Python: While-Else`

`while-else` statements attach an `else` block that only executes if the loop completes normally without encountering a `break` statement.

The `else` block runs only one time, after the condition is False.

syntax:
```
for variable in iterable:
    ...
else:
    ...
```
```python
#when the condition is no longer true run the else
i = 1
while(i <= 5):
    print(i, end = " ")
    i+=1
else: #when i becomes 6 this block runs
    print("Finished Counting")

# Output: 1 2 3 4 5 Finished Counting
```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Nested While Loops`
`Nesting` refers to the placement of one or more constructs with another construct of the same type. 

Placing one or more while loops inside of another creates a `nested while loop`.

> The inner while loop executes completely for every 1 iteration of the outer loop.

<br>

Placing one while loop inside another while loop.

syntax:
```
while(first_condition):
    
    while(second_condition):
        ...
    
    ...
```
```python
outer_start = ...; outer_stop = ...; outer_step = ...
inner_start = ...; inner_stop = ...; inner_step = ...


repeat = outer_start
while(repeat < outer_stop):#Outer Loop------------#
                                                  #
    count = inner_start                           #
    while(count < inner_stop):#Inner loop--#      #
        print(count, end = " ")            #      #
        count += inner_step                #      #
    #--------------------------------------#      #
    repeat += outer_step                          # This is apart of the outer loop
#-------------------------------------------------#
```

example:
```python
#Example count to 5, 3 times
repeat = 0
while(repeat < 3):
    print(repeat)

    count = 0
    while(count < 6):
        print(repeat, count, end = " ")
        count += 1
    
    repeat += 1
    print()

# Output:
# 0
# 0 1 2 3 4 5
# 1
# 0 1 2 3 4 5
# 2
# 0 1 2 3 4 5
```

<br>

[Back to Top](#python-while-loops)

___

<br>


# `Break Statement`
Basically: A `break` statement is used to end a loop early

Specifically: A `break` statement is used to exit (or "break out of") the loop prematurely. 

`break` is commonly used within loops like `for` and `while` to interrupt the loop's execution based on a certain condition.

```python
while(True):
    break
#the loop will exit on the first loop
```

example:
```python
count = 0

while True:
    print(count, end = " ")
    count += 1
    
    if count >= 5:
        print("Count has reached 5, breaking out of the loop.")
        break
```

```python
'Guessing Game'

secret_num = 10
user_guess = None

while(user_guess != secret_num):
    try:
        user_guess = int(input("Enter your guess:"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if(user_guess == secret_num):
        print("YOU WIN")
        break
    
    print("GUESS AGAIN")

```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Continue Statement`
Basically: `continue` is a statement that skips the rest of code block in the current loop.

Specifically:`continue` is a statement used to skip the rest of the code inside a loop for the current iteration, and continue with the next iteration of the loop.


```python
while(condition):
    continue
```

example:
```python
i = 0
while(i <= 100):
    if(i % 3 == 0):
        i+=1
        continue

    print(i, end = " ")
    i+=1

# Skips all numbers divisible by 3 between 0 and 100. 
# Output: 1 2 4 5 7 8 10 .....
```

```python
'Guessing Game'

secret_num = 10
user_guess = None

while(user_guess != secret_num):
    try:
        user_guess = int(input("Enter your guess:"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if(user_guess == secret_num):
        print("YOU WIN")
        break
    
    print("GUESS AGAIN")

```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Pass Statement`
Basically: `pass` is a placeholder

Specifically: `pass` is a placeholder statement that does nothing when executed, and preserves the syntax of Python to allow the code to run.  

`pass` is used when a statement is required syntactically but no action is needed. This can be useful in situations where code is being written incrementally, or when a function or loop is meant to be implemented later.

example:
```python
while(condition):
    pass
```

<br>

[Back to Top](#python-while-loops)

___

<br>

# `Combining Control Flow Statements`
`Control flow statements` such as `if`, `while`, and `for` can be combined to preform more complex algorithms.

examples:
```python
counter = 1
while counter <= 10:
    if counter % 2 == 0:
        print(f"{counter} is even")
    else:
        print(f"{counter} is odd")
    counter += 1
```

```python
correct_password = "python123"
while True:
    password = input("Enter the password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password, try again")
```

```python
num = 29
i = 2
while i < num:
    if num % i == 0:
        print(f"{num} is not a prime number")
        break
    i += 1
else:
    print(f"{num} is a prime number")
```

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 0
while row < len(matrix):
    for element in matrix[row]:
        print(element, end=' ')
    print()  # Newline for each row
    row += 1
```
```python
run = True

while(run):

    user_in = input("@lwm:/$ ").split(" ")

    match user_in[0]:
        case "echo":
            print(user_in[1])
        case "exit":
            run = False
        case _ :
            print(f"{user_in} is not a recognized command.")
```

<br>

[Back to Top](#python-while-loops)

___

<br>

*Created and maintained by Mr. Merritt* 