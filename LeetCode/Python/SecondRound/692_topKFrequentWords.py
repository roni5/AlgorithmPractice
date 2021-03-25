import collections
import heapq

def topKFrequent(self, words: List[str], k: int) -> List[str]:
    count = collections.Counter(words)
    maxHeap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(maxHeap)

    return [heapq.heappop(maxHeap)[1] for _ in range(k)]
    