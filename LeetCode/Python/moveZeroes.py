# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

  def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_idx = 0

        for idx, num in enumerate(nums):
            if num != 0:
                temp = nums[zero_idx]
                nums[zero_idx] = num
                nums[idx] = temp
                zero_idx += 1
        