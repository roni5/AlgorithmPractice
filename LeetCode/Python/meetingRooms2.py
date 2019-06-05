import heapq

class Solution:
    def minMeetingRooms(self, intervals):

        if len(intervals) == 0 or intervals is None:
            return 0

        intervals = sorted(intervals, key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])

        for i in range(1, len(intervals)):
            if free_rooms[0] <= intervals[i][0]:
                heapq.heappop(free_rooms)
            
            heapq.heappush(free_rooms, intervals[i][1])
        
        return len(free_rooms)
