# `[ Lists : Challenges ]`

| `INSTRUCTIONS` |
|:-:|
| All assignment code should be written inside of the `main.py` file. |
| In VS Code use `CTRL + J` to open the terminal. |
| In the terminal type `python main.py` to execute your code. |
| In the terminal type `python test.py` to test your code for correctness. |


<br>


* A `constraint` is a rule that tells you what you can or cannot do when solving a problem.

* `Hard coding` is the process of manually programming something that could be written programmatically.

<br>

---
<br>

# `Challenges`

---
<br>

### `Q1`
Define a variable named `empty` and assign it an empty list.

<br>

Constraints: 
* You may not use the list constructor call. 

---
<br>

### `Q2`
Define a variable named `my_letters` and assign it a list containing the individual characters of your first name. 

<br>

Constraints:
* You may not use the list constructor call. 

---
<br>

### `Q3`

Define a variable named `arabic_numerals` and assign it a list containing the characters 0-9.
* Use the list constructor to create the list. 

<br>   

Constraints:
* The list must contain characters, not integers
* The list must be created using the list constructor function. 


---
<br>

### `Q4`

Define a variable named `upper_alpha` and assign it to reference a list of all the uppercase characters in the alphabet.

Define a variable named `lower_alpha` and assign it to reference a list of all the lowercase characters in the alphabet.

Define a variable named `numerals` and assign it to reference a list of the integers 0 to 9

<br>

Define a function named `is_apart` with two parameters: 
1. `val` which represents the value to check. 
2. `lst` which represents a list

The function should check if `val` is found in `lst` and return a boolean. 

<br>

Constraints:
* The parameters must be in correct order `val` then `lst`

---
<br>

### `Q5`

Define a variable named `character` and assign it to reference any character of your choice. 

Call `is_apart` once for each of the following pairs of arguments: 
1. `character` and `upper_alpha`
2. `character` and `lower_alpha`
3. `character` and `numerals`

Print the result of each call.

<br>

Constraints:
* The print call must contain the `is_apart` call. 

---
<br>

### `Q6`

Concatenate `upper_alpha`, `lower_alpha`, and `numerals` into one list. Assign the result to a variable named `alphanumeric`.

<br>

Constraints:
* You must use the variables `upper_alpha`, `lower_alpha`, and `numerals` when concatenating.

---
<br>

### `Q7`

Define a variable named `front` and a variable named `back`. Assign each a different list of values. You may choose what values each list stores. 
        
Concatenate `front` to `back` and assign the result to a new variable named `joined`

<br>

Constraints:
* `front` must be the first half of `joined`

---
<br>

### `Q8`

Define a variable named `grouped` and assign it to reference an empty list.
1. Then concatenate `grouped` and `upper_alpha` and assign the result back to `grouped`
2. Then concatenate `grouped` and `lower_alpha` and assign the result back to `grouped`
3. Then concatenate `grouped` and `numerals` and assign the result back to `grouped`
4. Finally print out the value of `grouped`

<br> 

Concatenate:
* You must concatenated and assign in a single statement.
* `grouped` can only be used once per statement.

---
<br>

### `Q9`

Define a variable named `zeros` and assign it to reference a list containing 1000 integer 0s.

<br>

Constraints:
* Hard coding the 0s does not count. 
* You may not use any other variables.

---
<br>

### `Q10`

Define a variable named `binary` and assign it to reference a list containing each digit of 10001101.

Duplicate `binary` 500 times and assign the result back to `binary` in the same statement.

<br>

Constraints:
* Each digit must be a seperate element in the list. 
* You must duplicate and assign in the same statement.
* `binary` may only be used once per statement.

---
<br>

### `Q11`

Using subscripting notation print out the following from the list `alphanumeric`.
1. The first element using positive indexing.
2. The last element using negative indexing.
3. The 43rd element using positive indexing.
4. The 16th to last element using negative indexing.

<br>

Constraints:
* `alphanumeric` must come from the previous question in this set.

---
<br>

### `Q12`

Define a variable named `pylist` and assign it to reference a list of  100 spaces `" "`.
1. change the 50th element to be "PYTHON"
2. change the 19th to last element to be "PROGRAMMING"

<br>

Constraints:
* Hard coding the list will not count. You must use subscripting.

---
<br>

### `Q13`

Using slicing notation print out the following substrings from the list `alphanumeric`.
1. The first 26 characters (positive indexes)
2. The last 10 characters  (negative indexes)
3. The 27th character to the 52nd character (positive indexes)
4. Every 3rd character in the whole list    (positive indexes)
5. The whole list in reverse.

<br>

Constraints:
* Hard coding values will not count.
* You must use subscripting notation.
* Use are expected to use default values when applicable.

---
<br>

*`Created and maintained by Mr. Merritt`*