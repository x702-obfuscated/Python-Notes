# `Heap Sort`

`Heap Sort` is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements. It leverages the properties of heaps to efficiently sort an array in place.


A `heap` is a specialized tree-based data structure that satisfies the heap property. It is commonly used to implement priority queues and sorting algorithms like heap sort. 

The `heap property` is a fundamental characteristic that defines the organization of elements within a heap data structure. 

There are two main types of heaps:

1. Max Heap:
In a max heap, the value of each node is greater than or equal to the values of its children. This ensures that the largest element is always at the root of the tree.
For any given node at index i, its left child is located at index 2i + 1, and its right child is at index 2i + 2.

2. Min Heap:
In a min heap, the value of each node is less than or equal to the values of its children, making the smallest element the root of the tree.
The indexing structure is the same as in a max heap.

Properties of Heaps:
Complete Binary Tree: Heaps are usually implemented as complete binary trees, meaning all levels are fully filled except possibly for the last level, which is filled from left to right.

Dynamic Size: Heaps can grow and shrink dynamically as elements are added or removed.
Efficient Operations: Heaps allow for efficient insertion and deletion operations, typically achieving O(log n) time complexity for both operations.

Common Operations:
Insertion: Add a new element to the heap while maintaining the heap property.
Deletion: Remove the root element (maximum in max heap or minimum in min heap) and then restore the heap property.

Heapify: Adjust the position of a node to maintain the heap property, either from a given node downwards (sifting down) or upwards (sifting up).

Heaps are particularly useful in scenarios where the largest or smallest elements need to be accessed or removed frequently, making them ideal for implementing priority queues and sorting algorithms.

```python
def heap_sort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest element) to the end
        arr[i], arr[0] = arr[0], arr[i]  # swap
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child index
    right = 2 * i + 2  # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
heap_sort(arr)
print("Sorted array:", arr)
```