public class Solution {
    public int MaxSubArray(int[] nums) {
        
        if(nums.Length == 0) return 0;
        
        int currentSum = nums[0];
        int maxSum = nums[0];

        for(int i = 1; i < nums.Length; i++)
        {
            currentSum = Math.Max(currentSum + nums[i], nums[i]);
            maxSum = Math.Max(maxSum, currentSum);
        }

        return maxSum;
    }
}