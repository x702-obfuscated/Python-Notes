# `Bubble sort`

`Bubble sort` is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated multiple times, and with each pass, the largest unsorted element "bubbles" up to its correct position at the end of the list. The algorithm continues until no more swaps are needed, indicating that the list is sorted.

While easy to understand and implement, bubble sort is inefficient for large datasets due to its average and worst-case time complexity of O(n²). It is primarily used for educational purposes rather than practical applications.

1. `Initialize Variables`: Start with an unsorted list.
2. `Outer Loop`: Begin a loop that iterates over the list multiple times.
3. `Inner Loop`: During each pass, compare each pair of adjacent elements in the list (starting from the first element and moving toward the end).
4. `Compare Adjacent Elements`: For each pair of adjacent elements, if the left element is greater than the right element, swap them.
5. `Repeat`: After completing one full pass through the list, the largest unsorted element will be placed at the end of the list.
6. `Shrink Search Area`: For each subsequent pass, exclude the last sorted elements since they are already in their correct positions.
7. `Continue Until No Swaps`: Repeat the process until a complete pass is made without any swaps, indicating that the list is fully sorted.
8. `End of Algorithm`: The algorithm finishes when no more swaps are needed and all elements are in their correct positions.

```python
def iterative_bubble_sort(arr):
    n = len(arr)
    # Outer loop: Traverse the array
    for i in range(n):
        swapped = False
        # Inner loop: Compare adjacent elements
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no elements were swapped, the array is sorted
        if not swapped:
            break

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
iterative_bubble_sort(arr)
print("Sorted array:", arr)
```
```python
def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)
    # Base case: If the array has one or no elements, it's already sorted
    if n == 1:
        return

    # One pass of bubble sort: after this pass, the largest element is at the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call to bubble sort the first n-1 elements
    bubble_sort_recursive(arr, n - 1)

# Example usage
arr_recursive = [64, 34, 25, 12, 22, 11, 90]
recursive_bubble_sort(arr_recursive)
print("Sorted array (recursive):", arr_recursive)
```