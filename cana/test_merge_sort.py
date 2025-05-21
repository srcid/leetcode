import pytest

from merge import merge_sort


def test_empty_list():
    A = []
    merge_sort(A, 0, 0)
    assert A == []


def test_single_element():
    A = [42]
    merge_sort(A, 0, 1)
    assert A == [42]


def test_two_elements_sorted():
    A = [1, 2]
    merge_sort(A, 0, 2)
    assert A == [1, 2]


def test_two_elements_unsorted():
    A = [2, 1]
    merge_sort(A, 0, 2)
    assert A == [1, 2]


def test_multiple_elements():
    A = [5, 2, 9, 1, 5, 6]
    merge_sort(A, 0, len(A))
    assert A == [1, 2, 5, 5, 6, 9]


def test_negative_numbers():
    A = [0, -1, -3, 8, 7]
    merge_sort(A, 0, len(A))
    assert A == [-3, -1, 0, 7, 8]


def test_all_duplicates():
    A = [4, 4, 4, 4]
    merge_sort(A, 0, len(A))
    assert A == [4, 4, 4, 4]


def test_partial_range():
    A = [9, 3, 7, 5, 6]
    merge_sort(A, 1, 4)  # Sorts A[1:4] -> [3, 7, 5]
    assert A[:1] == [9]
    assert A[1:4] == sorted([3, 7, 5])
    assert A[4:] == [6]


def test_empty_range():
    A = [3, 1, 2]
    merge_sort(A, 2, 2)  # No-op
    assert A == [3, 1, 2]

def test_invalid_range_with_negative_index():
    A = [3, 1, 2]
    
    with pytest.raises(IndexError):
        merge_sort(A, -1, 2)

def test_invalid_range_with_i_bigger_than_j():
    A = [3, 1, 2, 5, 6]
    
    with pytest.raises(IndexError):
        merge_sort(A, 3, 2)
