
# `Python For Loops`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Control Flow Statements`](#control-flow-statements)
1. [`Iteration Defined`](#iteration-defined)
1. [`Python Indentation and Code Blocks`](#python-indentation-and-code-blocks)
1. [`For Loop Syntax`](#for-loop-syntax)
    1. [`Comparing for loop syntax between languages`](#comparing-for-loop-syntax-between-languages)
1. [`The range() constructor`](#the-range-constructor)
    1. [`The default start value is 0`](#the-default-start-value-is-0)
    1. [`The defaul step is 1`](#the-default-step-is-1)
1. [`Counting with For Loops`](#counting-with-for-loops)
    1. [`Ascending: Counting up by 1 and by Multiples`](#ascending-counting-up-by-1-and-by-multiples)
    1. [`Descending: Counting down by 1 and by Multiples`](#descending-counting-down-by-1-and-by-multiples)
1. [`Common Logical Errors: Off by One`](#common-logical-errors-off-by-one)
1. [`Unique to Python: For-Else`](#unique-to-python-for-else)
1. [`The For-Each Loop`](#the-for-each-loop)
1. [`Throw away variable '_'`](#throw-away-variable)
1. [`Nested For Loops`](#nested-for-loops)
1. [`Break Statement`](#break-statement)
1. [`Continue Statement`](#continue-statement)
1. [`Pass Statement`](#pass-statement)
1. [`Combining Control Flow Statements`](#combining-control-flow-statements)



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

[Back to Top](#python-for-loops)

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

[Back to Top](#python-for-loops)

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

[Back to Top](#python-for-loops)

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

[Back to Top](#python-for-loops)

___

<br>

# `For Loop Syntax`
Basically: A `for loop` repeats a code block a finite number of times.

Specifically: A `for loop` is a control flow statement that iterates over a sequence of elements in an iterable object

<br>

> The `for` keyword starts a loop in Python, with a `loop variable` following it. The `in` keyword specifies that the `loop variable` will take each value from the iterable placed after in. A colon `:` marks the start of the code block to be repeated for each value in the iterable.

<br>

`Note: for loop syntax in Python is different than most languages`


```python
iterable_object = ...

for loop_variable in iterable_object: #This line is called the for loop header
    #--> indent 4 spaces to be inside the loop block
    'repeat this code block'
#<-- unindent 4 spaces to exit the loop block
```
```python
iterable_object = ...

#--------------------------------------#
for variable in iterable_object: #     #         
    'repeat this code block'     #     #
    #----------------------------#     #
#--------------------------------------# 
```
example:
```python
for num in range(5):
    print(num, end = " ")

# Output: 0 1 2 3 4
```

<br>

## `Comparing for loop syntax between languages`

*Most commonly used programming languages use a similiar syntax for writing for loops. Python deviates from this common syntax in several ways, however since it is likely that you will encounter these other languages it is important to see the similarities. Therefore we will begin by showing how to count using for loops with a  "start, stop, step" syntax as this most closely translates to other languages.*

<br>

`Examples of for loop syntax in multiple languages are shown below.`

> *Each of the for loops below are printing out each number from 0 to 5.*

 


`Python`
```python
for i in range(0,6,1):
    print(i, end = " ")
```

`Java`
```java
for(int i = 0; i < 6; i++){
    System.out.print(i + " ");
}
```

`Javascript`
```javascript
for(let i = 0; i < 6; i++){
    console.log(i + " ");
}
```
`C++`
```cpp
for (int i = 0; i < 6; i++) {
    cout << i << " ";
}
```

`C#`
```csharp
for (int i = 0; i < 6; i++) {
    Console.Write(i + " ");
}
```

`Go`
```go
for i := 0; i < 6; i++ {
    fmt.Printf("%d ", i)
}
```

`Rust`
```rust
for i in 0..6 {
    print!("{} ", i);
}
```

`Lua`
```lua
for i = 0, 5 do
    io.write(i .. " ")
end
```

`Bash`
```bash
for (( i = 0; i < 6; i++ )); do
    echo -n "$i "
done
```

`Powershell`
```powershell
for ($i = 0; $i -lt 6; $i++) {
    Write-Host -NoNewline "$i "
}
```
`Swift`
```swift
for i in 0..<6 {
    print("\(i) ", terminator: "")
}
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `The range() constructor`
The `range()` constructor constructs a range object that is an iterable sequence of numbers

`range()` returns a range of number from start to stop-1 (up) or stop+1 (down)

<br>

The `range()` constructor has 3 parameters (`start`, `stop`, `step`)
* `start` value is included in the range (default is 0)  
* `stop` is not included in the range. (`stop-1` is the last value if going up. `stop+1` is the last value if going down.) 
* `step` (default is 1) 

<br>

syntax:
```
range(start, stop, step)
```
example
```python
range(0,11,1) # Returns: a range from 0 to 10 by 1s
```

<br>

## `The default start value is 0`
When only one argument value is provided to the `range()` constructor it is by default the value of the `stop` parameter. 

`When only 1 argument value is provided the default start value is 0 ` 
syntax:
```
range(stop)
```
examples:
```python
range(11)   # Returns: a range from 0 to 10 by 1s
range(6)    # Returns: a range from 0 to 5 by 1s
range(30)   # Returns: a range from 0 to 29 by 1s
```

<br>

## `The default step is 1`
When only one argument value is provided to the `range()` constructor it is by default the value of the `stop` parameter. 

`When less than 3 argument values are provided the default step value is +1`
> * This means ranges by default are ascending, you must specify both the start and step to create descending ranges

syntax:
```
range(stop)
```
```
range(start, stop)
```
example:
```python
range(11)   # Returns: a range from 0 to 10 by 1s
range(6)    # Returns: a range from 0 to 5 by 1s
range(30)   # Returns: a range from 0 to 29 by 1s
```
```python
range(5,20)     # Returns: a range from 5 to 19 by 1s
range(50,67)    # Returns: a range from 50 to 66 by 1s
range(100,1001) # Returns: a range from 100 to 1000 by 1s
```

<br>

## `Other range() examples`

```python
range(0,10,1)       # Returns: a range from 0 to 9 by 1s
range(10)           # Returns: a range from 0 to 9 by 1s
range(10,0,-1)      # Returns: a range from 10 to 1 by 1s
range(-5,6,1)       # Returns: a range from -5 to 5 by 1s
range(5,-6,-1)      # Returns: a range from 5 to -5 by 1s
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Counting with For Loops`
Compared to `while` loops, which are best for iteration through an undefined number of times, `for` loops are ideal for iterating a defined number of times. 


The use of the letter `i` as a control variable in loops is a long-standing convention in programming.   

> * This practice dates back to early computing and mathematical notation, where `i` often represents an index or iterator.

These following letters are commonly used as control variables:
> * `i`
> * `j`
> * `k`
> * `n`

<br>

`General Syntax for Counting with For Loops`
```python
for number in range(start,stop,step):   # for loop header
    print(number, end = " ")            # prints the value of number, and ends with a single space
```

<br>

## `Ascending: Counting up by 1 and by Multiples`
The `stop` value is always excluded from the range , thus the last number in the range is `stop+1` for ascending ranges. 

<br>

`This means that if you want to end the range at 5, then stop must equal 6`

examples:
```python
'From 0 to Positive by 1s'
#count from 0 to 10
for number in range(11):            #start = 0; default step = +1 
    print(number, end = " ")
#Output: 0 1 2 3 4 5 6 7 8 9 10 

for number in range(0,11,1): 
    print(number, end = " ")
#Output: 0 1 2 3 4 5 6 7 8 9 10 
```
```python
'From 0 to Postive by Multiples'
#count from 0 to 10 by 3
for number in range(0,11,3): 
    print(number, end = " ")
#Output: 0 3 6 9
```
```python
'From 1 to Positive by 1s'
#count from 1 to 5 
for number in range(1,6):           #step = +1; default
    print(number, end = " ")
#Output: 1 2 3 4 5

for number in range(1,6,1): 
    print(number, end = " ")
#Output: 1 2 3 4 5
```
```python
'From 1 to Postive by Multiples'
#count from 1 to 5 by 2
for number in range(1,6,2): 
    print(number, end = " ")
#Output: 1 3 5
```
```python
'From Positive to Positive by 1s'
#count from 70 to 80
for number in range(70,81):         #step = +1; default 
    print(number, end = " ")
#Output: 70 71 72 73 74 75 76 77 78 79 80

for number in range(70,81,1): 
    print(number, end = " ")
#Output: 70 71 72 73 74 75 76 77 78 79 80
```
```python
'From Positive to Positive by Multiples'
#count from 70 to 100 by 5
for number in range(70,101,5): 
    print(number, end = " ")
#Output: 70 75 80 85 90 95 100
```
```python
'From Negative to Negative by 1s'
#count -35 to -24
for number in range(-35,-24):       #step = +1; default
    print(number, end = " ")
#Output: -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -25
  
for number in range(-35,-24,1):
    print(number, end = " ")
#Output: -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -25
```
```python
'From Negative to Negative by Multiples'
#count from -100 to -10 by 10
for number in range(-100,-9,10):
    print(number, end = " ")
#Output: -100 -90 -80 -70 -60 -50 -40 -30 -20 -10
```
```python
'From Negative to Positive by 1s'
#count from -5 to 5
for number in range(-5,6):      #step = +1; default
    print(number, end = " ")
#Output: -5 -4 -3 -2 -1 0 1 2 3 4 5

for number in range(-5,6,1):
    print(number, end = " ")
#Output: -5 -4 -3 -2 -1 0 1 2 3 4 5
```
```python
'From Negative to Positive by Multiples'
#count from -5 to 5 by 4
for number in range(-5,6,4):
    print(number, end = " ")
#Output: -5 -1 3
```

<br>

## `Descending: Counting Down by 1 and by Multiples`
The `stop` value is always excluded from the range , thus the last number in the range is `stop-1` for descending ranges. 

<br>

`This means that if you want to end the range at 5, then stop must equal 4`

* `start` and `step` values must be provided for descending ranges
* The `stop` is always excluded, thus the last number in the range is `stop+1` for descending ranges

`For instance, if you want to stop at 5 then stop should equal 4`

```python
'From Positive to 0 by 1s'
#count from 10 to 0 
for number in range(10,-1,-1):
    print(number, end = " ")
#Output: 10 9 8 7 6 5 4 3 2 1 0
```
```python
'From Positive to 0 by Multiples'
#count from 10 to 0 by 3
for number in range(10,-1,-3):
    print(number, end = " ")
#Output: 10 7 4 1 0
```
```python
'From Positive to Positive by 1s'
#count from 50 to 40
for number in range(50,39,-1):
    print(number, end = " ")
#Output: 50 49 48 47 46 45 44 43 42 41 40
```
```python
'From Positive to Positive by Multiples'
#count from 100 to 50 by 5s
for number in range(100,49,-5):
    print(number, end = " ")
#Output: 100 95 90 85 80 75 70 65 60 55 50
```
```python
'From 0 to Negative by 1s'
#count from 0 to -10 
for number in range(0,-11,-1):
    print(number, end = " ")
#Output: 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10
```
```python
'From 0 to Negative by Multiples'
#count from 0 to -100 by 20
for number in range(0,-101,-20):
    print(number, end = " ")
#Output: 0 -20 -40 -60 -80 -100
```
```python
'From Positive to Negative by 1s'
#count from 5 to -5
for number in range(5,-6,-1):
    print(number, end = " ")
#Output: 5 4 3 2 1 0 -1 -2 -3 -4 -5
```
```python
'From Positive to Negative by Multiples'
#count from 100 to -100 by 50
for number in range(100,-101,-50):
    print(number, end = " ")
#Output: 100 50 0 -50 -100
```
```python
'From Negative to Negative 1s'
#count from -85 to -95
for number in range(-85,-96,-1):
    print(number, end = " ")
#Output: -85 -86 -87 -88 -89 -90 -91 -92 -93 -94 -95
```
```python
'From Negative to Negative Mutliples'
#count from -200 to -1500 by 100
for number in range(-200,-1501,-100):
    print(number, end = " ")
#Output: -200 -300 -400 -500 -600 -700 -800 -900 -1000 -1100 -1200 -1300 -1400 -1500
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Common Logical Errors: Off by One`
Basically: `Off by One Errors` result from counting 1 to many or 1 to few times


Specifically: `Off by One Errors` occur when an iterative loop executes one too many or one too few times typically due to incorrect indexing or boundary conditions.

<br>

*Off by One Errors are considered logical errors, but often cause runtime errors such as `IndexError: list index out of range`.*

*In `for` loops this is often a result of a misunderstanding of how the `stop` parameter controls the range.*

example:
```python
"Count to 10 with and off by one error"

for num in range(10):       #stop should = 11
    print(num, end = " ")alphabet = ["a", "b", "c"]

for i in range(4):
    print(alphabet[i], end = " ")

# Output: 0 1 2 3 4 5 6 7 8 9
```
```python
"Loop through a list with off by one error"
# indexes  [ 0 ,  1 ,  2]
alphabet = ["a", "b", "c"]

for i in range(4):      # stop should = 3
    print(alphbet[i], end = " ")

# Runtime Error --> Returns: 
# a b c Traceback (most recent call last):
# File "<filepath>":, line 5, in <module>
#     print(alphabet[i], end = " ")
#           ~~~~~~~~^^^
# IndexError: list index out of range
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Unique to Python: For-Else`
`for-else` statements attach an `else` block to only executes when the loop completes normally without encountering a `break` statement.

The `else` block runs only one time, after the condition is False. 

syntax:
```
for variable in iterable:
    ...
else:
    ...
```

real example:
```python
for number in range(1,11,1):
    print(number, end = " ")
else:
    print("\nDone Printing!")

#Output:
# 1 2 3 4 5 6 7 8 9 10
# Done Printing!
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `The For-Each Loop`
Basically: `for-each` loops iterate through the items in a collection.


Specifically: `for-each` loops are a type of loop construct used to iterate over elements in a collection or sequence.

<br>

`for-each` loops are used to directly loop through iterable types and typically when accessing all the elements of a collection.

<br>

`Note: all of the for loops in python are for each loops by design. This is not the case in all languages.`

syntax:
```
for variable in iterable:
    <Code Block to Execute Repeatedly>  
    ...
```
```python
iterable = ... #place holder

for variable in iterable:
    'code block to execute'
# iterables are something that can be repeated through 
# strings, lists, tuples, sets, dictionaries, etc. are iterable
```

examples:
```python
string = "abcdefghijklmnopqrstuvwxyz"

for character in string:
    print(character, end = " ")

#Output: a b c d e f g h i j k l m n o p q r s t u v w x y z 
```
```python
list1d = ["list","tuple","set","dictionary","iterators"]

#element does not represent an index, but the actual element. 
for element in list1d:
    print(element, end = " ")

#Output: list tuple set dictionary iterators 
```
```python
tuple1d = ("list","tuple","set","dictionary","iterators")

#element does not represent an index, but the actual element. 
for element in tuple1d:
    print(element, end = " ")

#Output: list tuple set dictionary iterators 
```
```python
set1d = {"list","tuple","set","dictionary","iterators"}

#element does not represent an index, but the actual element. 
for element in set1d:
    print(element, end = " ")

#Output order will vary with a set: 
# Output: list tuple set dictionary iterators 
```
```python
dictionary = {"list":None,"tuple":None,"set":None,"dictionary":None,"iterators":None}

for key in dictionary.keys():
    print(key, end = " ")

#Output: list tuple set dictionary iterators
```
real example use case:   
```python
'Sum of a List of Integers'
nums = [1,2,3,4,5]

sum = 0
for num in nums:
    sum += num

print(sum)

#Output: 15
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Throw away variable`
Use `_` as a throw away variable. Sometimes we don't need the `loop variable` when using a `for loop`, but still need a place holder. This is a convention in Python to signal to other programmers that the variable is unused. 

syntax:
```
for _ in range(start, stop, step):
    ...
```
example:
```python
# We don't actually use the loop variable in this loop.
for _ in range(5):
    print("Looping...")

#Output:
# Looping...
# Looping...
# Looping...
# Looping...
# Looping...
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Nested For Loops`
`Nesting` refers to the placement of one or more constructs with another construct of the same type. 

Placing one for loop inside of another creates a `nested for loop`.
> * The inner for loop fully executes for every 1 iteration of the outer loop

<br>

Placing one for loop inside of another for loop. 

syntax:
```
for variable in iterable:
    for variable in iterable:
        <Code Block to Repeat>
        ...
    ...
```
```python
for variable_1 in range():
    #--> indent 4 spaces to be inside the outer loop block
    for variable_2 in range():
        #--> indent 4 spaces to be inside the inner loop block
        'repeat this code block'
    #<-- unindent to exit the inner loop block
#<-- unindent to exit the outer loop block
```
```python
#----------------------------------------------#
for variable_1 in range(): #--------------#    #
    for variable_2 in range(): #------#   #    # 
        'repeat the code block'       #   #    #
    #---------------------------------#   #    #
#-----------------------------------------#    #
#----------------------------------------------#
```

example:
```python
for repeat in range(3):             # repeat 3 times
    for number in range(0,5,1):     # 0 to 4 by 1s
        print(number, end = " ")
    print()                         # added to format output
# Output:
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 
```
```python
for repeat in range(2):             # repeat 2 times
    for number in range(0,101,20):  # 0 to 100 by 20s
        print(number, end = " ")
    print()                         # added to format output
# Output:
# 0 20 40 60 80 100 
# 0 20 40 60 80 100 
```
```python
for repeat in range(4):             # repeat 4 times
    for number in range(5,-6,-1):   # 5 to -5 by 1s
        print(number, end = " ")
    print()                         # added to format output
# Output:
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
# 5 4 3 2 1 0 -1 -2 -3 -4 -5
```
```python
for repeat in range(4):             # repeat 4 times
    for number in range(20,9,-2):   # 20 to 10 by 2s
        print(number, end = " ")
    print()                         # added to format output
# Output:
# 20 18 16 14 12 10 
# 20 18 16 14 12 10
# 20 18 16 14 12 10
# 20 18 16 14 12 10
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Break Statement`
Basically: A `break` statement is used to end a loop early

Specifically: A `break` statement is used to exit (or "break out of") the loop prematurely. 

`break` is commonly used within loops like `for` and `while` to interrupt the loop's execution based on a certain condition.

```python
for variable in iterable:
    break
```

example: 
```python
'''Checking Prime Numbers'''

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,"equals",x,"*",n//x)
            break
    #loop fell through without finding a factor
    else:
        print(n,"is a prime number")
#the loop will exit on the first loop
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Continue Statement`

Basically: `continue` is a statement that skips the rest of code block in the current loop.

Specifically:`continue` is a statement used to skip the rest of the code inside a loop for the current iteration, and continue with the next iteration of the loop.

```python
for variable in iterable:
    continue
```

real example:
```python
#Not printing values divisible by 7
for x in range(50):
    if(x % 7 == 0):
        continue #skips the rest of the code block, and starts the next loop.
    else:
        print(x)
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Pass Statement`
Basically: `pass` is a placeholder

Specifically: `pass` is a placeholder statement that does nothing when executed, and preserves the syntax of Python to allow the code to run.  

`pass` is used when a statement is required syntactically but no action is needed. This can be useful in situations where code is being written incrementally, or when a function or loop is meant to be implemented later.


```python
for variable in iterable:
    pass
```

<br>

[Back to Top](#python-for-loops)

___

<br>

# `Combining Control Flow Statements`
`Control flow statements` such as `if`, `while`, and `for` can be combined to preform more complex algorithms.

```python
for i in range(10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```
```python
for i in range(10):
    if i == 5:
        print("Breaking the loop")
        break
    print(i)
```
```python
numbers = [3, 2, 5]

for num in numbers:
    print(f"Counting down from {num}:")
    while num > 0:
        print(num)
        num -= 1
    print("Done!\n")
```
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print("Row:", row)
    for item in row:
        print(f"Item: {item}")
    print()  # Blank line between rows
```


<br>

[Back to Top](#python-for-loops)

___

<br>

*Created and maintained by Mr. Merritt*


