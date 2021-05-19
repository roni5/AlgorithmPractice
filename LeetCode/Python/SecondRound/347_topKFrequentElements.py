import collections
import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:

    ans = []
    freq = collections.Counter(nums)

    for key, val in freq.items():
        if len(ans) == k:
            heapq.heappushpop(ans, (val, key))
        else:
            heapq.heappush(ans, (val, key))
    
    return [key for val, key in ans]