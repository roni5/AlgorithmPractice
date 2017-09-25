# 1

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    seen = {}
    output = []

    for idx, number in enumerate(nums):
        goal = target - number
        if goal not in seen:
            seen[number] = idx
        else:
            output.append(seen[goal])
            output.append(idx)
    return output
