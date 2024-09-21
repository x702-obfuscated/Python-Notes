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