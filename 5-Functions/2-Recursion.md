# `Python Recursion`
*Use CTRL + F to search for keywords in this file*  
*You are encouraged to copy and alter the code in this file to understand how it works*


___

Covered in this file:

1. [`Note on symbols used in this file`](#note-on-symbols-used-in-this-file)
1. [`Recursion Defined`](#recursion-defined)
1. [`Writing a base case`](#writing-a-base-case)
1. [`RecursionError: maximum recursion depth exceeded`](#recursionerror-maximum-recursion-depth-exceeded)
1. [`Common Recursive Algorithms`](#common-recursive-algorithms)
    1. [`Factorial Calculation`](#factorial-calculation)
    1. [`Fibonacci Sequence`](#fibonacci-sequence)
    1. [`Binary Search`](#binary-search)
    1. [`Merge Sort`](#merge-sort)
    1. [`Quick Sort`](#quick-sort)
    1. [`Permutations`](#permutations)
    1. [`Combinations`](#combinations)
    1. [`Depth First Search`](#depth-first-search)
    1. [`Breadth-First Search`](#breadth-first-search)

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

[Back to Top](#python-recursion)

___

<br>

### `Abstract vs. Real Examples`
In this file there are two types of examples, `abstract` and `real`. 

`Abstract` examples are a generalized, simplified representation that highlights the core concept or principle without including unnecessary details or specific instances. 

`Real` Examples are specific instances that illustrate the concept, principle, or method by providing concrete details. 

<br>

[Back to Top](#python-recursion)

___

<br>



# `Recursion Defined`
Basically: `Recursion` is the process of calling a function inside of itself

Specifically: `Recursion` is a programming technique in which a function calls itself directly or indirectly in order to solve a problem

<br>

Recursive algorithms are made of 3 parts:
* base case (aka the stop case)
* function code
* recursive call

<br>

*When a function executes the program stops at that point and executes the function code. When a recursive function is called this process may occur many times, until the final call meets the base case and returns. This results in the previous call returning, then the next, and so on until the original call returns. This is because each function call is placed on the stack along with its data, until it ends.*

<br>

syntax:
```
def recursive_function(parameters, ...):
    <base case>
    <function code>
    <recursive call>
    ...
```

<br>

abstract example:
```python
def recurse(n):
    if (n <= 1):
        print("Base Case Executed...")
        return

    print(f"Recursive Call: {n}")
    return recurse(n - 1)

recurse(5) 
# Output:
# Recursive Call: n = 5    
# Recursive Call: n = 4    
# Recursive Call: n = 3    
# Recursive Call: n = 2    
# Base Case Executed: n = 1
```

*The best way to visualize how recursive algorithms work is to use a debugging tool to step through the code execution.*

<br>

[Back to Top](#python-recursion)

___

<br>

# `Writing a base case`
The base case is the case that stops the recursive calls and returns

Recursive algorithms need a condition upon which the recursive calls end, otherwise the recursion continues until a stack overflow error occurs. 



abstract example:
```python
def recurse(n):
    if (n >= 1):                                # This is the base case.
        print("Base Case Executed...")
        return

    print(f"Recursive Call: {n}")
    return recurse(n - 1)

recurse(5) 
# Output:
# Recursive Call: n = 5    
# Recursive Call: n = 4    
# Recursive Call: n = 3    
# Recursive Call: n = 2    
# Base Case Executed: n = 1
```

<br>

[Back to Top](#python-recursion)

___

<br>

# `RecursionError: maximum recursion depth exceeded`
`RecursionError: maximum recursion depth execeeded` is a type of error that  typically occurs when a recursive function is called indefinitely or simply when the number of recursive calls is too large.
* This error is often the result of a non-existant base case or a base case that is never met.

<br>

*When a recursive call occurs, the state of the function is held in memory as a new call occurs. This means that each time a function calls itself, a new stack frame is created on the call stack to store the state of that function call.* 

*This stack frame includes information such as:*
* *The function’s return address (where the program should return after the function call completes).*
* *The parameters passed to the function.*
* *The local variables of the function.*  

*As each recursive call adds a new frame to the stack, the memory allocated for the stack increases. If the recursion is too deep (i.e., the function calls itself too many times without reaching a base case), the call stack will eventually exceed the memory limit allocated to it. This is because each function call requires additional stack space, and the operating system limits the size of the stack to prevent programs from using too much memory.*

<br>

abstract example:
```python
def recurse(n):

    print(f"Recursive Call: {n}")
    return recurse(n - 1)

recurse(5) 
# Output:
# Recursive Call: n = 5    
# Recursive Call: n = 4    
# Recursive Call: n = 3    
# Recursive Call: n = 2    
# Recursive Call: n = 1
# ...
# Recursive Call: n = -993
# Traceback (most recent call last):
#   File "<filepath>", line 9, in <module>
#     recurse(5)
#     ^^^^^^^^^^
#   File "<filepath>", line 7, in recurse
#     return recurse(n - 1)
#            ^^^^^^^^^^^^^^
#   File "<filepath>", line 7, in recurse
#     return recurse(n - 1)
#            ^^^^^^^^^^^^^^
#   File "<filepath>", line 7, in recurse
#     return recurse(n - 1)
#            ^^^^^^^^^^^^^^
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
```

<br>

[Back to Top](#python-recursion)

___

<br>

# `Common Recursive Algorithms`

## `Factorial Calculation ` 
The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n. 
* This is the most common example used when teaching Recursion as the algorithm is simple to understand.

Example `5! --> 5 * 4 * 3 * 2 * 1 == 125`

```python
def factorial(n):
    if n <= 0:      # base case
        return 1
    
    return n * factorial(n-1) # recursive calleeeee


factorial(5) # Returns 125
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Fibonacci Sequence ` 
A Fibonacci sequence is a series of numbers in which each number (Fibonacci number) is the sum of the two preceding ones, usually starting with 0 and 1.

```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Binary Search `
Binary search is an algorithm that works by repeatedly dividing the search interval in half, thereby reducing the search space exponentially with each iteration or recursion.
* It only works on sorted collections.

Steps to Binary Search:
* Check if the target value is equal to the middle element, if it is return that index
* If the target is less, the front half of the array is searched
* If the target is greater, the back half of the array is searched
* This process is repeated until the target is found, or the search has been exhausted

Properties:
* Time Complexity: O(log n) where n is the number of elements in the list
* Space Complexity: O(log n) for recursive implementation
* Requirement: The array must be sorted

```python
def binary_search(arr, target, low, high):
    if low > high:
        return -1               # Base case: target not found

    mid = (low + high) // 2     # Find the middle index

    if arr[mid] == target:      # Target found
        return mid
    elif arr[mid] < target:     # Target is in the right half
        return binary_search(arr, target, mid + 1, high)
    else:                       # Target is in the left half
        return binary_search(arr, target, low, mid - 1)



arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target, 0, len(arr) - 1)
print(result)  # Output: 3
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Merge Sort ` 
Merge Sort works by recursively dividing the array into two halves, sorting each half, and then merging the sorted halves to produce the sorted array.

Steps of Merge Sort
* Divide the unsorted array into two approximately equal halves.
* Recursively sort each half.
* Merge the two sorted halves to produce a single sorted array.

Properties
* Time Complexity: O(n log n) for all cases
* Space Complexity: O(n) due to the use of auxiliary space for merging

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2         # Find the middle of the array
        left_half = arr[:mid]       # Divide the array elements into two halves
        right_half = arr[mid:]

        merge_sort(left_half)       # Recursively sort the first half
        merge_sort(right_half)      # Recursively sort the second half

        i = j = k = 0

        # Merge the two halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
```

<br>

[Back to Top](#python-recursion)

___

<br>


## `Quick Sort `
`Quick Sort` works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The process is then recursively applied to the sub-arrays.

Steps for Quick Sort:
1. Choose a Pivot: Select an element from the array to act as the pivot.
2. Partition: Reorder the array so that all elements less than the pivot come before it, and all elements greater than the pivot come after it.
3. Recursively Apply: Apply Quick Sort recursively to the sub-arrays formed by the pivot.
4. Base Case: The recursion terminates when the sub-array has one or zero elements, which are already sorted.

Properties:
* Average Time Complexity: O(n log n) --> worst case O(n^2)
* Average Space Complexity: O(log n) --> worst case O(n)

```python
def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)              # Partitioning index
        quick_sort_in_place(arr, low, pi - 1)       # Recursively sort the left part
        quick_sort_in_place(arr, pi + 1, high)      # Recursively sort the right part

def partition(arr, low, high):
    pivot = arr[high]                               # Choose the last element as the pivot
    i = low - 1                                     # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]         # Swap if element is less than pivot
    arr[i + 1], arr[high] = arr[high], arr[i + 1]   # Place pivot in correct position
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort_in_place(arr, 0, len(arr) - 1)
print(arr)                                          # Output: [1, 5, 7, 8, 9, 10]
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Permutations ` 
A `permutation` of a set is a specific arrangement or ordering of its elements.

The number of permutations of n distinct items is given by n! (n factorial)
```
n!
```
The number of permutations of n items with only r items selected and arranged is: 

    P(n,r) = n! / (n-r)!

```python
def permutations(arr):
    if len(arr) == 0:   
        return [[]]
    
    result = []
    for i in range(len(arr)):
        current = arr[i]
        remaining = arr[:i] + arr[i+1:]
        for p in permutations(remaining):
            result.append([current] + p)
    
    return result


arr = [1, 2, 3]
print(permutations(arr))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Combinations ` 
A `combination` is a way of selecting items from a larger set without regard to the order of the items.

The number of combinations of n items taken r at a time is give by:
```
C(n,r) = n! / (r!(n-r)!)
```

```python
def combinations(arr, r):
    if r == 0:
        return [[]]
    if len(arr) == 0:
        return []
    
    # Include the first element and find combinations of the remaining elements
    with_first = combinations(arr[1:], r - 1)
    with_first = [[arr[0]] + combo for combo in with_first]
    
    # Exclude the first element and find combinations of the remaining elements
    without_first = combinations(arr[1:], r)
    
    return with_first + without_first


arr = [1, 2, 3]
print(combinations(arr, 2))  # Output: [[1, 2], [1, 3], [2, 3]]
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Depth-First Search` 
`Depth-First Search (DFS)` is a fundamental graph traversal algorithm used to explore nodes and edges of a graph. It starts from a given node and explores as far down a branch as possible before backtracking. 

Steps of DFS:
* Start at the Root: Begin traversal from a starting node (or root node).
* Explore Neighbors: Visit an unvisited neighbor, mark it as visited, and push it onto the stack (or call it recursively).
* Backtrack: When no unvisited neighbors are available, backtrack to the previous node and continue exploration.
* Repeat: Continue this process until all nodes have been visited.

```python
def dfs_recursive(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
visited = set()
dfs_recursive(graph, 'A', visited)
```

<br>

[Back to Top](#python-recursion)

___

<br>

## `Breadth-First Search` 
`Breadth-First Search (BFS)` is a fundamental graph traversal algorithm used to explore nodes and edges of a graph. Unlike Depth-First Search (DFS), which explores as far down a branch as possible, BFS explores all nodes at the present depth level before moving on to nodes at the next depth level.


Steps of BFS
* Initialize: Start by initializing a queue with the starting node and marking it as visited.
* Explore Neighbors: Dequeue a node from the front of the queue, visit it, and enqueue all its unvisited neighbors.
* Repeat: Continue the process until the queue is empty, meaning all reachable nodes have been explored.


```python
from collections import deque

def bfs_recursive(graph, queue, visited):
    if not queue:
        return

    node = queue.popleft()
    if node not in visited:
        print(node)
        visited.add(node)
        
        # Add unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    # Recursive call with the updated queue
    bfs_recursive(graph, queue, visited)

def bfs(graph, start):
    queue = deque([start])
    visited = set()
    bfs_recursive(graph, queue, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}
bfs(graph, 'A')
```

<br>

[Back to Top](#python-recursion)

___

<br>

*Created and maintained by Mr. Merritt*










