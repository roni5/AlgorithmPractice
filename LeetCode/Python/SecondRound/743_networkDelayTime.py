import heapq
import collections
def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

    graph = collections.defaultdict(list)

    for u, v, w in times:
        graph[u].append((v, w))
    
    minHeap = [(0, k)]
    visited = set()
    time = 0

    while minHeap:
        w1, n1 = heapq.heappop(minHeap)
        if n1 in visited:
            continue
        visited.add(n1)
        time = max(time, w1)

        for neighbor, weight in graph[n1]:
            if neighbor not in visited:
                heapq.heappush(minHeap, (weight + w1, neighbor))
    
    return 