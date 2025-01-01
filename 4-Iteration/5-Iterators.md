*WORK IN PROGRESS, CHECK BACK LATER FOR UPDATES*
# `Python Iterators`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*
___

Covered in this file:
1. [``]()


<br>

___

<br>

# ``

<br>

[Back To Top](#python-iterators)

___

<br>

*Created and maintained by Mr. Merritt*

iterators
__iter__()
__next__()
raise StopIteration

```python
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
```



In Python, an iterator is an object that enables you to traverse through a sequence of data, one item at a time. It provides a way to access elements of a collection sequentially without the need to store the entire collection in memory.

Key Features of Iterators:
Generates items one at a time:

Iterators produce elements as needed rather than storing all elements at once. This is particularly useful for working with large datasets.
Stateful traversal:

An iterator remembers its current position during iteration. Once it provides an item, it moves to the next one.
Exhaustion:

Once all items are consumed, the iterator is "empty." Trying to iterate over it again will not yield any results.
Example of an Iterator in A

```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

# Using the custom iterator
counter = Counter(3)
for number in counter:
    print(number)  # Output: 1 2 3
```

Memory efficiency:
Since they generate items on the fly, iterators can handle large data without loading everything into memory.
Lazy evaluation:
Values are computed only when needed, which can lead to performance benefits.