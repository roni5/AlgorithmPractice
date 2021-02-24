class Solution {

    public IList<IList<int>> Permutations (int[] nums) {
        var result = new IList<List<int>>();
        this.Permutations(a, 0, result);
        return result;
    }

    private void Permutations(int[] a, int start, IList<IList<int>> results) {

        if(start >= a.Length) {
            var ans = new int[a.Length];
            Array.Copy(a, ans, a.Length);
            results.Add(ans.ToList());
        }

        for(int i = 0; i < a.Length; i++) {
            this.Swap(a, start, i);
            this.Permutations(a, start + 1, results);
            this.Swap(a, start, i);
        }

    }

    private void Swap(int[] a, int i, int j) {
        int temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}

public class Solution {
    //input: 1,2,3
    //call 0: add 1
    //call 1: skip 1 //1,2
    //call 2: skip 1, 2 // add 3 // 1,2,3
    //call 3: base case, 1,2,3 -> add to result
    //call 2: remove 3, return // temp: 1,2
    //call 1: remove 2, add 3 // temp: 1,3
    //call 4: skip 1, add 2 // temp: 1,3,2
    //call 5: base case, 1,3,2 -> add to result
    //call 4: remove 2, skip 3
    
    public IList<IList<int>> Permute(int[] nums) {
        var result = new List<IList<int>>();
        var temp = new List<int>();
        this.BackTrack(nums, result, temp);
        return result;
    }
    
    public void BackTrack(int[] nums, List<IList<int>> result, List<int> temp){
        
        if(temp.Count == nums.Length) {
            result.Add(new List<int>(temp));
            return;
        }
        
        foreach(var num in nums) {
            if(temp.Contains(num)) continue;
            temp.Add(num);
            this.BackTrack(nums, result, temp);
            temp.RemoveAt(temp.Count - 1);
        }
    }
}