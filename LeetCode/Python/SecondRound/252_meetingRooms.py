def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    
    if not intervals:
        return False

    if len(intervals) == 1:
        return True
    
    intervals.sort(key=lambda x: x[0])

    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    
    return True
    