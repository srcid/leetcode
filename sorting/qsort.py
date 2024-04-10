from rich import print
from random import seed, randint
from queue import Queue
from collections import Counter

def partition(arr, start, end):
    pivot_idx = start
    pivot = arr[start]

    for i in range(start+1, end):
        if arr[i] <= pivot:
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]

    arr[pivot_idx], arr[start] = arr[start], arr[pivot_idx]

    return pivot_idx


def qsort(arr, start, end):
    if end - start >= 2:
        mid = partition(arr, start, end)

        qsort(arr, start, mid)
        qsort(arr, mid + 1, end)


def iqsort(arr):
    q = Queue()
    q.put((0, len(arr)))

    while not q.empty():
        start, end = q.get()

        if end - start >= 2:
            mid = partition(arr, start, end)
            q.put((start, mid))
            q.put((mid + 1, end))


seed(42)

arr = [randint(-19, 20) for _ in range(20)]
arr_cp = arr.copy()
pfilter = [*filter(lambda n: n <= arr_cp[0], arr_cp[1:]), arr_cp[0], *filter(lambda n: n > arr_cp[0], arr_cp[1:])]
p_idx = partition(arr_cp, 0, len(arr_cp))
comp = (
    pfilter[p_idx] == arr_cp[p_idx]
    and Counter(pfilter[:p_idx]) == Counter(arr_cp[:p_idx])
    and Counter(pfilter[p_idx+1:]) == Counter(arr_cp[p_idx+1:])
)

print('Partition algorithm')
print(f'{'initial:':12} {arr}')
print(f'{'pivot_idx:':12} {p_idx}')
print(f'{'partitioned:':12} {arr_cp}')
print(f'{'pfilter:':12} {pfilter}')
print(f'{'comp:':12} {comp}')

print('QSort algorithm')

arr = [randint(-1000, 1000) for _ in range(100_000)]
arr_cp = arr.copy()

qsort(arr_cp, 0, len(arr_cp))
print(f'{'qsort:':12} {arr_cp == sorted(arr)}')

arr_cp = arr
iqsort(arr_cp)
print(f'{'iqsort:':12} {arr_cp == sorted(arr)}')
