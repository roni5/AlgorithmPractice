class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        length = len(intervals)

        if length <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        ret = []
        ret.append(intervals[0])
        for i in range(1, length):
            curr = intervals[i]
            last_ret = ret[len(ret) - 1]

            if last_ret[1] >= curr[0]:
                last_ret[1] = max(curr[1], last_ret[1])
            else:
                ret.append(curr)
        
        return ret