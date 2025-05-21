import pytest
from inversion_count import inversion_count, inversion_count_naive


@pytest.mark.parametrize(
    "arr",
    [
        [],  # Empty array
        [1],  # Single element
        [1, 2],  # Sorted array
        [2, 1],  # One inversion
        [1, 3, 2],  # One inversion (3,2)
        [2, 4, 1, 3, 5],  # Multiple inversions
        [5, 4, 3, 2, 1],  # Maximum inversions
        [1, 2, 3, 4, 5],  # No inversions
        [3, 1, 2],  # (3,1) and (3,2)
        [8, 4, 2, 1],  # All inversions
        [1, 3, 5, 2, 4, 6],
        [1, 5, 7, 8, 2],
    ],
)
def test_count_inversions(arr):
    expected = inversion_count_naive(arr)
    assert inversion_count(arr) == expected
