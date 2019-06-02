import random

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
        
        pivotIdx = start + random.randint(0, end - start)
        pivotIdx = self.partition(nums, start, end, pivotIdx)

        if k == pivotIdx:
            return nums[k]
        elif k < pivotIdx:
            return self.quickSelect(nums, start, pivotIdx - 1)
        else:
            return self.quickSelect(nums, pivotIdx + 1, end)

    
    def partiton(self, nums, start, end, pivotIdx):

        pivotValue = nums[pivotIdx]
        self.swap(nums, pivotIdx, end)

        j = start
        for i in range(start, end):
            if nums[i] < pivotValue:
                self.swap(nums, i, j)
                j += 1
        
        self.swap(nums, j, end)

        return j

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

