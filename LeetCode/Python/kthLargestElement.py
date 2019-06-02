class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        return self.qucikSelect(nums, start, end, len(nums) - k)
    

    def quickSelect(self, nums, start, end, k):

        if start == end:
            return nums[start]
        
        pivotIdx = start + random.randrange(end - start)
