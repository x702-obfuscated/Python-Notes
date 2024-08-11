*Use CTRL + F to search for keywords in this file*
# <table><th>`Python While Loops`</th></table>
___

**Covered in this file:**
```
1. Iteration Defined
2. Python indentation and Code Blocks
3. While Loop Syntax
4. Using a Control Variable
5. Counting with while loops
6. Ascending: Counting Up by 1 and by multiples
7. Descending: Counting Down by 1 and by multiples
8. Run Time Errors: Infinite Loops and Off by 1 Errors
9. Unique to Python: While-Else
10. Nested While Loops
11. Break, Continue, and Pass Keywords
12. Combining Control Structures
```
## Note on symbols used in this file:
> Symbols appearing in python blocks should be treated as Python syntax.  
>... is used a placeholder in Python. 
```python 
... 
```

### Variable Information
> Text inside of <> should be treated as a place holder for variable information
```
  <text>    
```

### CLI Commands
> The > indicates commands to be executed in the Windows Powershell prompt
```
  > command flags arguments 
```
> The $ indicates commands to be executed in the Linux or Mac command line interface
```
  $ command flags arguments
```

## <table><th>`Iteration Defined`</th></table>
___
**Iteration:**
> * basically: means to loop or repeat
> * specifically: the process of repeating a set of instructions or operations in a sequence, typically within a loop

**Iterables**
> * are data types that can return their values one at a time


Iterable Types include, but are not limited too:
```
*   Strings <class 'str'>
*   Lists <class 'list'>
*   Tuples <class 'tuple'>
*   Sets <class 'set'>
*   Dictionaries <class 'dict'>
*   Iterators (classes that implement the \_\_iter\_\_ method)
*   Generators (a function that returns an iterator)
```
Example of other iterable types in Python:
```  
*   range  
*   bytes 
*   bytearray  
*   frozenset  
*   collections.deque  
*   collections.namedtuple  
*   collections.OrderedDict  
*   collections.defaultdict  
*   collections.ChainMap  
*   collections.Counter  
*   collections.UserDict  
*   collections.UserList  
*   collections.UserString  
*   files (file objects)  
*   generator objects 

``` 

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

* While Loops (Iteration)


```python
num = 1
while (num <= 10):
    print(num, end = " ")
    num += 1

#Output: 1 2 3 4 5 6 7 8 9 10 
```

* For Loops (Iteration)


```python
for num in range(1,11,1):
    print(num, end = " ")

#Output: 1 2 3 4 5 6 7 8 9 10 
```

* Functions (Recursion)


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

## <table><th>`Python Indentation and Code Blocks`<th></table>
___

**Python syntax uses indentation to define the scope of blocks of code.**   
**Code blocks are groups of statements that are executed together as a unit.**
> * Each indentation level represents a higher level of code structure (conditionals, loops, functions, classes)
> * All statements within the same block must have the same level of indentation.
> * Indent 4 spaces to create a code block.  
> * The end of a block is indicated by the decrease in indentation level. 

> *Note: Scope is the area of a program in which a block of code exists and executes.*  
<br>

> *Notes:*  
> * *Indentation is typically achieved using spaces or tabs.* 
> * *Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior.*   
> * *Python 3 disallows mixing tabs and spaces for indentation in the same source file.*  
> * *If you are using an editor like VScode using the tab key, and spaces is not a problem.*   

  



### Python Indentation Abstract Examples:


```python
condition = True or False

if(condition):
    #start of the if code block (scope/context)
    print("Inside the if statement")                    
                                                        
#end of the if code block (scope/context)
```


```python
condition = True or False

while(condition):
    #start of the while code block (scope/context)
    print("Inside the while loop")

#end of the while code block (scope/context)
```


```python
for _ in range(10):
    #start of the for code block (scope/context)
    print("Inside the for loop")

#end of the for code block (scope/context)
```


```python
def function_():
    #start of the function definition code block (scope/context)
    print("Inside of the function definition")

#end of the function definition code block (scope/context)
```


```python
class Class_():
    #start of the Class definition code block (scope/context)

    def __init__(self):
        # start of the Class Constructor Definition code block (scope/context)
        print("Inside the Class, inside the constructor")

    # end of the Class Constructor Definition code block (scope/context)
# end of the Class Definition code block (scope/context)
```

### Nested Indentation: Blocks inside of Blocks
***Indentation defines the level of the code block when nesting constructs***

*Note: Most code editors like VS Code will provide a line to help you keep track of the beginning and end of your code blocks*


```python
class Example():
    def example_():
        for _ in range(5):
            while(condition):
                if(condition):
                    print("So many indents!")
```

```python
class Example():#start of class code block~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def example_():                                                 #
        #start of function code block###########################    #
        for _ in range(5):                                     #    #
            #start of for code block++++++++++++++++++++++#    #    #
            while(condition):                             #    #    #
                #start of while code block============#   #    #    #      
                if(condition):                        #   #    #    #
                    #Start of if code block ------#   #   #    #    #
                    print("So many indents!")     #   #   #    #    #
                #end of if code block-------------#   #   #    #    #
            #end of while code block==================#   #    #    #
        #end of for code block++++++++++++++++++++++++++++#    #    #
    #end of function code block#################################    #
#start of class code block~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
```
## <table><th>`While Loop Syntax`</th></table>
___
**While Loops:**
> * basically: a block of code that repeats while a condition is True
> * specifically: a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. 
> * use: used are typically used when the number of iterations is not fixed.

> * the *while* keyword defines the start of a while loop


while loop syntax:
```
while(condition):
    <Code Block to Repeat>
    ...
```
```python
condition = True or False

while(condition):
    #indent 4 spaces to be inside of the loop block (scope/context)
    'repeat this code block'
#unindent 4 spaces to exit the loop block (scope/context)
```
```python
condition = True or False
#------------------------------------#
while(condition): #-------------#    #
    'repeat this code block'    #    #
    #---------------------------#    #
#------------------------------------#
```

## <table><th>`The control variable`</th></table>
___
**Control Variable**
> * basically: a variable used to determine when the loop stops
> * specifically: a variable that is used to regulate the execution flow of a loop or a conditional statement within a program

> * use: a control variable is used to control the number of loops
> * errors: runtime infinite loop errors can occur.
> * errors: runtime and logical off by one errors can occur.

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

## <table><th>`Counting with while loops`</th></table>
---

**Use a control variable, and define the start, stop, and step of the loop.**  

abstract examples
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

## <table><th>`Ascending: Counting Up by 1 and by multiples`</th></table>
> * The use of the letter i as a control variable in loops is a long-standing convention in programming.   
> * This practice dates back to early computing and mathematical notation, where i often represents an index or iterator.

These following letters are commonly used as control variables:
> * i
> * j
> * k
> * n

real counting examples:
```python
'0 to Positive By 1s'
i = 0                       # start at 0
while(i < 5):               # stop when i is 5  (i <= 4)
    print(i, end = " ")     #print out i with a space at the end
    i += 1                  # step  increment i by 1

# Output: 0 1 2 3 4 
```
```python
'0 to Positive By Multiples'
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

## <table><th>`Descending: Counting Down by 1 and by multiples`</th></table>

real counting examples:
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

## <table><th>`Run Time Errors: Infinite Loops and Off by 1 Errors`</th></table>
___

**Infinite Loops**
> * basically: occurs when the condition is never False
> * specifically: a loop that continues to execute indefinitely because the terminating condition is never met or because there is no condition that ends the loop.
> * error type: run time


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


**Off by One Errors**
> * basically: counting 1 to many or 1 to few times
> * specifically: occurs when an iterative loop executes one too many or one too few times typically due to incorrect indexing or boundary conditions.
> * error type: runtime or logical

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
## <table><th>`Unique to Python: While-Else`</th></table>

**while-else***
> * Python allows for an else block to be attached to a while block.  
> * The else only executes if the loops completes normally without encountering a break statement.
> * The else block runs only one time, once the condition is false

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
## <table><th>`Nested While Loops`</th></table>

**Nested While Loops**
> * one while loop placed inside of another.
> * the inner loop executes completely for every 1 iteration of the outer loop.


Placing one While Loop into another While Loop\

syntax:
```
while(first_condition):
    
    while(second_condition):
        ...
    
    ...
```

abstract example:
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

real example:
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


## <table><th>`Break, Continue, and Pass Keywords`</th></table>

## Break
**break**
> * basically: statement used to end a loop early
> * specifically: statement used to exit (or "break out of") the loop prematurely. 

> * use: commonly used within loops like for and while to interrupt the loop's execution based on a certain condition.

abstract example
```python
while(True):
    break
#the loop will exit on the first loop
```

real examples
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

## Continue

**continue**
> * basically: a statement that skips the rest of code block in the current loop.
> * specifically: a statement used to skip the rest of the code inside a loop for the current iteration, and continue with the next iteration of the loop.

abstract example
```python
while(condition):
    continue
```

real example
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

## Pass
**pass**
> * basically: is a placeholder
> * specifically:  is a placeholder statement that does nothing when executed. 

> * use: used when a statement is required syntactically but no action is needed. This can be useful in situations where code is being written incrementally, or when a function or loop is meant to be implemented later.


abstract example:
```python
while(condition):
    pass
```

## <table><th>`Combining Control Flow Statements`</th></table>
> * control flow statements like if, while, and for can be combined to preform more complex algorithms

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