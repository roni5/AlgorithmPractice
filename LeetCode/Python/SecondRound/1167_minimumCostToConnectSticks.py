import heapq
def connectSticks(self, sticks: List[int]) -> int:

    minCost = 0
    heapq.heapify(sticks)

    while len(sticks) > 1:
        x = heapq.heappop(sticks)
        y = heapq.heappop(sticks)

        minCost += x + y
        heapq.heappush(sticks, x + y)
        
    return minCost