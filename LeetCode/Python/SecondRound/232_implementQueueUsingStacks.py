class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.incoming = []
        self.outgoing = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.incoming.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        
        return self.outgoing.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outgoing:
            while self.incoming:
                self.outgoing.append(self.incoming.pop())
        
        return self.outgoing[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        return len(self.outgoing) == 0 and len(self.incoming) == 0