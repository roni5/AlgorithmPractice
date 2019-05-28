public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        var L = new int[nums.Length];
        var R = new int[nums.Length];
        var answer = new int[nums.Length];
        
        L[0] = 1;
        for(int i = 1; i < nums.Length; i++) {
            L[i] = nums[i - 1] * L [i - 1];
        }
        
        R[nums.Length - 1] = 1;
        for(int i = nums.Length - 2; i >= 0; i--) {
            R[i] = nums[i + 1] * R[i + 1];
        }
        
        for(int i = 0; i < nums.Length; i++){
            answer[i] = L[i] * R[i];
        }
        
        return answer;
        
    }
}