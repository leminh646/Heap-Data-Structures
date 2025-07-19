import sys
sys.setrecursionlimit(10000)

def quicksort(A, l=0, r=None):
    if r is None:
        r = len(A) - 1
    if l < r:
        pivot = A[l]
        i, j = l + 1, r
        while True:
            while i <= j and A[i] <= pivot:
                i += 1
            while i <= j and A[j] >= pivot:
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
            else:
                break
        A[l], A[j] = A[j], A[l]
        quicksort(A, l, j - 1)
        quicksort(A, j + 1, r)