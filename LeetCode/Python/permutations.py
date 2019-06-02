class Solution:
    def permute(self, nums):
        result = []
        temp = []
        self.backtrack(nums, result, temp)
        print(result)
        return result
    
    def backtrack(self, nums, result, temp):
        
        if len(temp) == len(nums):
            # print(temp)
            result.append(list(temp))
            return
        
        for num in nums:
            if num in temp:
                continue
            
            temp.append(num)
            self.backtrack(nums, result, temp)
            temp.pop()

nums = [1,2,3]
solution = Solution()
solution.permute(nums)
