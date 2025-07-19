def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])
    return merge(left, right)