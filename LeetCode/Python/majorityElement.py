# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        target = len(nums) // 2 + 1
        
        for num in nums:
            if not counter.get(num):
                counter[num] = 1
            else:
                counter[num] += 1
            if counter[num] >= target:
                return num