class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [None] * k
        self.head = -1
        self.tail = -1
        self.length = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.size
        
        self.queue[self.tail] = value
        self.length += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.size
        self.length -= 1
        return True

    def Front(self) -> int:
        return self.queue[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.queue[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.length == 0

    def isFull(self) -> bool:
        return self.length == self.size