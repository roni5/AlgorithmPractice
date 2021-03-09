namespace LeetCode.CSharp.SecondRound
{
    public class JumpGame
    {
        public bool CanJump(int[] nums)
        {
            int maxIndex = 0;
            int n = nums.Length;

            for (int i = 0; i < n; i++)
            {
                if (i > maxIndex)
                    return false;
                else
                    maxIndex = Math.Max(maxIndex, i + nums[i]);
            }

            return maxIndex >= n - 1;
        }
    }
}