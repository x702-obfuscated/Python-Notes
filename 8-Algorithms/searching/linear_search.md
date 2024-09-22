# `Linear Search`
`Linear search` is a straightforward algorithm used to find a target value within a list or array by examining each element sequentially. 

Starting from the first element, the algorithm checks if it matches the target; if not, it moves to the next element and continues this process until either the target is found or the end of the list is reached. This method is simple to implement and understand, making it suitable for small or unsorted datasets. However, linear search is inefficient for large collections, as its average and worst-case time complexity is O(n), meaning the time taken grows linearly with the number of elements. Despite its limitations, linear search can be useful in scenarios where the dataset is small or where data is unsorted and a quick solution is needed without the overhead of more complex algorithms.

1. `Initialize Variables`: Set the target value you want to find and start with the first index of the list (typically index = 0).

1. `Begin Loop`: Start a loop that continues as long as the current index is less than the length of the list.

1. `Compare Current Element`: Check if the element at the current index matches the target value. If it does, proceed to step 4. If not, proceed to step 5.

1. `Return Index`: If a match is found, return the current index as the position of the target value in the list.

1. `Increment Index`: Increase the current index by 1 to move to the next element in the list.

1. `Repeat`: Repeat steps 3 through 5 until the target is found or the end of the list is reached.

1. `Check End of List`: If the end of the list is reached and the target has not been found, return a value indicating that the target is not present (commonly -1).

1. `End of Algorithm`: The algorithm concludes when either the target is found (and the index is returned) or when all elements have been checked without a match.


```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found
```
