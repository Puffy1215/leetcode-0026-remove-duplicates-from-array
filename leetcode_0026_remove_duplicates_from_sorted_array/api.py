"""API for solving problem Remove Duplicates from Sorted Array"""

LEN_MAX = 3 * 10**4
LEN_MIN = 1

NUM_MAX = 100
NUM_MIN = -NUM_MAX


def _check_preconditions(nums: list[int]) -> bool:
    if not LEN_MIN <= len(nums) <= LEN_MAX:
        return False

    if not all(NUM_MIN <= x <= NUM_MAX for x in nums):
        return False

    if not nums == sorted(nums):
        return False

    return True


def remove_duplicates_from_sorted_array(nums: list[int]) -> int:
    """Solves problem Remove Duplicates from Sorted Array"""

    assert _check_preconditions(nums)

    m = len(nums)
    i = 0
    j = 1
    for j in range(1, m):
        if nums[i] == nums[j]:
            continue
        i = i + 1
        nums[i] = nums[j]

    return i
