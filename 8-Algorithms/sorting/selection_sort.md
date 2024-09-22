# `Selection Sort`

`Selection sort` is a straightforward sorting algorithm that organizes a list or array by repeatedly selecting the smallest (or largest, depending on the order) element from an unsorted portion and moving it to the beginning of the list. The algorithm works by dividing the input into two parts: a sorted section at the front and an unsorted section at the back. It begins by searching the entire unsorted section to find the smallest element, then swaps it with the first unsorted element, effectively growing the sorted section by one. This process is repeated, with the algorithm selecting the next smallest element from the remaining unsorted portion until the entire list is sorted. Selection sort has a time complexity of O(n²), making it inefficient for large datasets, but it is simple to implement and understand, making it useful for educational purposes and small datasets.

1. `Initialize:` Start with an unsorted list and divide it conceptually into a sorted and unsorted portion. Initially, the sorted portion is empty, and the unsorted portion is the entire list.
1. `Outer Loop`: Begin a loop that iterates over the entire list, starting from the first element.
1. `Find Minimum Element`: For each position in the unsorted portion of the list, find the smallest element by comparing it with every other element in the unsorted portion.
1. `Swap Elements`: Once the smallest element is found, swap it with the first unsorted element in the list, effectively placing it in its correct position in the sorted portion.
1. `Expand Sorted Portion`: The sorted portion now grows by one element, and the unsorted portion shrinks.
1. `Repeat:` Move to the next position in the list and repeat steps 3-5, continuing the process for the rest of the unsorted elements.
1. `Continue Until Sorted`: The process continues until the entire list is sorted, with the sorted portion eventually growing to encompass the entire list.
1. `End`: The algorithm finishes when every element has been placed in its correct position, and the list is completely sorted.

```python
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
```