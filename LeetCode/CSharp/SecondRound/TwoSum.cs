namespace LeetCode.CSharp.SecondRound
{
    public class TwoSum
    {
        public int[] TwoSum(int[] nums, int target)
        {
            Dictionary<int, int> seen = new Dictionary<int, int>();
                
            for(int i = 0; i < nums.Length; i++)
            {
                int lookFor = target - nums[i];

                if (seen.ContainsKey(lookFor)) return new int[] {seen[lookFor], i};
                else seen[nums[i]] = i;
            }

            return null;
        
        }
    }
}