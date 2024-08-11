# <table><th>Python Conditionals</th></table>
___
**Covered in this file:**
1. Review: Booleans, Relational, Membership, Identity, and Logical Operators
2. Boolean Expression
3. Python Indentation and Code Blocks
4. if Statements
5. if-else Statements
6. if-elif-else (Chained Conditionals)
7. Nested Conditionals
8. Ternary Operators: Shorthand Conditionals
9. Match Statements

## Note on Boolean Expressions and Conditionals
When it comes to boolean expressions and conditional statements, the range of possibilities is vast and varied. The examples provided here are intended to illustrate some of the fundamental concepts and common use cases. However, it is impossible to cover every possible scenario or combination of conditions that may arise in real-world programming.


## <table><th>Review: Booleans, Relational, Membership, Identity, and Logical Operators</th></table>
___
Conditionals often utilize Booleans, Relational, Membership, Identity, and Logical Operators in order to determine what block of code should be executed

### Booleans (True/False)
* Booleans are a data with only two states, typically True or False


```python
True
False
```




    False



### Relational Operators (Inequalities)
* are used for comparisions
* evaluate to a boolean value (True/False)
* Order of Operations is Left to Right

|Symbol| Inequality Operation      |
|:----:|:-------------------------:|
|   >  | greater than              |
|   <  | less than                 |
|  >=  | greater than or equal to  |
|  <=  | less than or equal to     |
|  ==  | equal to                  |
|  !=  | not equal to              |

### Identity Operators
|Symbol| Identity Operation |
|:----:|:------------------:|
|is    |identical to        |
|is not|not identical       |

* Identity Operators check if the memory location of the two objects are identical

### Membership Operators
|Symbol |Membership Operation|
|:-----:|:------------------:|
|in     |apart of            |
|not in |not apart of        |

* Membership Operators check if a value is found in a sequence
* ie. checks if one thing is 'apart of' another



### Logical Operators
|Operator| Operation| Description|Shorthand|
|:------:|:--------:|:-----------:|:----:|
| not    | NOT      | opposite   | not T --> F, not F --> T|
| and    | AND      | both       | T and T --> T, all others F|
| or     | OR       | at least one | F or F --> F, all others T|



### Abbreviated Operator Precedence
|Opertors|Description|
|:-:|:-:|
| == != > >= < <=  | Comparisons|
| is, is not      | Identity|
| in, not in   | Membership operators |
| not         | Logical NOT        |
| and         | Logical AND        |
| or          | Logical OR         |




## <table><th>Boolean Expressions</th></table>
___
Boolean expression is 
> * Basically: any expression that is answered with True or False
> * Specifically: an expression in programming that evaluates to a Boolean value, which is either True or False. Boolean expressions are fundamental in controlling the flow of programs, as they are used in conditional statements, loops, and logical operations.

***Boolean expressions use differing combinations of relational, identity, membership, and logical operators to evaluate conditions and control the flow of a program.***

### Boolean Expression Examples:


```python
# 1. Relational and Logical
print(10 > 5 and 5 < 10)  # Output: True
```


```python
# 2. Relational and Logical
print(15 != 10 or 10 == 5)  # Output: True
```


```python
# 3. Membership
print('a' in 'apple')  # Output: True
```


```python
# 4. Membership and Logical
print(3 in [1, 2, 3, 4] and 5 not in [1, 2, 3, 4])  # Output: True
```


```python
# 5. Identity
a = [1, 2, 3]
b = a
print(a is b)  # Output: True
```


```python
# 6. Identity and Logical
x = 5
y = 5
print(x is y or x is not y)  # Output: True
```


```python
# 7. Membership and Relational
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits and len(fruits) == 3)  # Output: True
```


```python
# 8. Logical and Relational
num = 20
print(num > 10 and num < 30)  # Output: True
```


```python
# 9. Identity and Logical
c = 10
d = 10
print(not (c is d))  # Output: False
```


```python
# 10. Membership, Relational, and Logical
numbers = [1, 2, 3, 4, 5]
print(5 in numbers and (max(numbers) == 5))  # Output: True
```

    True
    

### **Special Note on Evaluating Boolean Expressions:**
When writing if statments you will often get output, sometimes even correct output, but your code does not work as intended in every case. 
This is because your code is syntatically correct, and even at run time the code will execute without error.

**You have made a Logical Error, that may be hard to track down because of how Python interprets the "truthiness" of certain data.**
**Below illustrates how Python treats the truthiness of certain data:**

*Note: Truthiness refers to the evaluation of an object's value in a boolean context, ie. determining whether it is considered true or false.*
|Data Type| Truthiness|
|:-:|:-:|
|Integers/Floats|Any non-zero number (integer, float) is evaluated as True|
|Strings,Lists, Tuples, Sets, Dictionaries|Any non-empty string, list, tuple, set, or dictionary, is evaluated as True|
|Functions, Methods, Lambdas, Classes|Any function, method, lambda or class is evaluated as True|
|Objects|By default objects are evaluated True, but how an object is evaluated can be changed|


*Note on Errors:*  
*Syntax/Compile Time Errors: occur when compiling the code, and the code violates the rules of the programming language's syntax.*  
*Runtime Errors: occur after the program has been successfully compiled and started execution. They usually result from operations that are not possible to perform.*  
*Logical Errors: occur when a program runs without crashing but produces incorrect results. These errors are caused by mistakes in the program's logic, meaning the code does not behave as intended.*  

## <table><th>Python Indentation and Code Blocks</th></table>
___

**Python syntax uses indentation to define the scope of blocks of code.**   
**Code blocks are groups of statements that are executed together as a unit.**
> * Each indentation level represents a higher level of code structure (conditionals, loops, functions, classes)
> * All statements within the same block must have the same level of indentation.
> * Indent 4 spaces to create a code block.  
> * The end of a block is indicated by the decrease in indentation level. 

*Note: Scope is the area of a program in which a block of code exists and executes.*  
<br>

*Notes:*  
* *Indentation is typically achieved using spaces or tabs.* 
* *Don't mix spaces and tabs, it can lead to syntax errors or inconsistent behavior.*   
* *Python 3 disallows mixing tabs and spaces for indentation in the same source file.*  
* *If you are using an editor like VScode using the tab key, and spaces is not a problem.*   



### Python Indentation Examples:


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

## <table><th>if Statements</th></table>
___
**if Statements:**
> * Basically: determine if  code block is executed based on truth of a condition.
> * Specifically: a control flow statement that allows you to execute a block of code only if a specified condition is true. If the condition evaluates to false, the code block is skipped.
> * Provides the ability to make decisions in programs

syntax:

    if(condition):
        Code block to execute if the condition is True 
        ...

* If the condition is True the code block executes
* If the condition is False the code block is skipped.
* Each new *'if'* is independant


```python
condition = True or False

#the condition in parenthesis is a boolean expression
if(condition):  #end with a colon ":"
    #indent 4 spaces to be inside the if code block
    'Code Block Here'

#unident 4 spaces to be outside the if code block


#------------------------------------------------------#
if(condition): #------------------------------------#  #
    'runs this block when the condition is True'    #  #
    'skips this block when the condition if False'  #  #
    #-----------------------------------------------#  #
#------------------------------------------------------#

#each new if starts its own separate conditional
if(True): #----------#        
    'run this block' # 
#--------------------#

if(False): #----------#
    'skip this block' # 
#---------------------#
```

### Example if Statements


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

## <table><th>if-else Statements</th></table>
___
> * Basically: executes its code block if the all conditions above are false
> * Specifically: used in conjunction with if and elif statements to provide a block of code that will execute if none of the preceding conditions are true.

syntax:

    if(condition):
        Code block to execute if the condition is True
        ...
    else:
        Code block to execute if the condition above is False
        ...

* if the condition is True the *'if'* code block executes
* if the condition is False the *'if'* code block is skipped, and the *'else'* block executes
* The *'else'* is dependent on the *'if'*


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

#--------------------------#
if(True): #----------#     #
    'run this block' #     #
    #----------------#     #
else: #----------------#   #
    'skip this block'  #   #
    #------------------#   #
#--------------------------#

#---------------------------#
if(False): #-----------#    #
    'skip this block'  #    #
    #------------------#    #
else: #--------------#      #
    'run this block' #      #
    #----------------#      #
#---------------------------#
```

# Example if-else Statements


```python
number = 7
if (number % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")
# unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
string = "Hello"
if (len(string) > 5):
    print("The string is long.")
else:
    print("The string is short.")
# unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
numbers = [1, 2, 3, 4, 5]
if (len(numbers) > 3):
    print("The list has more than 3 elements.")
else:
    print("The list has 3 or fewer elements.")
# unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
temperature = 30
if (temperature >= 0 and temperature <= 25):
    print("The temperature is within a comfortable range.")
else:
    print("The temperature is outside the comfortable range.")
# unindent to be outside the if-else code block
print("This is outside the if-else block.")
```


```python
score = 85
if (score >= 90):
    print("Grade: A")
else:
    print("Grade: B or lower")
# unindent to be outside the if-else code block
print("This is outside the if-else block.")
```

## <table><th>if-elif-else Chained Conditional Statements</th></table>
___
**Chained Contionals**
> * Basically: a statement that contains an if, one or more elifs, and an else statement.
> * Specifically:  a series of conditional statements that are linked together using if, elif, and else keywords used to allo the program to evaluate multiple conditions in a sequence.

syntax:

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


* If condition_1 is True the *'if'* block executes
* If condition_1 is False and condition_2 is True the *'elif'* block executes
* If all conditions above it are False the *'else'* block executes
* *'elifs'* are dependent on *'if'*

<br>

* If a block is not executed it is skipped.
* If a block is executed every block after it is skipped.
* A new *'if'* starts a new conditional



```python
'if-elif-else (Chained Conditional)' 
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

### Example if-elif-else Statements


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
# unindent to be outside the if-elif-else code block
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
# unindent to be outside the if-elif-else code block
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
# unindent to be outside the if-elif-else code block
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
# unindent to be outside the if-elif-else code block
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
# unindent to be outside the if-elif-else code block
print("This is outside the if-elif-else block.")
```

## <table><th>Nested Conditionals</th></table>
___
**Nested conditionals are conditional statements placed within the code block of another conditional statement.**


```python
if(True):
    if(True):
        'the block runs only if both are True'

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

### Example Nested Conditionals


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

## <table><th>Ternary Operators: Shorthand Conditionals</th></table>
___
**Ternary Operators:**
> * Basically: a shorthand way to write an if statement
> * They are best used for short simple conditionals, as longer ternary operators are confusing. 

*Note: In general ternary operators should only be used with simple conditionals. They may make you feel smart, but they can become very difficult to read if they are not simple*

syntax:

    value_if_true if condition else value_if_false

*The term "ternary" refers to the fact that it takes three operands: the condition to be evaluated, the expression to be returned if the condition is true, and the expression to be returned if the condition is false.*

### Ternary Operator Examples:


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

    Short
    


```python
my_list = [1, 2, 3]
list_status = "Not Empty" if my_list else "Empty"
print(list_status) # Output: Not Empty
```

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

## <table><th>Match Statements</th></table>
___
**Match Statements:**
> * Basically: a way to compare against many simple patterns and execute code based on pattern matches
> * Specifically: structural pattern matching allows comparision of a value against a series of patterns and execute blocks of code based on which pattern matches.


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

**Only the first matched pattern is executed**

### Match Statement Examples:


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

### Combining Patterns
* multiple patterns can be combined into one case using **\|**


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

    Unknown Day
    

### Adding a Guard
* A guard is an additional condition that must be satisfied for a case to match successfully. 
* Guards are specified using the if keyword. 


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

## Appendix

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
