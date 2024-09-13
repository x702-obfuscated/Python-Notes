# `Python Boolean Expressions`
___

Covered in this file:

1. [`Review: Booleans, Relational, Membership, Identity, and Logical Operators`](#review-booleans-relational-membership-identity-and-logical-operators)
    1. [`Boolean (True/False)`](#booleans-truefalse)
    1. [`Comparision aka Relation Operators`](#comparision-aka-relational-operators)
    1. [`Identity Operators`](#identity-operators)
    1. [`Membership Operators`](#membership-operators)
    1. [`Logical Operators`](#logical-operators)
    1. [`Abbreviated Operator Precedence`](#abbreviated-operator-precedence)
1. [`Defining Boolean Expressions`](#defining-boolean-expressions)
1. [`Truthiness: Special Note on Evaluating Boolean Expressions`](#truthiness-special-note-on-evaluating-boolean-expressions)
1. [`Boolean Expression Examples`](#boolean-expression-examples)




<br>

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

[Back to Top](#python-boolean-expressions)

___

<br>


# `Defining Boolean Expressions`
Basically: A `boolean expression` is any expression that is answered with `True` or `False`

Specifically: A `boolean expression` is an expression in programming that evaluates to a Boolean value, which is either True or False. 

<br>

* Boolean expressions are fundamental in controlling the flow of programs, as they are used in conditional statements, loops, and logical operations.

* Boolean expressions use differing combinations of comparision, identity, membership, and logical operators to evaluate conditions and control the flow of a program.

<br>


## `Note on Boolean Expressions and Conditionals`
*When it comes to boolean expressions and conditional statements, the range of possibilities is vast and varied. The examples provided here are intended to illustrate some of the fundamental concepts and common use cases. However, it is impossible to cover every possible scenario or combination of conditions that may arise in real-world programming.*

<br>

[Back to Top](#python-boolean-expressions)

___

<br>

# `Truthiness: Special Note on Evaluating Boolean Expressions`
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

[Back to Top](#python-boolean-expressions)

___

<br>

# `Boolean Expression Examples`


```python
# 1. Relational and Logical
print(10 > 5 and 5 < 10)  # Output: True
```
Evaluation steps:
1. 10 > 5 evaluates to True
1. 5 < 10 evaluates to True
1. True and True results in True

<br>


```python
# 2. Relational and Logical
print(15 != 10 or 10 == 5)  # Output: True
```
Evaluation steps:
1. 15 != 10 evaluates to True
1. 10 == 5 evaluates to False
1. True or False results in True

<br>

```python
# 3. Membership
print('a' in 'apple')  # Output: True
```
Evaluation steps:
1. 'a' is found in 'apple', so the result is True

<br>

```python
# 4. Membership and Logical
print(3 in [1, 2, 3, 4] and 5 not in [1, 2, 3, 4])  # Output: True
```
Evaluation steps:
1. 3 in [1, 2, 3, 4] evaluates to True
1. 5 not in [1, 2, 3, 4] evaluates to True
1. True and True results in True

<br>

```python
# 5. Identity
a = [1, 2, 3]
b = a
print(a is b)  # Output: True
```
Evaluation steps:
1. a and b refer to the same object in memory
1. a is b results in True

<br>

```python
# 6. Identity and Logical
x = 5
y = 5
print(x is y or x is not y)  # Output: True
```
Evaluation steps:
1. x is y evaluates to True (because Python caches small integers like 5)
1. x is not y evaluates to False
1. True or False results in True

<br>

```python
# 7. Membership and Relational
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits and len(fruits) == 3)  # Output: True
```
Evaluation steps:
1. "banana" in fruits evaluates to True
1. len(fruits) == 3 evaluates to True
1. True and True results in True

<br>

```python
# 8. Logical and Relational
num = 20
print(num > 10 and num < 30)  # Output: True
```
Evaluation steps:
1. num > 10 evaluates to True
1. num < 30 evaluates to True
1. True and True results in True

<br>

```python
# 9. Identity and Logical
c = 10
d = 10
print(not (c is d))  # Output: False
```
Evaluation steps:
1. c is d evaluates to True (small integers like 10 are cached by Python)
1. not True results in False

<br>

```python
# 10. Membership, Relational, and Logical
numbers = [1, 2, 3, 4, 5]
print(5 in numbers and (max(numbers) == 5))  # Output: True
```
Evaluation steps:
1. 5 in numbers evaluates to True
1. max(numbers) == 5 evaluates to True
1. True and True results in True

<br>

```python
# 11. Membership, Relational, and Logical
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits or len(fruits) > 5)  # Output: True
```
Evaluation steps:
1. 'banana' in fruits evaluates to True
1. len(fruits) > 5 evaluates to False
1. True or False results in True

<br>

```python
# 12. Membership, Relational, and Logical
numbers = [10, 20, 30, 40]
print(50 not in numbers and min(numbers) > 0)  # Output: True
```
Evaluation steps:
1. 50 not in numbers evaluates to True
1. min(numbers) > 0 evaluates to True
1. True and True results in True

<br>

```python
# 13. Relational and Logical
x, y = 7, 10
print(x < y and x % 2 == 1)  # Output: True
```
Evaluation steps:
1. x < y evaluates to True
1. x % 2 == 1 evaluates to True
1. True and True results in True

<br>

```python
# 14. Relational and Logical
a, b, c = 3, 5, 7
print(a + b == c or c - a == b)  # Output: True
```
Evaluation steps:
1. a + b == c evaluates to True
1. c - a == b evaluates to True
1. True or True results in True

<br>

```python
# 15. Membership, Relational, and Logical
colors = ['red', 'blue', 'green']
print('yellow' not in colors and len(colors) == 3)  # Output: True
```
Evaluation steps:
1. 'yellow' not in colors evaluates to True
1. len(colors) == 3 evaluates to True
1. True and True results in True

<br>

```python
# 16. Relational and Logical
m, n = 12, 15
print(m >= 10 and n <= 20)  # Output: True
```
Evaluation steps:
1. m >= 10 evaluates to True
1. n <= 20 evaluates to True
1. True and True results in True

<br>

```python
# 17. Relational and Logical
p, q = -5, 5
print(p * -1 == q or q < 0)  # Output: True
```
Evaluation steps:
1. p * -1 == q evaluates to True
1. q < 0 evaluates to False
1. True or False results in True

<br>

```python
# 18. Relational and Logical
x = 8
print(x % 2 == 0 and x ** 2 > 50)  # Output: True
```
Evaluation steps:
1. x % 2 == 0 evaluates to True
1. x ** 2 > 50 evaluates to True
1. True and True results in True

<br>

```python
# 19. Membership and Logical
vowels = ['a', 'e', 'i', 'o', 'u']
print('a' in vowels and 'b' not in vowels)  # Output: True
```
Evaluation steps:
1. 'a' in vowels evaluates to True
1. 'b' not in vowels evaluates to True
1. True and True results in True

<br> 

```python
# 20. Relational and Logical
age = 20
print(age >= 18 and age < 30)  # Output: True
```
Evaluation steps:
1. age >= 18 evaluates to True
1. age < 30 evaluates to True
1. True and True results in True


<br>

[Back to Top](#python-boolean-expressions)

___

<br>


*Created and maintained by Mr. Merritt* 