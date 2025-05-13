# `Python Iterators`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*

[Python3 Documentation](https://docs.python.org/3/)
___

Covered in this file:
1. [`Iterators Defined`](#iterators-defined)
1. [`Iterator vs Iterable`](#iterator-vs-iterable)
1. [`Creating an Iterator from an Iterable`](#creating-an-iterator-from-an-iterable)
1. [`Creating a Custom Iterable`](#creating-a-custom-iterable)
1. [`Creating a Custom Iterator`](#creating-a-custom-iterator)

<br>

___

<br>

# `Iterators Defined`

Basically: An Iterator is an object that allows the return of its items one at a time. 

<br>

Specifically: An Iterator is an object that defines the `__iter__()` method and the `__next__()` method and returns items one at a time without the need to store the collection in memory.
* `__iter__()` returns the iterator object
* `__next__()` returns the next item in a sequence or raises the `StopIteration` Exception.

<br>

### Features of Iterators:
1. `Generates Items`: Iterators return items one at a time as needed.
1. `Stateful Traversal`: Iterators track the current position during iteration
1. `Exhaustion`: Once an item is used it is "consumed", and once all items are used the iterator is "empty" and cannot be used again.
1. `Memory Efficiency`: Iterators are memory efficient by not loading all data into memory, and instead generate the items on the fly.

1. `Lazy Evaluation`: Values are computed only when needed, and can lead to better performance. 

<br>

`NOTE: Iterators are single use`

<br>

[Back To Top](#python-iterators)

___

<br>

# `Iterator vs Iterable`

* An `Iterable` is any object capable of returning its elements one at a time.
* An `Iterator` is an object the tracks its position in a sequence (state) and returns the next value when next() is called. 

| Feature                           | **Iterable**              | **Iterator**                  |
| --------------------------------- | ------------------------- | ----------------------------- |
| Can be looped through with `for`? | ✅ Yes                     | ✅ Yes                         |
| Has `__iter__()`?                 | ✅ Yes                     | ✅ Yes                         |
| Has `__next__()`?                 | ❌ No                      | ✅ Yes                         |
| Used with `iter()`?               | ✅ Yes                     | Not needed (already iterable) |
| Keeps state?                      | ❌ No (restarts each time) | ✅ Yes                         |


<br>

[Back To Top](#python-iterators)

___

<br>

# `Creating an Iterator from an Iterable`
To create an Iterator from an Iterable used the built-in `iter()` function.
* Use the built-in `next()` function to return the next item.

syntax:
```
iter(iterable)
```
```
next(iterator)
```
example:
```python
data = [2,4,6,8,10]
it = iter(data)

print(next(it))     # Output: 2
print(next(it))     # Output: 4
print(next(it))     # Output: 6
```

<br>

[Back To Top](#python-iterators)

___

<br>

# `Creating a Custom Iterable`
To create a custom iterable, write a class that defines the `__iter__()` dunder method.
* The __iter__() method is used to make an object iterable by returning an iterator object.


<br>

syntax:
```
__iter__(self):
    ...
```
examples:
```python
class Player:
    def __init__(self):
        self.items = ["potion","sword","shield","armor"]

    def __iter__(self):
        return iter(self.items)


player = Player() # player is iterable, because Player defines __iter__

for item in player:
    print(item, end = ", ")

# Output: 
# potion, sword, shield, armor,
```



<br>

[Back To Top](#python-iterators)

___

<br>

# `Creating a Custom Iterator`
To create a custom iterator, write a class that defines the `__iter__()` and `__next__()` dunder methods.
* The __iter__() method returns *`self`* when the class defines the `__next__()` method. 
* The __next__() method defines how to return each item in sequence, and when there are no more items raises a `StopIteration` Exception

<br>

syntax:
```
__iter__(self):
    ...

__next__(self):
    ...
```
examples:
```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.spot = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.spot < self.limit:
            self.spot += 1
            return self.spot
        else:
            raise StopIteration




counter = Counter(15)
for number in counter:
    print(number, end = " ")  

# Output:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
```
```python
class Fibonacci:
    def __init__(self,num):
        self.__num = num
        self.__step = 0
        self.__pointer_one = 1
        self.__pointer_two = 1


    def __iter__(self):
        return self

    def __next__(self):
        self.__step += 1

        if self.__step > self.__num:
            raise StopIteration

        if self.__step in (1,2):
            return 1

        result = self.__pointer_one + self.__pointer_two
        self.__pointer_one, self.__pointer_two = self.__pointer_two, result

        return result 



for i in Fibonacci(10):
    print(i, end = " ")

# Output: 
# 1 1 2 3 5 8 13 21 34 55
```
```python
class Alphabet:
    def __init__(self):
        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.spot = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.spot += 1

        if self.spot > len(self.letters):
            raise StopIteration
    
        return self.letters[self.spot-1]



for letter in Alphabet():
    print(letter, end = " ")

# Output:
# a b c d e f g h i j k l m n o p q r s t u v w x y z 
```
<br>

[Back To Top](#python-iterators)

___

<br>

*Created and maintained by Mr. Merritt*