public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        var dict = new Dictionary<int,int>();
        var ans = new List<int>();

        foreach(var num in nums1) {
            if(!dict.ContainsKey(num)) dict.Add(num, 1);
            else dict[num] += 1;
        }

        foreach(var num in nums2) {
            if(dict.ContainsKey(num) && dict[num] > 0){
                ans.Add(num);
                dict[num] -= 1;
            } 
        }

        return ans.ToArray();
    }
}