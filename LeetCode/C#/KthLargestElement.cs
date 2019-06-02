public class Solution {
    public int FindKthLargest(int[] nums, int k) {
        int start = 0;
        int end = nums.Length - 1;
        return this.QuickSelect(nums, start, end, nums.Length - k);
    }
    
    public int QuickSelect(int[] nums, int start, int end, int kthSmallest) {
        if(start == end) return nums[start];
        
        Random random = new Random();
        int pivotIdx = start + random.Next(end - start);
        
        pivotIdx = this.Partition(nums, start, end, pivotIdx);
        
        if(kthSmallest == pivotIdx) return nums[kthSmallest];
        else if(kthSmallest < pivotIdx) {
            return this.QuickSelect(nums, start, pivotIdx - 1, kthSmallest);
        }else{
            return this.QuickSelect(nums, pivotIdx + 1, end, kthSmallest);
        }
        
    }
    
    public int Partition(int[] nums, int start, int end, int pivotIdx) {
        int pivot = nums[pivotIdx];
        this.Swap(nums, pivotIdx, end);
        
        int j = start;
        for(int i = start; i < end; i++) {
            if(nums[i] <= pivot) {
                this.Swap(nums,j, i);
                j += 1;
            }
        }
        
        this.Swap(nums, j, end);
        
        return j;
    }
    
    public void Swap(int[] nums, int a, int b) {
    int tmp = nums[a];
    nums[a] = nums[b];
    nums[b] = tmp;
  }
    
    
}