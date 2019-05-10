# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
def missingNumber(self, nums: List[int]) -> int:
    num_limit = len(nums) + 1
    num_set = set(nums)

    for i in range(num_limit):
        if i not in num_set:
            return i
    raise ValueError("There is no answer")