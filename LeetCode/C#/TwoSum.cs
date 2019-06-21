public class Solution {
    public int[] TwoSum(int[] nums, int target) 
    {
        var dict = new Dictionary<int, int>();

        for(int i = 0; i < nums.Length; i++)
        {
            int lookFor = target - nums[i];
            if(dict.ContainsKey(lookFor)) return new int[] {dict[lookFor], i};
            else dict[nums[i]] = i;
        }

        return new int[]{0,0};
    }

    public static void Main(string[] args) 
    {
        var nums = new int[] {1,2,3,4};
        
        int target = 5;
        
        var answer = TwoSum(nums, target);
        foreach(var item in answer)
        {
            Console.WriteLine(item);
        }
    }
}