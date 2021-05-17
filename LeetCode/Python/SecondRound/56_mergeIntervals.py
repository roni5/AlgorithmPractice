def merge(self, intervals: List[List[int]]) -> List[List[int]]:

    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    merged = []
    merged.append(intervals[0])

    for i in range(1, len(intervals)):
        interval = intervals[i]
        prevInterval = merged[-1]
        if prevInterval[1] >= interval[0]:
            merged[-1][1] = max(prevInterval[1], interval[1])
        else:
            merged.append(interval)
    
    return merged
