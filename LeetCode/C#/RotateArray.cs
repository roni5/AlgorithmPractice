public class Solution {
    public void Rotate(int[] nums, int k) {
        k = k % nums.Length;
        Reverse(nums, 0, nums.Length - 1);
        Reverse(nums, 0, k - 1);
        Reverse(nums, k, nums.Length - 1);
    }
    
    public void Reverse(int[] nums, int start, int end)
    {
        while(start < end)
        {
            int temp = nums[end];
            nums[end] = nums[start];
            nums[start] = temp;
            start += 1;
            end -= 1;
        }
    }
}