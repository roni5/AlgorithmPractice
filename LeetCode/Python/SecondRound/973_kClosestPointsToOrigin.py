import heapq

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

    maxHeap = []

    for x, y in points:
        dist = -(x * x + y * y)
        if len(maxHeap) == k:
            heapq.heappushpop(maxHeap, (dist, x, y))
        else:
            heapq.heappush(maxHeap, (dist,x,y))
    
    return [(x, y) for (dist, x, y) in maxHeap]