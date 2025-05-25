def merge_inplace(A, i, k, j):
    p, q = i, k

    while p < q and q < j:
        if A[p] < A[q]:
            p += 1
        else:
            # tmp = A[q]
            # for m in range(q, p, -1):
            #     A[m] = A[m - 1]
            # A[p] = tmp
            A[p : q + 1] = [A[q], *A[p:q]]
            q += 1


def merge(A, i, k, j):
    p, q = i, k
    a = []

    while p < k and q < j:
        if A[p] < A[q]:
            a.append(A[p])
            p += 1
        else:
            a.append(A[q])
            q += 1

    if p == k:  # left sub array is empty
        a.extend(A[q:j])
    else:  # q == j, right sub array is empty
        a.extend(A[p:k])

    A[i:j] = a


def merge_sort(A, i, j):
    if i < 0 or j < 0 or (j - i) < 0:  # Invalid range
        raise IndexError("Invalid range")

    if (j - i) == 0:  # Empty array
        return

    if (j - i) == 1:  # Single element array
        return

    k = i + (j - i) // 2

    merge_sort(A, i, k)
    merge_sort(A, k, j)

    merge(A, i, k, j)
