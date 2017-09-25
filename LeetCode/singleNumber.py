# 136
# Given an array of integers, every element appears twice except for one. Find that single one.
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for num in nums:
        result ^= num
    return result

nums = [1,1,2,3,2,3,5,4,5]

print(singleNumber(nums))