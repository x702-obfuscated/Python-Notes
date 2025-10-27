# `[ For Loops: Challenges ]`

| `INSTRUCTIONS` |
|:-:|
| All assignment code should be written inside of the `main.py` file. |
| In VS Code use `CTRL + J` to open the terminal. |
| In the terminal type `python main.py` to execute your code. |
| In the terminal type `python test.py` to test your code for correctness. |


<br>

* `Preconditions` are requirements that must be true before a function is called in order for the function to operate correctly.

* `Constraints` are rules that tell you what you can or cannot do when solving a problem.

* `Inclusive` means that the values should be included.

* `Iteration` in programming refers to the process of repeatedly executing a set of instructions or a block of code.
    * `An iteration` is exactly one repetition 

* `Hard coding` is the process of manually programming something that could be written programmatically.

<br>

---
<br>

# `Challenges`

---
<br>

### `Q1`
Define a variable named `ranges` and assign it to a list that contains the following range objects:
    
1. a range from 0 to 15 by 1s
1. a range from 5 to 25 by 5s
1. a range from -10 to -2 by 2s
1. a range from -50 to -10 by 10s
1. a range from -5 to 5 by 1s
1. a range from -100 to 100 by 20s
1. a range from 10 to -10 by -5s
1. a range from 50 to -50 by -10s
1. a range from -3 to 9 by 3s
1. a range from 20 to -4 by -2s

<br>

Constraints:
* `ranges` must contain range objects and in the same order as above.


---
<br>

### `Q2`


Define a variable named `default_step` and assign it to a range object storing 50 to 70 by 1s. Use the default step parameter value for range objects.
Define a variable named `default_start_step` and assign it to a range object storing 0 to 100 by 1s. Use the default start and step parameter values for range objects.

<br>

Constraints:
* `default_step` must contain a range object that is constructed using the default step parameter value.
* `default_start_step` must contain a range object that is constructed using the default start and step parameter values.

---
<br>

### `Q3`
Define a function named `upcount` with the parameters `start`, `stop`, and `step`. 
* `start`, `stop`, and `step` each represent any integer value.

<br>

In the function definition write a for loop that prints out each value from `start` to `stop` inclusive on the same line with a space after each value and increasing by a value of `step` each iteration.

<br> 

Preconditions:
* `start` value must be less than `<` the value of `stop`
* The value of `step` must be positive (`step > 0`)

<br>

Constraints:
* You must use a for loop.



---
<br>

### `Q4`

Define a function named `downcount` with the parameters `start`, `stop`, and `step`. 
* `start`, `stop`, and `step` each represent any integer value.

<br>

In the function definition write a for loop that prints out each value from `start` to `stop` inclusive on the same line with a space after each value and decreasing by a value of `step` each iteration.

<br> 

Preconditions:
* `start` value must be greater than `>` the value of `stop`
* The value of `step` must be positive (`step > 0`)

<br>

Constraints:
* You must use a for loop.

---
<br>

### `Q5`
Define a function named `onlyodds` with the parameter `lst`.
* `lst` represents a list of integers

<br>

In the function definition write a for loop that prints out only the odd numbers found in `lst`. Each value should be printed on the same line with a space after each item. 


<br>

Constraints: 
*  You must use a for loop.
*  The function must work for any length of `lst`
*  The function must work for all integer values in `lst`

---
<br>

### `Q6`
Define a function named `total` with the parameter `nums`.
* `nums` represents a list of integers

<br>

In the function definition write a for loop that adds up all the numbers in `nums`, and returns the result.


<br>

Constraints: 
*  You must use a for loop
*  The function must work for length of `nums`
*  The function must work for all integer values in `nums`

---
<br>

### `Q7`
Define a function named `num_vowels` with a parameter named `txt`.
* `txt` represent a string of any length.

<br>

In the function definition write a for loop that counts the number of vowels in `txt` and returns the result.


<br>

Constraints: 
*  You must use a for loop.
*  The function must work for any string value of `txt`

---
<br>


### `Q8`
Define a function named `search` with 2 parameters `lst`, and `item`.
* `lst` represents a list of any length.
* `item` represents the element to be searched for.

<br>

In the function definition write a for loop that loops through each element of `lst` and returns a list of each index that `item` appears in the list.
If `item` does not appear in `lst` return and empty list.


<br>

Constraints: 
*  You must use a for loop.
*  The function must work for any possible value of `lst`
*  The function must return a list

---
<br>



*`Created and maintained by Mr. Merritt`*