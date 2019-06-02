public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
         
        var answer = new List<IList<int>>();
        int target = 0;
        Array.Sort(nums);
            
        for(int i = 0; i < nums.Length - 2; i++) {
            
            if(i == 0 || nums[i] > nums[i-1]) {
                
                int start = i + 1;
                int end = nums.Length - 1;
                
                while(start < end) {
                    if(nums[i] + nums[start] + nums[end] == target) {
                        var combo = new List<int>() {nums[i], nums[start], nums[end]};
                        answer.Add(combo);
                    }
                    
                    if(nums[i] + nums[start] + nums[end] < target) {
                        int currentStart = start;
                        while(nums[start] == nums[currentStart] && start < end){
                            start += 1;
                        }
                        
                    } else {
                        int currEnd = end;
                        while(nums[end] == nums[currEnd] && start < end) {
                            end -= 1;
                        }
                    }
                }
            }
        }
        
        return answer;
        
    }
}