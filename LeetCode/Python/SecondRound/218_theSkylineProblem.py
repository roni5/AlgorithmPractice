import heapq

class MaxHeap:
    def __init__(self) -> None:
        self.data = []
    
    def peek(self):
        return 0 if not self.data else -self.data[0]
    
    def add(self, height):
        heapq.heappush(self.data, -height)
    
    def remove(self, height):
        self.data.remove(-height)
        heapq.heapify(self.data)

def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    START = -1
    END = -1
    heap = MaxHeap()
    skyline = []
    events = []

    for l, r, h in buildings:
        events.append((l,h,START))
        events.append((r,h,END))
    events.sort(key=lambda x: [x[0], x[2], x[1] * x[2]])

    for x, h, t in events:
        if t == START:
            if h > heap.peek():
                skyline.append([x, h])
            heap.add(h)
        else:
            heap.remove(h)
            if h > heap.peek():
                skyline.append([x, heap.peek()])
    
    return skyline
