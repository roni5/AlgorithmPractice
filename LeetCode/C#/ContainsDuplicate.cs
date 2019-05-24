public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var hs = new HashSet<int>();
        
        foreach(var num in nums){
            if(hs.Contains(num)) return true;
            else hs.Add(num);
        }
        
        return false;
    }
}