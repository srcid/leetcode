from numpy.random import randint

def ordered_merge(a, b):
    a_size, b_size = len(a), len(b)
    c_size = a_size + b_size
    c = []

    a_idx, b_idx = 0, 0

    while a_idx < a_size and b_idx < b_size:
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1 
        else:
            c.append(b[b_idx])
            b_idx += 1

    if len(c) < c_size:
        if a_idx == a_size:
            c.extend(b[b_idx:])
        else: # b_idx == b_size
            c.extend(a[a_idx:])

    return c

def merge_sort(arr):
    size = len(arr)
    mid = size // 2

    if size < 2:
        return arr

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    ordered = ordered_merge(left, right)

    return ordered

print(ordered_merge([1,6,9,10], [2,3,7,10]))

arr = randint(-20, 19, size=15)
print(arr)
print(merge_sort(arr))