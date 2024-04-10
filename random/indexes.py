from typing import Iterable, Union
from itertools import product

def indexes(arr: Iterable) -> Union[tuple[int], tuple[tuple[int]]]:
    """Returns the indexes of elements in a N-th dimensional array

    Args:
        arr (Iterable): N-th dimensional array 

    Returns:
        Union[tuple[int], tuple[tuple[int]]]: tuple of indexes if arr is 1-th dimension, tuple with tuple
        of index otherwise.
    """

    subs = []
    
    while isinstance(arr[0], Iterable):
        subs.append(range(len(arr)))
        arr = arr[0]

    return tuple(product(*subs, range(len(arr)))) if subs else tuple(range(len(arr)))


if __name__ == '__main__':
    arr_1d = [1,3,3]

    arr_2d = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    arr_3d = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ]
]


    print(indexes(arr_1d))
    print(indexes(arr_2d))
    print(indexes(arr_3d))