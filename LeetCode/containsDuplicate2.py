# 219
# Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """

    seen = {}

    for i in range(len(nums)):
        if nums[i] not in seen:
            seen[nums[i]] = i
        else:
            if abs(seen[nums[i]] - i) <= k:
                return True
            seen[nums[i]] = i
    return False