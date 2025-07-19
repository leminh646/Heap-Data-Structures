def max_heapify(A, i, heap_size):
    """
    Ensure the subtree rooted at index i obeys the max-heap property,
    assuming the subtrees rooted at its children already do.
    """
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < heap_size and A[l] > A[largest]:
        largest = l
    if r < heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    """
    Convert an unordered array A into a max-heap in-place.
    """
    n = len(A)
    # Start from the last non-leaf node and heapify each one
    for i in range(n//2 - 1, -1, -1):
        max_heapify(A, i, n)

def heapsort(A):
    """
    Perform in-place Heapsort on array A and return it sorted in ascending order.
    """
    n = len(A)
    build_max_heap(A)
    # Repeatedly extract the maximum element (at index 0)
    for i in range(n - 1, 0, -1):
        # Move current max to the end
        A[0], A[i] = A[i], A[0]
        # Restore max-heap property on the reduced heap
        max_heapify(A, 0, i)
    return A

# Example usage
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("Original array:", arr)
    sorted_arr = heapsort(arr.copy())
    print("Sorted array:  ", sorted_arr)
