 def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0 for _ in range(len(nums))]
        right = [0 for _ in range(len(nums))]
        ans = [0 for _ in range(len(nums))]
        left[0] = 1
        right[-1] = 1
        
        for i in range(1, len(left)):
            left[i] = left[i - 1] * nums[i - 1]
        
        for i in range(len(right) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]
        
        return ans