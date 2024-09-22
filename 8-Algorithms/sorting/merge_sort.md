# `Merge Sort`

`Merge sort` is a divide-and-conquer sorting algorithm that recursively splits an unsorted list into smaller sublists until each sublist contains a single element (which is inherently sorted). It then merges these sublists back together in a sorted manner to produce the final sorted list.

1. `Start with an Unsorted List`: Begin with an array or list that needs to be sorted.

2. `Check Base Case`: If the list has one or zero elements, it is already sorted. Return the list.

3. `Divide the List`: 
   - Find the middle index of the list.
   - Split the list into two halves: the left half and the right half.

4. `Recursively Sort Each Half`: 
   - Call the merge sort function on the left half.
   - Call the merge sort function on the right half.

5. `Merge the Sorted Halves`: 
   - Create a temporary list to hold the merged elements.
   - Use two pointers to track the current index of each half.
   - Compare the elements pointed to by the pointers and append the smaller element to the temporary list.
   - Move the pointer of the half from which the element was taken.

6. `Append Remaining Elements`: If there are any remaining elements in either half after one half is exhausted, append them to the temporary list.

7. `Copy Back to Original List`: Replace the elements in the original list with those from the temporary list.

8. `End of Algorithm`: The original list is now sorted.

```python
def iterative_merge_sort(arr):
    n = len(arr)
    # Create a temporary list to hold the sorted elements
    temp = [0] * n

    # Width of the sublists
    width = 1

    while width < n:
        # Merge sublists in pairs
        for i in range(0, n, 2 * width):
            left = i
            mid = min(i + width, n)
            right = min(i + 2 * width, n)

            # Merge the two halves
            merge(arr, temp, left, mid, right)

        # Copy the sorted elements back to the original array
        arr[:] = temp[:]
        width *= 2

def merge(arr, temp, left, mid, right):
    i = left     # Starting index for left sublist
    j = mid      # Starting index for right sublist
    k = left     # Starting index for merged sublist

    while i < mid and j < right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i < mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j < right:
        temp[k] = arr[j]
        j += 1
        k += 1

# Example usage of iterative merge sort
arr_iterative = [38, 27, 43, 3, 9, 82, 10]
iterative_merge_sort(arr_iterative)
print("Sorted array (iterative):", arr_iterative)
```
```python
def recursive_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]

        # Recursive call on the left half
        recursive_merge_sort(left_half)

        # Recursive call on the right half
        recursive_merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    # Merging the two halves
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example usage of recursive merge sort
arr_recursive = [38, 27, 43, 3, 9, 82, 10]
recursive_merge_sort(arr_recursive)
print("Sorted array (recursive):", arr_recursive)
```