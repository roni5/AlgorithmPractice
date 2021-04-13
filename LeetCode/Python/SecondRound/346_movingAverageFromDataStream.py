class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.capacity = size
        self.windowSum = 0
    
    def next(self, val: int) -> float:
        
        self.windowSum += val
        if len(self.data) == self.capacity:
            head = self.data.popleft()
            self.windowSum -= head
        self.data.append(val)
        
        return self.windowSum / len(self.data)
