namespace LeetCode.CSharp.SecondRound
{
    public class FindMinimumInRotatedArray
    {
        public int FindMin(int[] nums)
        {
            int left = 0;
            int right = nums.Length - 1;

            while (left < right)
            {
                int mid = (left + right) / 2;
                if (nums[mid] > nums[right])
                    left = mid + 1;
                else
                    right = mid;
            }

            return nums[left];
        }
    }
}