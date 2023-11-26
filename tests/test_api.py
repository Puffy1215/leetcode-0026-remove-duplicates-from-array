"""Tests API for solving problem Remove Duplicates from Sorted Array"""

import pytest

from leetcode_0026_remove_duplicates_from_sorted_array import api


@pytest.mark.parametrize(
    ["result", "nums"],
    (
        [(2, [1, 2]), [1, 1, 2]],
        [(5, [0, 1, 2, 3, 4]), [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]],
        [(1, [1]), [1]],
        [(1, [1]), [1, 1, 1, 1, 1]],
    ),
)
def test_remove_duplicates_from_sorted_array(
    result: tuple[int, list[int]], nums: list[int]
) -> None:
    """Tests solution for problem Remove Duplicates from Sorted Array"""

    k = api.remove_duplicates_from_sorted_array(nums)

    assert (k, nums[:k]) == result
