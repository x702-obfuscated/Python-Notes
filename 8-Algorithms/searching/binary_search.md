# `Binary Search`

`Binary search` is an efficient algorithm used to find the position of a target value within a sorted array or list. It works by repeatedly dividing the search interval in half. The algorithm begins by comparing the target value to the middle element of the list. If the target is equal to the middle element, its position is returned. If the target is less than the middle element, the search continues in the lower half of the array; if greater, it continues in the upper half. This process is repeated until the target is found or the search interval is empty. Binary search has a time complexity of O(log n), making it significantly faster than linear search for large datasets, provided that the data is sorted beforehand.

1. `Precondition`: Ensure that the list is sorted in ascending order before starting the search.
1. `Initialize Variables`: Set two variables, low to 0 (the start of the list) and high to the last index of the list (length of the list minus one).
1. `Begin Loop`: Start a loop that continues as long as low is less than or equal to high.
1. `Calculate Middle Index`: Calculate the middle index using the formula mid = (low + high) // 2.
1. `Compare Middle Element`: Check if the element at the middle index matches the target value. If it does, proceed to step 6. If not, proceed to step 7 or step 8.
1. `Return Index`: If a match is found, return the middle index as the position of the target value in the list.
1. `Adjust Search Range`:
    * If the target value is less than the middle element, adjust the search range by setting high to mid - 1.
    * If the target value is greater than the middle element, adjust the search range by setting low to mid + 1.
1. `Repeat`: Repeat steps 4 through 7 until the target is found or the search range is invalid (low exceeds high).
1. `Check End of Search`: If the search range becomes invalid and the target has not been found, return a value indicating that the target is not present (commonly -1).
1. `End of Algorithm`: The algorithm concludes when either the target is found (and the index is returned) or when all possible search ranges have been checked without a match.

```python
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Return -1 if the target is not found
```
```python
def recursive_binary_search(arr, target, low, high):
    # Base case: If the range is invalid, the target is not found
    if low > high:
        return -1

    # Find the middle index
    mid = (low + high) // 2

    # Check if the target is at the middle
    if arr[mid] == target:
        return mid
    # If target is smaller than middle, search in the left half
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    # If target is larger than middle, search in the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = recursive_binary_search(arr, target, 0, len(arr) - 1)
if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found")