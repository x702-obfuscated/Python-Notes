# `Insertion`   
`Insertion sort` is a simple sorting algorithm that builds a sorted array one element at a time by repeatedly taking an element from the unsorted portion and inserting it into its correct position within the sorted portion. The algorithm starts by assuming that the first element is already sorted, then moves the next element into the sorted part by comparing it with previous elements and shifting them to the right until it finds the correct position for the new element. This process is repeated for each element in the list.

Insertion sort has a time complexity of O(n²) in the worst case but performs efficiently on small or nearly sorted datasets, with a best-case time complexity of O(n) when the array is already sorted. The algorithm is stable (preserves the relative order of equal elements) and works in-place, meaning it requires only a constant amount of extra memory.



1. `Start with the Second Element`: Assume the first element of the list is already sorted. Begin the process from the second element.
1. `Pick the Next Element`: Select the element at the current position (let’s call it the “key”) and prepare to insert it into the sorted portion of the list.
1. `Compare with Sorted Elements`: Compare the key with the elements before it (i.e., the sorted portion of the list).
1. `Shift Elements`: If the key is smaller than the element being compared, shift that element one position to the right to make space for the key.
1. `Insert the Key`: Continue shifting elements until you find the correct position for the key. Insert the key into that position.
1. `Repeat`: Move to the next unsorted element and repeat steps 2 through 5 until all elements are sorted.
1. `End of Algorithm`: When you reach the last element of the list, and it has been inserted into the sorted portion, the list is fully sorted.



```python
def iterative_insertion_sort(arr):
    # Traverse from the second element to the last
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted into the sorted portion
        j = i - 1

        # Move elements of the sorted portion that are greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key in the correct position
        arr[j + 1] = key

# Example usage
arr = [12, 11, 13, 5, 6]
iterative_insertion_sort(arr)
print("Sorted array:", arr)
```
```python
def recursive_insertion_sort(arr, n):
    # Base case: If the array contains only one element, it's already sorted
    if n <= 1:
        return

    # Sort the first n-1 elements recursively
    recursive_insertion_sort(arr, n - 1)

    # Insert the nth element into its correct position in the sorted portion
    last = arr[n - 1]
    j = n - 2

    # Move elements of arr[0..n-1], that are greater than last, to one position ahead
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    # Insert the last element in the correct position
    arr[j + 1] = last

# Example usage
arr_recursive = [12, 11, 13, 5, 6]
recursive_insertion_sort(arr_recursive, len(arr_recursive))
print("Sorted array (recursive):", arr_recursive)
```