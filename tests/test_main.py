import pytest
from subset_sum import subset_sum

@pytest.mark.parametrize("numbers, target, expected", [
    ([3, 34, 4, 12, 5, 2], 9, True),
    ([1, 2, 3, 4, 5], 10, True),
    ([1, 2, 3, 4, 5], 11, False),
    ([1, 1, 1, 1, 1], 5, True),
    ([1, 1, 1, 1, 1], 6, False),
    ([], 5, False),
    ([5], 5, True),
    ([5], 10, False),
])
def test_subset_sum(numbers, target, expected):
    assert subset_sum(numbers, target) == expected
