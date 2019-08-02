class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = [1 for x in range(len(nums))]
        maxLen = 1

        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[i] + 1, dp[j])

            maxLen = max(maxLen, dp[j])
        
        return maxLen