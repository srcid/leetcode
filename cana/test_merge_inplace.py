from merge import merge_inplace


def test_merge_inplace_basic_sorted():
    A = [1, 3, 5, 2, 4, 6]
    merge_inplace(A, 0, 3, 6)
    assert A == [1, 2, 3, 4, 5, 6]


def test_merge_inplace_with_overlap():
    A = [1, 4, 6, 2, 3, 5]
    merge_inplace(A, 0, 3, 6)
    assert A == [1, 2, 3, 4, 5, 6]


def test_merge_inplace_single_element_sublists():
    A = [1, 2]
    merge_inplace(A, 0, 1, 2)
    assert A == [1, 2]


def test_merge_inplace_identical_elements():
    A = [1, 1, 2, 2]
    merge_inplace(A, 0, 2, 4)
    assert A == [1, 1, 2, 2]


def test_merge_inplace_with_negatives():
    A = [-3, -1, 0, -2, 2, 4]
    merge_inplace(A, 0, 3, 6)
    assert A == [-3, -2, -1, 0, 2, 4]


def test_merge_inplace_empty_left():
    A = [1, 2, 3]
    merge_inplace(A, 0, 0, 3)
    assert A == [1, 2, 3]


def test_merge_inplace_empty_right():
    A = [1, 2, 3]
    merge_inplace(A, 0, 3, 3)
    assert A == [1, 2, 3]


def test_merge_inplace_internal_segment():
    A = [9, 1, 3, 5, 2, 4, 6, 0]
    merge_inplace(A, 1, 4, 7)  # Merge [1,3,5] and [2,4,6]
    assert A == [9, 1, 2, 3, 4, 5, 6, 0]
    assert A[1:7] == sorted(A[1:7])
