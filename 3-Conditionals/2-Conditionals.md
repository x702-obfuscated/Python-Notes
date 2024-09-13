# `Python Conditionals`

___

Covered in this file:
1. [`Note on Boolean Expressions and Conditionals`](#note-on-boolean-expressions-and-conditionals)
1. [`Review: Booleans, Relational, Membership, Identity, and Logical Operators`](#review-booleans-relational-membership-identity-and-logical-operators)
    1. [`Booleans (True/False)`](#booleans-truefalse)
    1. [`Comparison aka Relational Operators`](#comparison-aka-relational-operators)
    1. [`Identity Operators`](#identity-operators)
    1. [`Membership Operators`](#membership-operators)
    1. [`Logical Operators`](#logical-operators)
    1. [`Abbreviated Operator Precedence`](#abbreviated-operator-precedence)
1. [`Truthiness: Special Note on Evaluating Boolean Expressions`](#truthiness-special-note-on-evaluating-boolean-expressions)
1. [`Python Indentation and Code Blocks`](#python-indentation-and-code-blocks)
1. [`if statements`](#if-statements)
1. [`elif statements`](#elif-statements)
1. [`else statements`](#else-statements)
1. [`if-elif-else Chained Conditional Statements`](#if-elif-else-chained-conditional-statements)
1. [`Nested Conditionals`](#nested-conditionals)
1. [`Ternary Operators: Shorthand Conditionals`](#ternary-operators-shorthand-conditionals)
1. [`Match Statements`](#match-statements)
    1. [`Combining Patterns`](#combining-patterns)
    1. [`Adding a Guard`](#adding-a-guard)


<br>


___

<br>


# `Note on Boolean Expressions and Conditionals`
*When it comes to boolean expressions and conditional statements, the range of possibilities is vast and varied. The examples provided here are intended to illustrate some of the fundamental concepts and common use cases. However, it is impossible to cover every possible scenario or combination of conditions that may arise in real-world programming.*

<br>

[Back to Top](#python-conditionals)

___

<br>


# `Review: Booleans, Relational, Membership, Identity, and Logical Operators`
Conditionals often utilize Booleans, Relational, Membership, Identity, and Logical Operators in order to determine what block of code should be executed.

<br>

## `Booleans (True/False)`
* Booleans are a data with only two states, typically True or False


```python
True
False
```

<br>

## `Comparison aka Relational Operators `
`Comparison operators` are used to compare two values.
> * they evaluate to a boolean value (True/False)
> * Order of Operations is Left to Right

|Symbol| Inequality Operation      |
|:----:|:-------------------------:|
|   `>`  | greater than              |
|   `<`  | less than                 |
|  `>=`  | greater than or equal to  |
|  `<=`  | less than or equal to     |
|  `==`  | equal to                  |
|  `!=`  | not equal to              |

<br>

## `Identity Operators`
`Identity Operators` check if the memory location of the two objects are identical

|Symbol| Identity Operation |
|:----:|:------------------:|
|`is`    |identical to        |
|`is not`|not identical       |

<br>

## `Membership Operators`
`Membership operators` check if a value is found in a sequence
> * ie. checks if one thing is 'apart of' another

|Symbol |Membership Operation|
|:-----:|:------------------:|
|`in`    |apart of            |
|`not in` |not apart of        |

<br>



## `Logical Operators`
|Operator| Operation| Description|Shorthand|
|:------:|:--------:|:-----------:|:----:|
| `not`    | NOT      | opposite   | not T --> F, not F --> T|
| `and`    | AND      | both       | T and T --> T, all others F|
| `or`     | OR       | at least one | F or F --> F, all others T|

<br>


## `Abbreviated Operator Precedence`
*Operations at the same level proceed from left to right*
|Operators|Description|
|:-:|:-:|
| `==` `!=` `>` `>=` `<` `<=`  | Comparisons|
| `is` `is not`      | Identity|
| `in` `not in`   | Membership operators |
| `not`         | Logical NOT        |
| `and`         | Logical AND        |
| `or`          | Logical OR         |

<br>

[Back to Top](#python-conditionals)

___

<br>

# `Truthiness: Special Note on Evaluating Boolean Expressions:`
When writing if statments you will often get output, sometimes even correct output, but your code does not work as intended in every case. 
This is because your code is syntatically correct, and even at run time the code will execute without error.

<br>

**You have unfortunaly made a `Logical Error`, that may be hard to track down because of how Python interprets the "truthiness" of certain data.**
**Below illustrates how Python treats the truthiness of certain data:**

`Truthiness` refers to the evaluation of an object's value in a boolean context, ie. determining whether it is considered true or false.*
|Data Type| Truthiness|
|:-:|:-:|
|`Integers`, `Floats`|Any non-zero number (integer, float) is evaluated as True|
|`Strings`, `Lists`, `Tuples`, `Sets`, `Dictionaries`|Any non-empty string, list, tuple, set, or dictionary, is evaluated as True|
|`Functions`, `Methods`, `Lambdas`, `Classes`|Any function, method, lambda or class is evaluated as True|
|`Objects`|By default objects are evaluated True, but how an object is evaluated can be changed|


*Note on Errors:*  
> *`Syntax/Compile Time Errors`: occur when compiling the code, and the code violates the rules of the programming language's syntax.*  

> *`Runtime Errors`: occur after the program has been successfully compiled and started execution. They usually result from operations that are not possible to perform.* 

> *`Logical Errors`: occur when a program runs without crashing but produces incorrect results. These errors are caused by mistakes in the program's logic, meaning the code does not behave as intended.*  

<br>

[Back to Top](#python-conditionals)

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

[Back to Top](#python-conditionals)

___

<br>

# `if Statements`
Basically: `if statements` determine if  code block is executed based on truth of a condition.

Specifically: `if statements` are a control flow statement that allows you to execute a block of code only if a specified condition is true. If the condition evaluates to false, the code block is skipped.

<br>

`if statements` provide a way to make decisions in programs

syntax:

    if(condition):
        Code block to execute if the condition is True 
        ...

> * If the condition is True the code block executes
> * If the condition is False the code block is skipped.
> * Each new `if` is a new `if statement` independant of any other `if statement`

<br>

```python
condition = True or False

#the condition in parenthesis is a boolean expression
if(condition):  #end with a colon ":"
    #--> indent 4 spaces to be inside the if code block
    'Code Block Here'

#<-- unident 4 spaces to be outside the if code block
```
```python
#------------------------------------------------------#
if(condition): #------------------------------------#  #
    'runs this block when the condition is True'    #  #
    'skips this block when the condition if False'  #  #
    #-----------------------------------------------#  #
#------------------------------------------------------#
```

```python
if(True): #----------#        
    'run this block' # 
#--------------------#
```

```python
if(False): #----------#
    'skip this block' # 
#---------------------#
```
<br>

Each new `if` is independent
```python
if(True): #----------#        
    'run this block' # 
#--------------------#

if(False): #----------#
    'skip this block' # 
#---------------------#
#^^^^^^^^^^^^^^^^^^^^^^
#This if is not effected by the one above it.
```

<br>

examples:
```python
age = 20
if (age >= 18):
    print("You are an adult.")

print("This is outside the if block.")
```


```python
fruits = ["apple", "banana", "cherry"]
if ("banana" in fruits):
    print("Banana is in the list.")

print("This is outside the if block.")
```


```python
x = 10
y = 10
if (x == y):
    print("x is equal to y.")

print("This is outside the if block.")
```


```python
num = 25
if (num > 20 and num < 30):
    print("num is between 20 and 30.")

print("This is outside the if block.")
```


```python
a = [1, 2, 3]
b = a
if (a is b):
    print("a and b refer to the same object.")

print("This is outside the if block.")
```

<br>

[Back to Top](#python-conditionals)

___

<br>

# `elif Statements`
Basically: `elif statements`, short for 'else if', are additional `if` statements that depend on the `if` and `elif` statements that come before it. 

Specifically: An `elif statement` is a conditional branch that provides an alternative condition to be checked if the preceding `if` and `elif` statements evaluate to False. 

> `elif` statements allows multiple mutually exclusive conditions to be evaluated sequentially, where only the first True condition will execute its corresponding block of code.

> Each `elif` statement depends on the preceding `if` or `elif`conditions, meaning that it will only be evaluated if all prior conditions have been False

<br>

An `elif statement` cannot be used by itself; it must always be used in conjunction with an `if statement`. Multiple `elif` statements can follow an `if` statement and precede an `else` statement.


syntax:
```
if(condition1): 
    Code block to execute if condition1 is True 
    ... 
elif(condition2): 
    Code block to execute if condition1 is False and condition2 is True 
    ... 
elif(condition3): 
    Code block to execute if all previous conditions are False and condition3 is True
    ... 
...
```
> * The `if` statement's condition is checked first.
> * If the `if` condition is `False`, the `elif` conditions are checked in order.
> * If an `elif` condition is `True`, its block executes, and the remaining `elif` and `else` blocks are skipped.

<br>

```python
condition1 = True or False
condition2 = True or False
condition3 = True or False
#------------------------------------------------------------------------------------------#
if(condition1): #--------------------------------#                                         #
    'runs this block when condition1 is True'    #                                         #
    'skips this block when condition1 is False'  #                                         #
    #--------------------------------------------#                                         #
elif(condition2): #-----------------------------------------------------#                  #
    'runs this block when condition1 and condition2 are True'           #                  # 
    'skips this block when condition1 is True or condition2 is False'   #                  #
    #-------------------------------------------------------------------#                  #
elif(condition3): #-------------------------------------------------------------------#    #                
    'runs this block when condition1, condition2 are False and condition3 is True'    #    # 
    'skips this block when any preceding condition is True'                           #    #
    #---------------------------------------------------------------------------------#    #          
#------------------------------------------------------------------------------------------#
```
```python
#--------------------------#
if(True): #------------#   #
    'run this block'   #   #
    #------------------#   #
elif(True): #---------#    #
    'skip this block' #    #
    #-----------------#    #
elif(False): #--------#    #
    'skip this block' #    #
    #-----------------#    #
#--------------------------#
```
```python
#--------------------------#
if(False): #-----------#   #
    'skip this block'  #   #
    #------------------#   #
elif(True): #--------#     #
    'run this block' #     #
    #----------------#     #
elif(False): #--------#    #
    'skip this block' #    #
    #-----------------#    #
#--------------------------#
```
```python
#--------------------------#
if(False): #-----------#   #
    'skip this block'  #   #
    #------------------#   #
elif(False): #--------#    #
    'skip this block' #    #
    #-----------------#    #
elif(True): #---------#    #
    'run this block'  #    #
    #-----------------#    #
#--------------------------#
```

<br>

These `elif` statements are dependent on their preceding `if` or `elif` conditions, but each `elif` statement only executes if all previous conditions are False.
```python
if(condition1):
    ...
elif(condition2):
    ...
elif(condition3):
    ...
...
```


<br>

examples:
```python
x = 10
if x > 20:
    print("x is greater than 20")
elif x > 15:
    print("x is greater than 15 but not greater than 20")
elif x > 10:
    print("x is greater than 10 but not greater than 15")
elif x > 5:
    print("x is greater than 5 but not greater than 10")

#<-- unindent to be outside the if-elif code block
print("This is outside the if-elif block.")
```
```python
temperature = 30
if temperature > 35:
    print("It's very hot outside")
elif temperature > 25:
    print("It's warm outside")
elif temperature > 15:
    print("It's cool outside")
elif temperature > 5:
    print("It's cold outside")

#<-- unindent to be outside the if-elif code block
print("This is outside the if-elif block.")
```
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

#<-- unindent to be outside the if-elif code block
print("This is outside the if-elif block.")
```
```python
day = "Monday"
if day == "Friday":
    print("It's almost the weekend!")
elif day == "Wednesday":
    print("It's the middle of the week")
elif day == "Monday":
    print("It's the start of the week")
elif day == "Sunday":
    print("It's the end of the week")

#<-- unindent to be outside the if-elif code block
print("This is outside the if-elif block.")
```
```python
day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = "Friday"

if today in day_of_week[0:5]: 
    print("It's a weekday")
elif today in day_of_week[5:]:
    print("It's the weekend")

#<-- unindent to be outside the if-elif code block
print("This is outside the if-elif block.")
```

<br>

[Back to Top](#python-conditionals)

___

<br>

# `else Statements`
Basically: `else statements` execute their code block if all the conditions above are false

Specifically: `else statements` are used in conjunction with `if` and `elif` statements to provide a block of code that will execute if none of the preceding conditions are true.

<br>

An `else statement` cannot be written by itself, it must always be used in conjunction with an `if statement`

syntax:
```
if(condition):
    Code block to execute if the condition is True
    ...
else:
    Code block to execute if the condition above is False
    ...
```
> * if the condition is True the `if` code block executes
> * if the condition is False the `if` code block is skipped, and the `else` block executes
> * The `else` is dependent on the `if`

<br>

```python
condition = True or False
#--------------------------------------------------------------#
if(condition): #-----------------------------------#           #
    'runs this block when the condition is True    '           #
    'skips this block when the condition is False  '           #
    #----------------------------------------------#           #
else: #-----------------------------------------------------#  #
    'runs this block when all conditions above it are False '  #
    'skips this block when any condition above it is True   '  #
    #-------------------------------------------------------#  #
#--------------------------------------------------------------#
```
```python
#--------------------------#
if(True): #----------#     #
    'run this block' #     #
    #----------------#     #
else: #----------------#   #
    'skip this block'  #   #
    #------------------#   #
#--------------------------#
```
```python
#---------------------------#
if(False): #-----------#    #
    'skip this block'  #    #
    #------------------#    #
else: #--------------#      #
    'run this block' #      #
    #----------------#      #
#---------------------------#
```

<br>

These two `if` statements are independent, but each `else` statement depends on its attached `if`.
```python
if(True):
    ...
else:
    ...


if(False):
    ...
else:
    ...
```


<br>


example:
```python
number = 7
if (number % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")
#<-- unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
string = "Hello"
if (len(string) > 5):
    print("The string is long.")
else:
    print("The string is short.")
#<-- unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
numbers = [1, 2, 3, 4, 5]
if (len(numbers) > 3):
    print("The list has more than 3 elements.")
else:
    print("The list has 3 or fewer elements.")
#<-- unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
temperature = 30
if (temperature >= 0 and temperature <= 25):
    print("The temperature is within a comfortable range.")
else:
    print("The temperature is outside the comfortable range.")
#<-- unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
score = 85
if (score >= 90):
    print("Grade: A")
else:
    print("Grade: B or lower")
#<-- unindent to be outside the if-else code block
print("This is outside the if-else block.")
```

<br>

[Back to Top](#python-conditionals)

___

<br>

# `if-elif-else Chained Conditional Statements`
Basically: A `chained conditional` is a statement that contains an `if`, one or more `elif`s, and an else statement.

Specifically: A `chained conditional` is a series of conditional statements that are linked together using `if`, `elif`, and `else` keywords used to allow the program to evaluate multiple conditions in a sequence.


1. `If a block is not executed it is skipped.`
1. `If a block is executed every block after it is skipped.`
1. `A new 'if' starts a new independent conditional`

<br>

syntax:
```
if(condition_1):
    Code block to execute if condition_1 is True
    ...
elif(condition_2):
    Code block to execute if condition_1 is False AND condition_2 is True
    ...
...
else:
    Code block to execute if condition_1 AND condition_2 are False
    ...
```
> * If condition_1 is True the `if` block executes
> * If condition_1 is False and condition_2 is True the `elif` block executes
> * If all conditions above it are False the `else` block executes
> * `elifs` are dependent on `if`

<br>

```python
#---------------------------------------------------------------------------------------#
if(condition): #------------------------------------#                                   #
    'runs this block when the condition is True'    #                                   #
    'skips this block when the condition is False'  #                                   #
    #-----------------------------------------------#                                   #
elif(condition): #------------------------------------------------------------------#   #
    'runs this block when the conditions above are False and its condition is True '#   #
    'skips this block when an above condition is True or its condition is False'    #   #
    #-------------------------------------------------------------------------------#   #
else:#------------------------------------------------------------#                     #
    'runs this block only when the conditions above it are False' #                     #
    'skips this block when any condition above it is True'        #                     #
    #-------------------------------------------------------------#                     # 
#---------------------------------------------------------------------------------------#
```
```python
#---------------------------------#
if(True): #------------#          #
    'run this block'   #          #
    #------------------#          #
elif(True): #-------------#       #
    'skip this block'     #       #
    #---------------------#       #
else: #----------------#          #
    'skip this block'  #          #
    #------------------#          #
#---------------------------------#
```
```python
#---------------------------------#
if(False): #------------#         #
    'skip this block'   #         #
    #-------------------#         #
elif(True): #-------------#       #
    'run this block'      #       #
    #---------------------#       #
else: #----------------#          #
    'skip this block'  #          #
    #------------------#          #
#---------------------------------#
```
```python
#---------------------------------#
if(False): #------------#         #
    'skip this block'   #         #
    #-------------------#         #
elif(False): #------------#       #
    'skip this block'     #       #
    #---------------------#       #
else: #----------------#          #
    'run this block'   #          #
    #------------------#          #
#---------------------------------#
```

<br>

Each `elif` depends on the `if` and `elif` statements above it. The `else` only executes when the `if` and `elif` statements above it are False.
```python
if(condition1):
    ...
elif(condition2):
    ...
else:
    ...
```

<br>

example:
```python
score = 75
if (score >= 90):
    print("Grade: A")
elif (score >= 80):
    print("Grade: B")
elif (score >= 70):
    print("Grade: C")
elif (score >= 60):
    print("Grade: D")
else:
    print("Grade: F")
#<-- unindent to be outside the if-elif-else code block
print("This is outside the if-elif-else block.")
```


```python
age = 25
if (age < 13):
    print("Child")
elif (age < 18):
    print("Teenager")
elif (age < 65):
    print("Adult")
else:
    print("Senior")
#<-- unindent to be outside the if-elif-else code block
print("This is outside the if-elif-else block.")
```


```python
temperature = 45
if (temperature < 0):
    print("Freezing")
elif (temperature < 10):
    print("Very Cold")
elif (temperature < 20):
    print("Cold")
elif (temperature < 30):
    print("Warm")
else:
    print("Hot")
#<-- unindent to be outside the if-elif-else code block
print("This is outside the if-elif-else block.")
```


```python
light = "yellow"
if (light == "red"):
    print("Stop")
elif (light == "yellow"):
    print("Caution")
elif (light == "green"):
    print("Go")
else:
    print("Invalid light color")
#<-- unindent to be outside the if-elif-else code block
print("This is outside the if-elif-else block.")
```


```python
rating = "R"
if (rating == "G"):
    print("General Audiences")
elif (rating == "PG"):
    print("Parental Guidance")
elif (rating == "PG-13"):
    print("Parents Strongly Cautioned")
elif (rating == "R"):
    print("Restricted")
else:
    print("No rating")
#<-- unindent to be outside the if-elif-else code block
print("This is outside the if-elif-else block.")
```

# `Nested Conditionals`
`Nested conditionals` are conditional statements placed within the code block of another conditional statement.


```python
if(True):
    if(True):
        'the block runs only if both are True'
```
```python
a = True or False
b = True or False
c = True or False

#=====================================================#
if(a):                                                #
    print("a is True")                                #
    #+++++++++++++++++++++++++++++++++++++++#         #
    if(b):                                  #         #
        print("a,b are True")               #         #
        #----------------------------#      #         #
        if(c):                       #      #         #
            print("a,b,c are True")  #      #         #
        else:                        #      #         #
            print("c is False")      #      #         #
        #----------------------------#      #         #
    else:                                   #         #
        print("b is False")                 #         #
    #+++++++++++++++++++++++++++++++++++++++#         #
else:                                                 #
    print("a is False")                               #
#=====================================================#

#There can many different combinations
```

<br>

example:
```python
mode_of_travel = "car"
distance = 15

if (mode_of_travel == "car"):
    if (distance > 20):
        print("Long car trip.")
    else:
        print("Short car trip.")
elif (mode_of_travel == "bike"):
    if (distance > 20):
        print("Long bike ride.")
    else:
        print("Short bike ride.")
else:
    if (distance > 20):
        print("Long trip.")
    else:
        print("Short trip.")
# Unindented to be outside the nested conditionals
print("This is outside the nested conditionals.")
```


```python
device = "phone"
battery_level = 50

if (device == "phone"):
    if (battery_level > 20):
        print("Phone battery is sufficient.")
    else:
        print("Phone battery is low.")
elif (device == "laptop"):
    if (battery_level > 20):
        print("Laptop battery is sufficient.")
    else:
        print("Laptop battery is low.")
else:
    if (battery_level > 20):
        print("Device battery is sufficient.")
    else:
        print("Device battery is low.")
# Unindented to be outside the nested conditionals
print("This is outside the nested conditionals.")
```


```python
age = 17
member = True

if (age >= 18):
    if (member):
        print("Adult member")
    else:
        print("Adult non-member")
else:
    if (member):
        print("Underage member")
    else:
        print("Underage non-member")
# Unindented to be outside the nested conditionals
print("This is outside the nested conditionals.")
```

<br>

[Back to Top](#python-conditionals)

___

<br>


# `Ternary Operators: Shorthand Conditionals`
Basically: `Ternary Operators` are a shorthand way to write an if statement.

`Ternary Operators` are best used for short simple conditionals, as longer ternary operators are confusing. 

*In general ternary operators should only be used with simple conditionals. They may make you feel smart, but they can become very difficult to read if they are not simple*

syntax:
```
value_if_true if condition else value_if_false
```

> *The term "ternary" refers to the fact that it takes three operands: the condition to be evaluated, the expression to be returned if the condition is true, and the expression to be returned if the condition is false.*

<br>

examples:
```python
x = 2; y = 3; z = 4
print("if") if True else print("else") #Output: if
```
```python
x = 10
result = "Positive" if x > 0 else "Non-positive"
print(result) # Output: Positive
```
```python
num = 4
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Even
```
```python
string = "Hello"
length_status = "Long" if len(string) > 5 else "Short"
print(length_status) # Output: Short
```
```python
my_list = [1, 2, 3]
list_status = "Not Empty" if my_list else "Empty"
print(list_status) # Output: Not Empty
```

<br>

These nested ternary operators can be very confusing and are great examples of why they should be reserved for simple conditions


```python
x = -1; y = -1
print("if") if x > 0 else print("else if") if y > 0 else print("else") #Output: else
```


```python
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(grade) # Output: B

```

<br>

[Back to Top](#python-conditionals)

___

<br>

# `Match Statements`
Basically: `Match Statements` are a way to compare against many simple patterns and execute code based on pattern matches.


Specifically: `Match Statements` use structural pattern matching to compare a value against a series of patterns and execute blocks of code based on which pattern matches.

`Only the first matched pattern is executed`

syntax:

    match subject:
        case pattern1:
            block of code to execute if pattern1 matches
            ...
        case pattern2:
            block of code to execute if pattern2 matches
            ...
        ...
        case _:
            block of code to execute if no other pattern matches (default case)
            ...



<br>

examples:


```python
error_code = 404

match error_code:
    case 200:
        message = "OK"
    case 400:
        message = "Bad Request"
    case 401:
        message = "Unauthorized"
    case 403:
        message = "Forbidden"
    case 404:
        message = "Not Found"
    case 500:
        message = "Internal Server Error"
    case _:
        message = "Unknown Error"

print(message)  # Output: Not Found
```


```python
role = "admin"

match role:
    case "admin":
        access_level = "Full access"
    case "user":
        access_level = "Limited access"
    case "guest":
        access_level = "Guest access"
    case _:
        access_level = "No access"

print(access_level)  # Output: Full access
```


```python
color = "red"

match color:
    case "red":
        action = "Stop"
    case "yellow":
        action = "Prepare to stop"
    case "green":
        action = "Go"
    case _:
        action = "Unknown color"

print(action)  # Output: Stop
```


```python
shape = ("rectangle", 10, 5)

match shape:
    case ("circle", radius):
        area = 3.14 * radius * radius
    case ("rectangle", length, width):
        area = length * width
    case ("triangle", base, height):
        area = 0.5 * base * height
    case _:
        area = "Unknown shape"

print(area)  # Output: 50
```


```python
command = "--help"

match command:
    case "--help":
        response = "Displaying help information..."
    case "--version":
        response = "Version 1.0.0"
    case "--verbose":
        response = "Verbose mode enabled"
    case _:
        response = "Unknown command"

print(response)  # Output: Displaying help information...

```

<br>

## `Combining Patterns`
Combine multiple patterns into one case using `|`


```python
status = 401
match status:
    case 200 | 201 | 202:
        description = "Success"
    case 400 | 401 | 403:
        description = "Client Error"
    case 500 | 502 | 503:
        description = "Server Error"
    case _:
        description = "Unknown Status"

print(description)  # Output: Client Error
```


```python
day = "Funday"
match day:
    case "Saturday" | "Sunday":
        day_type = "Weekend"
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        day_type = "Weekday"
    case _:
        day_type = "Unknown Day"

print(day_type)  # Output: Unknown Day
```

<br>

## `Adding a Guard`
* A `guard` is an additional condition that must be satisfied for a case to match successfully. 
* Guards are specified using the `if` keyword. 


```python
number = 7

match number:
    case n if n % 2 == 0:
        result = "Even"
    case n if n % 2 != 0:
        result = "Odd"
    case _:
        result = "Unknown"

print(result)  # Output: Odd
```


```python
temperature = 25

match temperature:
    case t if t < 0:
        category = "Freezing"
    case t if 0 <= t <= 10:
        category = "Cold"
    case t if 10 < t <= 25:
        category = "Moderate"
    case t if 25 < t <= 35:
        category = "Warm"
    case t if t > 35:
        category = "Hot"
    case _:
        category = "Unknown"

print(category)  # Output: Moderate
```

<br>

[Back to Top](#python-conditionals)

___

<br>


# `Appendix`

More Conditional Examples


```python
#Determine if a number is even or odd
num = 0

if(num % 2 == 0):
    print("even")
else:
    print("odd")

#Determine if a number is positive negative or 0
num = 0

if(num > 0):
    print("positive")
elif(num < 0):
    print("negative")
else:
    print(0)

#Given two numbers determine which one is larger
a = 4
b = 3

if(a > b):
    print(a)
elif(b > a):
    print(b)
else:
    print("equal")

#Given 3 numbers determine the largest
a = 1
b = 2
c = 3

if(a > b and a > c):
    print(a, "is largest")
elif(b > a and b > c):
    print(b, "is largest")
else:
    print(c, "is largest")


#Determine if a year is a leap year(nested if)
#A leap year is a year that is divisible by 4, except for years that are divisible by 100 but not divisible by 400. 
# 1900 was not a leap year because it is divisible by 100 but not by 400, 
# 2000 was a leap year because it is divisible by both 100 and 400.

year = 2023

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year") 


#Write a program that takes a number from 1 to 12 as input from the user and prints the corresponding month name.
month = 1

if(month == 1):
    print("January")
elif(month == 2):
    print("February")
elif(month == 3):
    print("March")
elif(month == 4):
    print("April")
elif(month == 5):
    print("May")
elif(month == 6):
    print("June")
elif(month == 7):
    print("July")
elif(month == 8):
    print("August")
elif(month == 9):
    print("September")
elif(month == 10):
    print("October")
elif(month == 11 ):
    print("Novemeber")
elif(month == 12):
    print("December")
else:
  print("error")


#Write a program to check if a number is between 0-10 or 10-20 or 20-30.
number = 0

if(0 <= number and number <= 10):
    print(number, "is between 0-10")
elif(10 < number and number <=20):
    print(number, "is between 10-20")
elif(20 < number and number <= 30):
    print(number, "is between 20 and 30")
else:
    print(number, "is not in the range")
  

#Write a program to convert roman numerals to integers
#Limit your answer to these numerals I = 1, V = 5, X = 10, L = 50
numeral = "X"

if(numeral == "I"):
    print(1)
elif(numeral == "V"):
    print(5)
elif(numeral == "X"):
    print(10)
elif(numeral == "L"):
    print(50)
else:
    print("not recognized")



#Check if a character is a vowel or a consonant

char = input().lower()

if char in "aeiou":
    print(f'{char} is a VOWEL')
else:
    print(f'{char} is a Consonant')


#Determine the type of triangle based on side length

a_size = float(input())
b_size = float(input())
c_size = float(input())


if(a_size == b_size == c_size):
    print("Equalateral Triangle")
elif(a_size == b_size or a_size == c_size or b_size == c_size):
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")


#Check if a number is within a given range

num = int(input("Enter a whole number: "))
low = 10
high = 100

if low <= num <= high:
    print(f"{num} is in the range")
else:
    print(f"{num} is not in the range")

#OR
if num in range(low,high+1):
    print(f"{num} is in the range")
else:
    print(f"{num} is not in the range")


#Determine the quadrant of a coordinate point 
x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
elif x > 0 and y < 0:
    print("Quadrant IV")
else:
    print("On the axes or origin")


#Determine the type of quadrilateral
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
d = float(input("Enter side d: "))

if a == b == c == d:
    print("Square")
elif a == c and b == d:
    print("Rectangle")
else:
    print("Quadrilateral")
```


<br>

[Back to Top](#python-conditionals)

___

<br>


*Created and maintained by Mr. Merritt* 