# `[ Conditionals : Challenges ]`

| `INSTRUCTIONS` |
|:-:|
| All assignment code should be written inside of the `main.py` file. |
| In VS Code use `CTRL + J` to open the terminal. |
| In the terminal type `python main.py` to execute your code. |
| In the terminal type `python test.py` to test your code for correctness. |


<br>

* A `requirement` requirement is a something that must be handled by the program.

* A `constraint` is a rule that tells you what you can or cannot do when solving a problem.

* `Hard coding` is the process of manually programming something that could be written programmatically.

<br>

---
<br>

# `Challenges`

---
<br>


### `Q1`
Define a function named `is_True` with a parameter named `var`. The function should use a conditional to determine if `var` is equal to True. 

* If it is, the function returns True.  
* If it is NOT, the function returns False.

<br>

Constraints:
* Your function must work for any value of `var`.
* You must use a conditional in the function definition.


`Hint: Check the notes on Truthiness`

---
<br>


### `Q2`
Define a function named `get_sign` with a parameter named `num`. Inside the function write a conditional that returns if `num` is a positive or negative number.  
* If `num` is positive return "POSITIVE".  
* If `num` is negative return "NEGATIVE".
* If `num` is zero return "ZERO".

<br>

Constraints:
* You must use a conditional in the function definition.

---
<br>

### `Q3`
Define a function named `is_even` with a parameter named `number`. 

Inside the definition write a conditional:
* If `number` is even return "EVEN".  
* If `number` is odd return "ODD".

<br>

Constraints:
* You must use a conditional in the function definition.

---
<br>


### `Q4`

Define a function named `is_divisible` with 2 parameters `dividend` and `divisor`. In the function definition, write a conditional that returns if the `dividend` is divisible by the `divisor`.

* If `divisor` is 0 return "Division by 0 is UNDEFINED"

* If `dividend` is divisible by `divisor`, return a concatenated string → `dividend` + " is divisible by " + `divisor`.  

* If `dividend` is NOT divisible by `divisor`, return a concatenated string → `dividend` + " is NOT divisible by " + `divisor`.

<br>

Constraints:
* The parameters must be written in the order they were provided.

---
<br>


### `Q5`
Define a function named `stoplight` with a parameter named `color`. `color` represents one of 3 possible values → `"red"`, `"yellow"`, or `"green"`. 

<br>

In the function definition, write a conditional:
* If `color` is "green", return "GO".
* If `color` is "yellow", return "CAUTION".
* If `color` is "red", return "STOP".
* If `color` is any other value return "ERROR".

<br>

Constraints:
* You must use a conditional in the function definition.

---
<br>


### `Q6`

Define a function named `alarm` with the parameter `time`. `time` represents any hour on a 24-hour clock (0-23).

<br>

Write a conditional inside the function definition:
* If `time` is after 22 or before 8 return "SLEEP".
* Otherwise return "WAKEUP" 

<br>

Constraints:
* You must use a conditional in the function definition.




---
<br>


### `Q7`

Define a function named `is_vowel` with the parameter `char`. `char` represents any lowercase alphabetical character (a-z).

<br>

Write a conditional inside of the function definition:
* If `char` is a vowel return "VOWEL".
* if `char` is not a vowel return "CONSONANT".

<br>

Constraints:
* DO NOT include the character "y" as a vowel. 
* You must use a conditional in the function definition



---
<br>



### `Q8`

Define a function named `get_max` with the parameters `a`,`b`, and `c`. `a`,`b`, and `c` each represent any possible integer value. 

<br>

Write a conditional in the function definition to determine which of the 3 parameters references the largest value. 
* If `a` is the largest return `a`
* If `b` is the largest return `b`
* If `c` is the largest return `c`
* If `a`,`b`, and `c` are equal return any of the 3.
* If any two are equal and larger than the third return either of the two. 

<br>

Constraints:
* You must use a conditional in the function definition.




---
<br>


### `Q9`

Define a function named `get_quadrant` with the parameters `x` and `y`. `x` and `y` represent any possible integer coordinate value in a standard Cartesian coordinate plane. 

<br>

Write a conditional in the function definition that returns the quadrant that (`x`,`y`) coordinate pair appears.
* If `x` and `y` are both 0 return "ORIGIN".
* If just `x` is 0 return "X-AXIS".
* If just `y` is 0 return "Y-AXIS".
* If `x` is positive and `y` is positive return "QI".
* If `x` is negative and `y` is positive return "QII".
* If `x` is negative and `y` is negative return "QIII".
* If `x` is positive and `y` is negative return "QIV".

<br>

Constraints:
* You must use a conditional in the function definition.

---
<br>


### `Q10`

Define a function named `calculate` with the parameters `a`, `b`, and `operation`. 
* `a` and `b` represent any two integer values.
* `operation` represents one of 4 string characters: "+", "-", "*", "/".

<br>

Write a conditional in the function definition:
* If `operation` is "+", return the sum of `a` and `b`.
* If `operation` is "-", return the difference of `a` and `b`.
* If `operation` is "/", return the quotient of `a` and `b`.
    * If `b` is 0, return "UNDEFINED".
* If `operation` is "*", return the product of `a` and `b`.
* If `operation` is not one of the 4 possible `operation` values, return "Operation Not Supported".

<br>

Constraints:
* You must use a conditional in the function definition.


---
<br>


*`Created and maintained by Mr. Merritt`*