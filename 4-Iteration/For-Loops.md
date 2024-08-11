*Use CTRL + F to search for keywords in this file*
# <table><th>``For Loops (without lists)``<th></table>
___

Covered in this file:
1. Iteration Defined
2. Python indentation and Code Blocks
3. For Loop Syntax
4. range() constructor
5. Counting with For Loops
6. Ascending: Counting Up by 1 and by multiples 
7. Descending: Counting Down by 1 and by multiples
8. Unique to Python: For-Else
9. For Each Loops
10. Run Time Errors: Off by 1 
11. Throw away variable _
12. Nested For loops
13. Break, Continue, and Pass Keywords
14. Combining Control Structures

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


## <table><th>`Iteration Defined`<th></table>
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
> Indentation defines the level of the code block when nesting constructs

> Note:   
> Most code editors like VS Code will provide a line to help you keep track of the beginning and end of your code blocks



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

## <table><th>`For Loop Syntax`<th></table>
___
**for loop**
> * basically: repeat a code block a finite number of times
> * specifically: a control flow statement that iterates over a sequence of elements in an iterable object

> * The *for* keyword defines the start of a for loop
> * Each for loop has a loop variable that appears after the *for* keyword
> * Each for loop in python uses the 'in' keyword after the loop variable
>    * It signifies the loop variable will take on each value from the iterable in turn
> * A for loop, iterates through an iterable type placed after the 'in' keyword
> * a ':' is used to indicate the start of the block of code to be repeated

`Note: for loop syntax in Python is different than most languages`

abstract example:
```python
iterable_object = ...

for loop_variable in iterable_object: #This line is called the for loop header
    #indent 4 spaces to be inside the loop block
    'repeat this code block'
#unindent 4 spaces to exit the loop block
```
```python
iterable_object = ...

#--------------------------------------#
for variable in iterable_object: #     #         
    'repeat this code block'     #     #
    #----------------------------#     #
#--------------------------------------# 
```
real example:
```python
for num in range(5):
    print(num, end = " ")
```

## Comparing for loop syntax between languages

example: Print out each number from 0 to 5.  

> NOTE:  
> *Most commonly used programming languages use a similiar syntax for writing for loops. 
> Python deviates from this common syntax in several ways, however since it is likely that you will encounter these other languages it is important to see the similarities. 
> Therefore we will begin by showing you how to count using for loops with a  "start, stop, step" syntax as this most closely translates to other languages.
> Examples of for loop syntax in multiple languages is shown below.*

Python
```python
for i in range(0,6,1):
    print(i, end = " ")
```

Java
```java
for(int i = 0; i < 6; i++){
    System.out.print(i + " ");
}
```

Javascript
```javascript
for(let i = 0; i < 6; i++){
    console.log(i + " ");
}
```
C\+\+
```cpp
for (int i = 0; i < 6; i++) {
    cout << i << " ";
}
```

C#
```csharp
for (int i = 0; i < 6; i++) {
    Console.Write(i + " ");
}
```

Go
```go
for i := 0; i < 6; i++ {
    fmt.Printf("%d ", i)
}
```

Rust
```rust
for i in 0..6 {
    print!("{} ", i);
}
```

Lua
```lua
for i = 0, 5 do
    io.write(i .. " ")
end
```

Bash
```bash
for (( i = 0; i < 6; i++ )); do
    echo -n "$i "
done
```

Powershell
```powershell
for ($i = 0; $i -lt 6; $i++) {
    Write-Host -NoNewline "$i "
}
```
Swift
```swift
for i in 0..<6 {
    print("\(i) ", terminator: "")
}
```
## <table><th>`The range() constructor`<th></table>
___
> * the range() constructor constructs a range object that is an iterable sequence of numbers
> * range() returns a range of number from start to stop-1

> * The range() constructor has 3 parameters (start, stop, step)
>    * These parameters define the range of numbers that is constructed
>    * The 'start' is always included in the range
>    * The 'stop' is always excluded, thus the last number in the range is stop-1 for ascending ranges, and stop+1 for descending ranges

abstract example:
```python
start,stop,step = ... #just place holders

'The range() constructor has 3 parameters (start, stop, step)'
#returns a range of numbers from start to stop-1. 
range(start, stop, step)
```
real example:
```python
range(0,11,1) # Returns: a range from 0 to 10 by 1s
```

### The default start value is 0:
> * Only works for ascending ranges where the step is 1

abstract example:
```python
stop = ... #place holder

'The range() constructor has 3 parameters (start, stop, step)'
#returns a range of numbers from start to stop-1. 
range(stop)
```
real examples:
```python
range(11)   # Returns: a range from 0 to 10 by 1s
range(6)    # Returns: a range from 0 to 5 by 1s
range(30)   # Returns: a range from 0 to 29 by 1s
```

### The default step is 1
> * This means ranges by default are ascending, you must specify both the start and step to create descending ranges

abstract example:
```python
start,stop= ... #just place holders

'The range() constructor has 3 parameters (start, stop, step)'
#returns a range of numbers from start to stop-1. 
range(start, stop)
```
real examples:
```python
range(5,20)     # Returns: a range from 5 to 19 by 1s
range(50,67)    # Returns: a range from 50 to 66 by 1s
range(100,1001) # Returns: a range from 100 to 1000 by 1s
```

Other real range examples:
> * start is included (default is 0)  
> * stop is not included (+1 if going up or -1 if going down)  
> * step (default is 1) 

```python
range(0,10,1)       # Returns: a range from 0 to 9 by 1s
range(10)           # Returns: a range from 0 to 9 by 1s
range(10,0,-1)      # Returns: a range from 10 to 1 by 1s
range(-5,6,1)       # Returns: a range from -5 to 5 by 1s
range(5,-6,-1)      # Returns: a range from 5 to -5 by 1s
```
## <table><th>`Counting with For Loops`<th></table>
___
> * The use of the letter i as a control variable in loops is a long-standing convention in programming.   
> * This practice dates back to early computing and mathematical notation, where i often represents an index or iterator.

> These following letters are commonly used as control variables:
> * i
> * j
> * k
> * n

**General Syntax for Counting with For Loops**
```python
for number in range(start,stop,step):   # for loop header
    print(number, end = " ")            # prints the value of number, and  adds a single space
```
## <table><th>`Ascending: Counting up by 1 and by Multiples`<th></table>
___
> * The 'stop' is always excluded, thus the last number in the range is stop-1 for ascending ranges. 
>   * For example: if you want to stop at 5 then stop should equal 6 

real examples:
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

## <table><th>`Descending: Counting Down by 1 and by Multiples`<th></table>
___
> * start and step values must be provided for descending ranges
> * The 'stop' is always excluded, thus the last number in the range is stop+1 for descending ranges
>   * For example: if you want to stop at 5 then stop should equal 4

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

## <table><th>`Unique to Python: For-Else`<th></table>
___
> * Python allows for an else block to be attached to a for block.
> * The else only executes if the loops completes normally without encountering a break statement.
> * The else block runs only one time, once the for loop ends.

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

## <table><th>`The For-Each Loop`<th></table>
___
**for each**
> * basically: loops through the items in a collection
> * specifically: a type of loop construct used to iterate over elements in a collection or sequence.

> * use: used to directly loop through iterable types
> * use: typically used when accessing all the elements of a collection

`Note: all of the for loops in python are for each loops by design. This is not the case in all languages.`

For-Each syntax:
```
for variable in iterable:
    <Code Block to Execute Repeatedly>  
```

abstract example:
```python
iterable = ... #place holder

for variable in iterable:
    'code block to execute'
#iterables are something that can be repeated through 
# strings, lists, tuples, sets, dictionaries, etc. are iterable
```

real examples:
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

## <table><th>`Run Time Errors: Off by 1 `<th></table>
___
> * basically: counting 1 to many or 1 to few times
> * specifically: occurs when an iterative loop executes one too many or one too few times typically due to incorrect indexing or boundary conditions.
> * error type: runtime or logical

counting example: logical error
```python
# Suppose we want to print numbers from 1 to 5
# but mistakenly use range(6) which includes 0 to 5
for i in range(6):
    print(i)

#Output:
# 0
# 1
# 2
# 3
# 4
# 5

```

example with a list: runtime error
```python
letters = ["a", "b", "c", "d","e"]

for i in range(0,6,1):
    print(letters[i], end=" ")

# Results: IndexError: list index out of range
```

## <table><th>`Throw away variable _`<th></table>
___
> * sometimes we don't need the loop variable, but still need a place holder
> * use an underscore _ as a throw away (unused) variable

real example:
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

## <table><th>`Nested For Loops`<th></table>
___
> * Placing one for loop inside of another creates a nested for loop
> * The inner for loop fully executes for every 1 iteration of the outer loop

syntax:
```
for variable in iterable:
    for variable in iterable:
        <Code Block to Repeat>
        ...
    ...
```

abstract examples:
```python
for variable_1 in range():
    #indent 4 spaces to be inside the outer loop block
    for variable_2 in range():
        #indent 4 spaces to be inside the inner loop block
        'repeat this code block'
    #unindent to exit the inner loop block
#unindent to exit the outer loop block
```
```python
#----------------------------------------------#
for variable_1 in range(): #--------------#    #
                                          #    #
    for variable_2 in range(): #------#   #    # 
        'repeat the code block'       #   #    #
        #-----------------------------#   #    #
  #---------------------------------------#    #
#----------------------------------------------#
```

real examples:
```python
for repeat in range(3):             # repeat 3 times
    for number in range(0,5,1):     # 0 to 4 by 1s
        print(number, end = " ")
    print()                         # added to format output
# Output:
# 0 1 2 3 4 
# 0 1 2 3 4 
# 0 1 2 3 4 

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

## <table><th>`Break, Continue and Pass Keywords`<th></table>
___


## Break
**break**
> * basically: statement used to end a loop early
> * specifically: statement used to exit (or "break out of") the loop prematurely. 

> * use: commonly used within loops like for and while to interrupt the loop's execution based on a certain condition.


abstract example:
```python
for variable in iterable:
    break
```

real example: Checking Prime Numbers
```python
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

## Continue

**continue**
> * basically: a statement that skips the rest of code block in the current loop.
> * specifically: a statement used to skip the rest of the code inside a loop for the current iteration, and continue with the next iteration of the loop.

abstract example:
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

## Pass
**pass**
> * basically: is a placeholder
> * specifically:  is a placeholder statement that does nothing when executed. 

> * use: used when a statement is required syntactically but no action is needed. This can be useful in situations where code is being written incrementally, or when a function or loop is meant to be implemented later.

abstract example:
```python
for variable in iterable:
    pass
```



