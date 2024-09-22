# `Quick Sort`

`Quick sort` is a highly efficient sorting algorithm that employs the divide-and-conquer strategy to sort elements. It works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays: those less than the pivot and those greater than the pivot. The process is recursively applied to the sub-arrays.


1. `Start with an Unsorted List`: Begin with an array or list that needs to be sorted.

2. `Choose a Pivot`: Select an element from the list as the pivot. This can be the first element, the last element, a random element, or the median.

3. `Partition the List`:
   - Create two sub-arrays: one for elements less than the pivot and one for elements greater than the pivot.
   - Traverse the list, comparing each element with the pivot and placing it in the appropriate sub-array.

4. `Recursively Sort the Sub-arrays`:
   - Apply the quick sort algorithm recursively to the left sub-array (elements less than the pivot).
   - Apply the quick sort algorithm recursively to the right sub-array (elements greater than the pivot).

5. `Combine`: Since the sub-arrays are sorted in place, no explicit merging is needed. The original list will be sorted when the recursive calls complete.

6. `End of Algorithm`: The algorithm finishes when all sub-arrays contain one or zero elements, indicating that the entire list is sorted.


```python
def quick_sort(arr):
    # Base case: if the array has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (here, we choose the last element)
    pivot = arr[-1]
    left = []
    right = []

    # Partition the array into two sub-arrays
    for element in arr[:-1]:  # Exclude the pivot
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)

    # Recursively sort the left and right sub-arrays, and combine
    return quick_sort(left) + [pivot] + quick_sort(right)


arr_recursive = [38, 27, 43, 3, 9, 82, 10]
sorted_array = quick_sort(arr_recursive)
print("Sorted array (recursive):", sorted_array)
```