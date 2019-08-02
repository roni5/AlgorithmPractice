class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False for x in range(len(nums))]
        dp[0] = True

        for j in range(1, len(nums)):
            for i in range(0, j):
                if dp[i] and i + nums[i] >= j:
                    dp[j] = True
                    break
        return dp[len(dp) - 1]