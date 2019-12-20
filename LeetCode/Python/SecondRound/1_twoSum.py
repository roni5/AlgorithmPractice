# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(self, nums, target):
    dic = dict()
    for idx, num in enumerate(nums):
        lookFor = target - num
        if dic.get(lookFor) is not None:
            return [dic.get(lookFor), idx]
        else:
            dic[lookFor] = idx
    return []