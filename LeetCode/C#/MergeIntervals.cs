public class Solution {
    public int[][] Merge(int[][] intervals) {
        
        if(intervals.Length <= 1) {
            return intervals;
        }

        Array.Sort(intervals, (a,b) => a[0] -b[0]);

        var ret = new List<int[]>();
        ret.Add(intervals[0]);

        for(int i = 1; i < intervals.Length; i++) {
            var curr = intervals[i];
            var last = ret[ret.Count - 1];

            if(last[1] >= curr[0]) {
                last[1] = Math.Max(curr[1], last[1]);
            } else {
                ret.Add(curr);
            }
        }

        return ret.ToArray();
    }
}