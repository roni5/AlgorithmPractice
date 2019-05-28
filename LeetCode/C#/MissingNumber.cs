public class Solution {
    public int MissingNumber(int[] nums) {
        var mySet = new HashSet<int>();
        
        foreach(var num in nums) {
            mySet.Add(num);
        }
        
        for(int i = 0; i < nums.Length + 1; i++) {
            if(!mySet.Contains(i)){
                return i;
            }
        }
        
        return -1;
    }
}