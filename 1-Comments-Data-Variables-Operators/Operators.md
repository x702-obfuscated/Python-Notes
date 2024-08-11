# `Python Operators`
___

Covered in this file:
1. Concatenation and Duplication (combining strings)
2. Casting (changing data type)
3. Arithmetic operators (math)
4. Relational operators (inequalities)
5. Membership operators
6. Identity operators
7. Assignment vs Equality Operator
8. Compound Assignment Operators
9. Logical operators (not, and, or)
10. Compound Logical Expressions and De Morgan's Laws
11. Built-in Operation Function Calls
12. Bitwise Operators
13. Complete Operator Precedence


# `Concatenation and Duplication`
___
## Concatenation:
> * Basically: concatenation means "to join"
> * Specifically: the operation of joining two or more strings, arrays, or other sequences end-to-end to form a single sequence.
> * use the '+' sign to concatenate

syntax: 
```
sequence1 + sequence2
```   

```python
# Concatenating strings
"Hello" + "World"
#Result: Hello World

print("Hello" + "World")
#Output: Hello World

#Using Variables
first = "Hello"
second = "World"
print(first + second)
#Output: Hello World
```


```python
# Concatenating lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
# Output: [1, 2, 3, 4, 5, 6]

# Using Variables
first_list = [1, 2, 3]
second_list = [4, 5, 6]
print(first_list + second_list)
# Output: [1, 2, 3, 4, 5, 6]
```


```python
# Concatenating tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)
# Output: (1, 2, 3, 4, 5, 6)

# Using Variables
first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(first_tuple + second_tuple)
# Output: (1, 2, 3, 4, 5, 6)
```

## Duplication:
> * is the operation of copying an object or repeating a sequence.
> * use the '*' sign to duplicate

syntax:
```
object * n
```

***NOTE: n represents a variable number***


```python
"a" * 3
# Result: aaa

laugh = "ha"
print(laugh * 3) 
#Output: hahaha

```

# `Casting (changing data type)`
___
## Casting
> * the process of converting data from one type to another. This is also known as type conversion. 

Built-in Function Calls for casting
> * type(object)  returns the data type
> * str(object)   converts to string
> * int(object)   converts to an integer

> * float(object) converts to a float


syntax:
```
type(object)
```  

type() returns the data type of the object


```python
type(5)   #Returns: <class 'int'>
type("5") #Returns: <class 'str'>
type(5.0) #Returns: <class 'float'>
```

syntax:
```
str(object) 
```

> * creates a new string object from another object
> * ie. converts to a string
> * works on custom classes with the \_\_str\_\_ method defined


```python
null = None
str(null)       #Returns: 'None'
type(str(null)) #Returns: <class 'str'>
```


```python
boo = True
str(boo)        #Returns: 'True'
type(str(boo))  #Returns: <class 'str'>
```


```python
num = 123
str(num)        #Returns: "123"
type(str(num))  #Returns: <class 'str'>
```


```python
flo = 3.14
str(flo)        #Returns: "3.14"
type(str(flo))  #Returns: <class 'str'>
```


```python
complex_num = 1 + 2j
str(complex_num)        #Returns: '(1+2j)'
type(str(complex_num))  #Returns: <class 'str'> 
```


```python
list1d = ["a","b","c"]
str(list1d)         #Returns: "['a', 'b', 'c']"
type(str(list1d))   #Returns: <class 'str'>
# tuples, sets, dictionaries all work similiarly
```


```python
str(len)        #Returns: '<built-in function len>'
type(str(len))  #Returns: <class 'str'>
```

syntax:
```
int(object)
```

> * converts a number or string into an integer object
> * can be used to convert between bases (>= 2 and <=36) 
>     * base 2  (binary) (prefix: 0b)
>     * base 8  (octal) (prefix: 0o)
>     * base 16 (hexadecimal) (prefix: 0x)


```python
num = 3.14
int(num)        #Returns: 3
type(int(num))  #Returns: <class 'int'>

txt = "404"
int(txt)        #Returns: 404
type(int(txt))  #Returns: <class 'int'>
```


```python
int(0b1101) #Returns: 13

binary = "1101"
int(binary, 2) #Returns: 13
```


```python
int(0o147) #Returns: 103

octal = "147"
int(octal, 8) #Returns: 103
```


```python
int(0xff) #Returns: 255

hexadecimal = "ff"
int(hexadecimal, 16) #Returns: 255
```

syntax:
```
float(object)
```
> * converts a number or string into a floating point object if possible


```python
num = 2
float(num)       #Returns: 2.0
type(float(num)) #Returns: <class 'float'>
```


```python
txt = 2.17
float(txt)      #Returns: 2.17
type(float(txt))#Returns: <class 'float'>
```

# `General Order of Operations`
___
|||
|-:|:-:|
|1.| Arithmetic Operators (PEMDAS)|
|2.| Relational Operators (LEFT TO RIGHT)|
|3.| Logical Operators (NAO)|

# `Arithmetic Operators (Math)`
___
> * Order of operations follows PEMDAS from Algebra (BODMAS for the EU)

*PEMDAS --> Parenthesis, Exponents, Multiply/Divide, Add/Subtract*  
*BODMAS --> Brackets, Orders, Division/Multiplication, Addition/Subtraction*

|Symbol| Operation                         |
|:----:|:---------------------------------:|
|   ** | exponentiation (power)            |
|      |                                   |
|   *  | multiplication                    |
|   /  | normal division                   |
|   // | floor division (Integer division) |
|   %  | modulo division (remainder division)|
|      |                                   |
|   +  | addition                          |
|   -  | subtraction                       |

## Exponentiation **    


```python
5 ** 2   #Returns: 25
```

## Multiplication *


```python
5 * 2 #Returns: 10 
```

## Regular Division \\
> * always returns a \<class 'float'\>


```python
5 / 2 #Returns: 2.5 
4 / 2 #Returns: 2.0
```

## Floor Division (Integer Division) \\\\
> * returns a <class 'int'>
> * truncates (2.5 --> 2): cuts off the fractional part


```python
5 // 2 # Returns: 2
```

## Modulo Division (Remainder Division) %
> * returns a <class 'int'>
> * returns the remainder of a division, not the quotient


```python
5 % 2 #Returns: 1
# 5 / 2 == 2 remainder 1
```

## Addition +


```python
5 + 2 #Returns: 7
```

## Subtraction -


```python
5 - 2 #Returns: 3
```

# `Relational Operators (Inequalities)`
___
> * are used for comparisions
> * evaluate to a boolean value (True/False)
> * Order of Operations is Left to Right

|Symbol| Inequality Operation      |
|:----:|:-------------------------:|
|   >  | greater than              |
|   <  | less than                 |
|  >=  | greater than or equal to  |
|  <=  | less than or equal to     |
|  ==  | equal to                  |
|  !=  | not equal to              |



```python
x = 50; y = 45; z = 45

x > y               # Returns: True
x < y               # Returns: False
x >= z              # Returns: True
x <= z              # Returns: False
y == z              # Returns: True
y != x              # Returns: True
```

# `Membership Operators`
___

|Symbol |Membership Operation|
|:-----:|:------------------:|
|in     |apart of            |
|not in |not apart of        |

> * Membership Operators check if a value is found in a sequence
> * ie. checks if one thing is 'apart of' another



```python
txt = "Hello World"
list1d = ["a","b","c"]

"a" in txt      # Returns: False
"a" in list1d   # Returns: True

"d" not in txt      # Returns: True
"d" not in list1d   # Returns: False
```

# `Identity Operators`
___
|Symbol| Identity Operation |
|:----:|:------------------:|
|is    |identical to        |
|is not|not identical       |

> * Identity Operators check if the memory location of the two objects are identical



```python
w = "Hello World"
x = "Hello World"
y = "hello world"

x is y # Returns: False
w is x # Returns: True

x is not w # Returns: False
y is not x # Returns: True

#works similiarly with all data types
```


```python
class Example():
    def __init__(self):
        pass

obj1 = Example()
obj2 = Example()

obj1 is obj2     # Returns: False
obj1 is not obj2 # Returns: True
```

# `Assignment vs. Equality Operators`
___
|Symbol| Operation    | Description |
|:----:|:------------:|:------------|
|=     | assignment   | assigns a value to a variable |
|==    | equality     | compares the value of two objects |
|!=    | not equal to | compares if two objects are not equal|


```python
a = 1 #assigns the variable 'a' to 1

a == 1 # compares if the value of 'a' is equal to 1
# Returns: True
```

# `Compound Assignment Operators`
___
## Compound Assignment Operators
> * are short hand operators for performing an operation and then assigning the result back the to variable


```python
num = 0
num = num + 1 # num = 1 
```

This code above can become tedious when done often.  
There is a shorthand way to perform this type of operation.

|Symbol| Compound Operation |
|:----:|:------------------:|
|+=    | add and assign     |
|-=    | subtract and assign |
|*=    | multiply and assign |
|/=    | divide and assign   |
|//=   | floor divide and assign |
|%=    | modulo (remainder) and assign |
|**=   | exponentiation (power) and assign |

Often it is necessary to change the value of a variable by taking its current value performing and operation then setting the variable to the new value

Like this:
```
variable = current_value + n
```

Compound Operations allow us to shorten this code:
```
variable += n
```
### Compound Operation Examples:


```python
x = 0
x = x ** 1 # Instead of this
x **= 1    # Do this
```


```python
x = 0
x = x * 1 # Instead of this
x *= 1    # Do this
```


```python
x = 0
x = x / 1 # Instead of this
x /= 1    # Do this
```


```python
x = 0
x = x // 1 # Instead of this
x //= 1    # Do this
```


```python
x = 0
x = x % 1 # Instead of this
x %= 1    # Do this
```


```python
x = 0
x = x + 1 # Instead of this
x += 1    # Do this
```


```python
x = 0
x = x - 1 # Instead of this
x -= 1    # Do this
```

|This|Same As|
|:-:|:-:|
|x = x + 1 |x+=1|
|x = x - 1 |x-=1|
|x = x * 1 |x*=1|
|x = x / 1 |x/=1|
|x = x // 1|x//=1|
|x = x % 1 |x%=1|
|x = x ** 1|x**=1|

## Incrementing a Value
> * increasing the value of a variable by 1 or more


```python
number = 0
number += 1 # number = 1
number += 1 # number = 2
```

## Decrementing a Value
> * decreasing the value of a variable by 1 or more


```python
number = 10
number -= 1 # number = 9
number -= 1 # number = 8
number -= 1 # number = 7
```

# `Logical Operators`
___
* Order of Operations
    * NOT
    * AND
    * OR
    
|Operator| Operation| Description|
|:------:|:--------:|:-----------|
| not    | NOT      | opposite   |
| and    | AND      | both       |
| or     | OR       | at least one |

Truth Tables are used to illustrate the evaluation of a logical expression. In this case they show how we evaluate, not, and, and or.  

## NOT truth table
> * returns the opposite


|a|NOT a|
|:-:|:-:|
|True| False|
|False|True|



```python
not True    # Returns: False    
not False   # Returns: True  
```


```python
#examples
is_raining = False

not is_raining # Returns: True 

a = 10
not a < 20 # Returns: False 

is_sunny = True
not is_sunny and is_raining # Returns: True 
```

## AND truth table
> * both must be True to evaluate True

|a|b|a AND b|
|:-:|:-:|:-:|
|True|True|True|
|True|False|False|
|False|True|False|
|False|False|False|


```python
True  and True     # Returns: True
True  and False    # Returns: False 
False and True     # Returns: False 
False and False    # Returns: False 
```


```python
#examples
temperature = 72; is_sunny = True

temperature > 70 and is_sunny
# Returns: True


items = ["apple", "banana", "cherry"]
item1 = "apple"
item2 = "banana"

item1 in items and item2 in items
# Returns: True


username = "user123"; password = "securepass"

username == "user123" and password == "securepass"
# Returns: True

age = 25
has_license = True

age >= 18 and has_license
# Returns: False
```

## OR truth table
> * at least one must be True to evaluate True

|a|b|a OR b|
|:-:|:-:|:-:|
|True|True|True|
|True|False|True|
|False|True|True|
|False|False|False|


```python
True  or True    # Returns: True
True  or False   # Returns: True
False or True    # Returns: True
False or False   # Returns: False
```


```python
temp = 80

temp > 78 or temp < 68 # Returns: True


grade = "D"

grade == "A" or grade == "B" or grade =="C" # Returns: False\


password_hash = "password123"
has_master_key = False

input_password = input()


input_password == password or has_master_key


```

# `De Morgan's Laws`
___
De Morgan's Laws are a set of fundamental principles in logic that describe the relationship between negation (logical NOT) and conjunction (logical AND), as well as negation and disjunction (logical OR). 

*The way these laws are applied to logical operators is similiar to the Distributive Property in Mathematics*

|This|Same As|
|:-:|:-:|
|not(a and b)|(not a or not b)|



```python
a = True or False
b = True or False


# These two statements are equivalent
not(a and b) 
(not a or not b)

not(a and b) == (not a or not b)  # Returns: True 
#regardless of the values for 'a' and 'b'

```

|This|Same As|
|:-:|:-:|
|not(a or b)|(not a and not b)|


```python
a = True or False
b = True or False

# These two statements are equivalent
not(a or b)
(not a and not b) 

not(a or b)  == (not a and not b)  # Returns: True 
#regardless of the values for 'a' and 'b' 
```

 # `Built-in Operation Function Calls`
___


* abs(x,/)
```python
abs(-10) #10
# Returns the absolute value of x. 
```

* max(iterable, *, key, default)
    * \* : separates the positional arguments from the keyword-only arguments that follow.

```python
max(3, 7, 2, 10) #10
# Returns the largest item in an iterable or the largest of two or more arguments.
```

* min(iterable, *, key, default)


```python
min(3, 7, 2, 10) # 2
# Returns the smallest item in an iterable or the smallest of two or more arguments.

```

* sum(iterable, /, start=0)


```python
sum([1, 2, 3, 4, 5]) # 15
# Sums the items of an iterable from left to right and returns the total.

```

* pow(x, y, z=None, /)


```python
pow(2, 3) # 8
# Raises x to the power of y, optionally modulo z.

```

* round(number, ndigits)


```python
round(3.14159, 2) # 3.14
# Rounds a floating-point number to a specified number of decimal digits.

```

* divmod(x, y,/)


```python
divmod(10, 3) # (3,1)
# Returns a tuple containing the quotient and remainder of the division of a by b.

```

* complex([real,imag)


```python
complex(1, 2) # 1 + 2j
# Creates a complex number.
#complex numbers are a built-in data type used to represent numbers in the form of a + bj, 
#where a and b are real numbers, and j represents the imaginary unit (√(-1)).

```

* all(iterable)


```python
round(3.7) # 4
# Rounds a number to the nearest integer.
```

* any(iterable)


```python
all([True, True, False]) #False
# Returns True if all elements of the iterable are true (or if the iterable is empty).
```

# `Bitwise Operations`
___
> * Bitwise operations work on individual bits within data.  
> * Order of operations for Bitwise Operators is Not, Shifts, And, Xor, Or (NSAXO)


|Operation| Symbol|Description|
|:-:|:-:|:-|
|Bitwise NOT| ~| opposite|
|Bitwise SHIFT| << or >>| bit shift left or right|
|Bitwise AND|&| both|
|Bitwise XOR|^| only one|
|Bitwise OR| \|| at least one|

*In bits True and False values are represented by 1 and 0*
|Logic|Bit|
|:-:|:-:|
|True| 1|
|False| 0|


## Binary Data Representation: Two's complement notation.
***To accurately understand bitwise NOT, and bitshift operations an understanding of how Integers are stored in memory is required***

Integers use as many bits as they need in memory  

<br>

In two's complement representation:  
* Positive integers have a leading 0 bit.  
* Negative integers have a leading 1 bit.  


|Positive Integers: conceptually infinite leading 0s|
|:-:| 
|...01 --> 1 | 
|...000000000000000000000001 |


|Negative Integers: conceptually infinite leading 1s| 
|:-:|
|....1 --> -1  |
|....11111111111111111111111 |


## **Bitwise NOT (~)**
> * flips all the bits in a binary number, changing each 0 to 1 and each 1 to 0.
> * When you see NOT think *'opposite'*




```python
x = 3
bin(x)  #Returns: 0b11  --> ...011
bin(~x) #Returns: 0b100 --> ...100
```

Bitwise NOT truth table

|a|~a|
|:-:|:-:|
|1|0|
|0|1|


```python
not 1   #Returns: 0            
not 0   #Returns: 1  
```

## **Bitwise Shift (<<) Left | Right (>>)**
> * moves all the bits in a number by a specified number of positions.

### Left Shift
> * equivalent to (x * 2**shift_amount)


```python
x = 1 #0b1

print( x << 3) #8 --> 0b1000
#               0b 0 0 0 1 --> 0b 1 0 0 0
#shift left 3      3 2 1 0
```

### Right Shift
> * equivalent to (x / 2** shift_amount)


```python
x = 255 #0b10000000

print( x >> 7) # 1 --> 0b1
#                0b 1 0 0 0 0 0 0 0 --> 0b 1
# shift right 7     0 1 2 3 4 5 6 7
```

## **Bitwise AND ( & )**
> * takes two numbers and performs a logical AND operation on each pair of corresponding bits.
> * The resultant bit is 1 if both bits are 1
> * When you see AND think *'both'*


```python
x = 12         # 0b1100 
y = 10         # 0b1010 
x & y          # 0b1000 --> 8
```

Bitwise AND truth table

|a|b|a & b|
|:-:|:-:|:-:|
|1|1|1|
|1|0|0|
|0|1|0|
|0|0|0|


```python
1 and 1  #Returns: 1  
1 and 0  #Returns: 0           
0 and 1  #Returns: 0         
0 and 0  #Returns: 0  
```

## **Bitwise XOR ( ^ )** 

> * takes two numbers and performs a logical XOR operation on each pair of corresponding bits.
> * The resultant bit is 1 if only one bit is 1
> * When you see XOR think *'only one'*


```python
x = 12         # 0b1100 
y = 10         # 0b1010 
x ^ y          # 0b0110 --> 6
```

Bitwise XOR truth table

|a|b|a ^ b|
|:-:|:-:|:-:|
|1|1|0|
|1|0|1|
|0|1|1|
|0|0|0|


```python
1 ^ 1   #Returns: 0          
1 ^ 0   #Returns: 1               
0 ^ 1   #Returns: 1               
0 ^ 0   #Returns: 0 
```

## **Bitwise OR ( | )**
> * takes two numbers and performs a logical OR operation on each pair of corresponding bits
> * The resultant bit is 1 if at least on bit is 1\
> * When you see OR think *'at least one'*


```python
x = 12         # 0b1100 
y = 10         # 0b1010 
x | y          # 0b1110 --> 14
```

### Bitwise OR truth table

|a|b|a \| b|
|:-:|:-:|:-:|
|1|1|1|
|1|0|1|
|0|1|1|
|0|0|0|


```python
1 or 1  #Returns: 1       
1 or 0  #Returns: 1      
0 or 1  #Returns: 1        
0 or 0  #Returns: 0 
```

# `Complete Operator Precedence`
___
*Operations at the same level proceed from left to right*

|Opertors|Description|
|:-:|:-:|
| ()          | Parentheses                     |
| **          | Exponentiation                  |
| +x -x ~x    | Unary plus, unary minus, and bitwise NOT       |
| * / // %    | Multiplication, division, floor division, and modulus       |
| + -         | Addition and subtraction        |
| << >>       | Bitwise left and right shifts   |
| &           | Bitwise AND                     |
| ^           | Bitwise XOR                     |
| \|          | Bitwise OR                      |
| == != > >= < <= | Comparisons             |
| is, is not      | Identity                        |
| in, not in   | Membership operators            |
| not         | Logical NOT                     |
| and         | Logical AND                     |
| or          | Logical OR                      |

***NOTE: If you have trouble remembering operation precedence remember that you can always use parenthesis to make your code clear***


```python
'Appendix'

'Bitwise NOT'
bitwise_NOT = []

for x in range(128):
  x_bin = bin(x)
  bin_not = bin(~x)
  int_not = int(bin_not,2)
  bitwise_NOT.append((x, x_bin, bin_not, int_not ))

print(str(bitwise_NOT).replace("),","),\n"))

[(0,  '0b0', '-0b1', -1),
 (1,  '0b1', '-0b10', -2),
 (2,  '0b10', '-0b11', -3),
 (3,  '0b11', '-0b100', -4),
 (4,  '0b100', '-0b101', -5),
 (5,  '0b101', '-0b110', -6),
 (6,  '0b110', '-0b111', -7),
 (7,  '0b111', '-0b1000', -8),
 (8,  '0b1000', '-0b1001', -9),
 (9,  '0b1001', '-0b1010', -10),
 (10, '0b1010', '-0b1011', -11),

 (11, '0b1011', '-0b1100', -12),
 (12, '0b1100', '-0b1101', -13),
 (13, '0b1101', '-0b1110', -14),
 (14, '0b1110', '-0b1111', -15),
 (15, '0b1111', '-0b10000', -16),
 (16, '0b10000', '-0b10001', -17),
 (17, '0b10001', '-0b10010', -18),
 (18, '0b10010', '-0b10011', -19),
 (19, '0b10011', '-0b10100', -20),
 (20, '0b10100', '-0b10101', -21),

 (21, '0b10101', '-0b10110', -22),
 (22, '0b10110', '-0b10111', -23),
 (23, '0b10111', '-0b11000', -24),
 (24, '0b11000', '-0b11001', -25),
 (25, '0b11001', '-0b11010', -26),
 (26, '0b11010', '-0b11011', -27),
 (27, '0b11011', '-0b11100', -28),
 (28, '0b11100', '-0b11101', -29),
 (29, '0b11101', '-0b11110', -30),
 (30, '0b11110', '-0b11111', -31),

 (31, '0b11111', '-0b100000', -32),
 (32, '0b100000', '-0b100001', -33),
 (33, '0b100001', '-0b100010', -34),
 (34, '0b100010', '-0b100011', -35),
 (35, '0b100011', '-0b100100', -36),
 (36, '0b100100', '-0b100101', -37),
 (37, '0b100101', '-0b100110', -38),
 (38, '0b100110', '-0b100111', -39),
 (39, '0b100111', '-0b101000', -40),
 (40, '0b101000', '-0b101001', -41),

 (41, '0b101001', '-0b101010', -42),
 (42, '0b101010', '-0b101011', -43),
 (43, '0b101011', '-0b101100', -44),
 (44, '0b101100', '-0b101101', -45),
 (45, '0b101101', '-0b101110', -46),
 (46, '0b101110', '-0b101111', -47),
 (47, '0b101111', '-0b110000', -48),
 (48, '0b110000', '-0b110001', -49),
 (49, '0b110001', '-0b110010', -50),
 (50, '0b110010', '-0b110011', -51),

 (51, '0b110011', '-0b110100', -52),
 (52, '0b110100', '-0b110101', -53),
 (53, '0b110101', '-0b110110', -54),
 (54, '0b110110', '-0b110111', -55),
 (55, '0b110111', '-0b111000', -56),
 (56, '0b111000', '-0b111001', -57),
 (57, '0b111001', '-0b111010', -58),
 (58, '0b111010', '-0b111011', -59),
 (59, '0b111011', '-0b111100', -60),
 (60, '0b111100', '-0b111101', -61),

 (61, '0b111101', '-0b111110', -62),
 (62, '0b111110', '-0b111111', -63),
 (63, '0b111111', '-0b1000000', -64),
 (64, '0b1000000', '-0b1000001', -65),
 (65, '0b1000001', '-0b1000010', -66),
 (66, '0b1000010', '-0b1000011', -67),
 (67, '0b1000011', '-0b1000100', -68),
 (68, '0b1000100', '-0b1000101', -69),
 (69, '0b1000101', '-0b1000110', -70),
 (70, '0b1000110', '-0b1000111', -71),

 (71, '0b1000111', '-0b1001000', -72),
 (72, '0b1001000', '-0b1001001', -73),
 (73, '0b1001001', '-0b1001010', -74),
 (74, '0b1001010', '-0b1001011', -75),
 (75, '0b1001011', '-0b1001100', -76),
 (76, '0b1001100', '-0b1001101', -77),
 (77, '0b1001101', '-0b1001110', -78),
 (78, '0b1001110', '-0b1001111', -79),
 (79, '0b1001111', '-0b1010000', -80),
 (80, '0b1010000', '-0b1010001', -81),

 (81, '0b1010001', '-0b1010010', -82),
 (82, '0b1010010', '-0b1010011', -83),
 (83, '0b1010011', '-0b1010100', -84),
 (84, '0b1010100', '-0b1010101', -85),
 (85, '0b1010101', '-0b1010110', -86),
 (86, '0b1010110', '-0b1010111', -87),
 (87, '0b1010111', '-0b1011000', -88),
 (88, '0b1011000', '-0b1011001', -89),
 (89, '0b1011001', '-0b1011010', -90),
 (90, '0b1011010', '-0b1011011', -91),

 (91, '0b1011011', '-0b1011100', -92),
 (92, '0b1011100', '-0b1011101', -93),
 (93, '0b1011101', '-0b1011110', -94),
 (94, '0b1011110', '-0b1011111', -95),
 (95, '0b1011111', '-0b1100000', -96),
 (96, '0b1100000', '-0b1100001', -97),
 (97, '0b1100001', '-0b1100010', -98),
 (98, '0b1100010', '-0b1100011', -99),
 (99, '0b1100011', '-0b1100100', -100),
 (100, '0b1100100', '-0b1100101', -101),

 (101, '0b1100101', '-0b1100110', -102),
 (102, '0b1100110', '-0b1100111', -103),
 (103, '0b1100111', '-0b1101000', -104),
 (104, '0b1101000', '-0b1101001', -105),
 (105, '0b1101001', '-0b1101010', -106),
 (106, '0b1101010', '-0b1101011', -107),
 (107, '0b1101011', '-0b1101100', -108),
 (108, '0b1101100', '-0b1101101', -109),
 (109, '0b1101101', '-0b1101110', -110),
 (110, '0b1101110', '-0b1101111', -111),

 (111, '0b1101111', '-0b1110000', -112),
 (112, '0b1110000', '-0b1110001', -113),
 (113, '0b1110001', '-0b1110010', -114),
 (114, '0b1110010', '-0b1110011', -115),
 (115, '0b1110011', '-0b1110100', -116),
 (116, '0b1110100', '-0b1110101', -117),
 (117, '0b1110101', '-0b1110110', -118),
 (118, '0b1110110', '-0b1110111', -119),
 (119, '0b1110111', '-0b1111000', -120),
 (120, '0b1111000', '-0b1111001', -121),

 (121, '0b1111001', '-0b1111010', -122),
 (122, '0b1111010', '-0b1111011', -123),
 (123, '0b1111011', '-0b1111100', -124),
 (124, '0b1111100', '-0b1111101', -125),
 (125, '0b1111101', '-0b1111110', -126),
 (126, '0b1111110', '-0b1111111', -127),
 (127, '0b1111111', '-0b10000000', -128)]

'Bitwise Shift (<<) Left | Right (>>)'
def create_shift_table(number, shift):
    """
    Creates a table that shows the results of left and right bit shifts for integers.

    Args:
        number (int): The maximum number to include in the table.
        shift (int): The number of positions to shift left or right.

    Returns:
        list: A list of tuples representing the shift table, each tuple containing:
            - The original number
            - Its binary representation
            - The result of left shifting the number by the given shift
            - The binary representation of the left shifted result
            - The result of right shifting the number by the given shift
            - The binary representation of the right shifted result

    Example:
        create_shift_table(5, 2) returns:
        [
            ('number', 'binary', 'left_int', 'left_bin', 'right_int', 'right_bin'),
            (0, '0b0', 0, '0b0', 0, '0b0'),
            (1, '0b1', 4, '0b100', 0, '0b0'),
            (2, '0b10', 8, '0b1000', 0, '0b0'),
            (3, '0b11', 12, '0b1100', 0, '0b0'),
            (4, '0b100', 16, '0b10000', 1, '0b1'),
            (5, '0b101', 20, '0b10100', 1, '0b1')
        ]
    """
    shifts = [("number", "binary", 'left_int', 'left_bin', 'right_int', 'right_bin')]
    for x in range(number):
        binary = bin(x)
        left_int = x << shift
        left_bin = bin(left_int)
        right_int = x >> shift
        right_bin = bin(right_int)
        shifts.append((x, binary, left_int, left_bin, right_int, right_bin))

    return shifts
```
