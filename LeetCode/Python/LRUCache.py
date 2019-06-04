class LRUCache:

    class Item:

        def __init__(self, key, value):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.map = {}
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        else:
            curr = self.map[key]

            if curr is not self.head:

                if curr is tail:
                    self.tail = self.tail.prev
                
                if curr.next is not None:
                    curr.next.prev = curr.prev
                
                if curr.prev is not None:
                    curr.prev.next = curr.next
                
                curr.next = self.head
                curr.prev = None
                self.head.prev = curr
                self.head = curr
                
           
            return curr.val

    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            curr = Item(key, value)
            
            if self.head is None:
                self.head = curr
                self.tail = curr
            else:
                curr.next = self.head
                self.head.prev = curr
                self.head = curr
            
            self.map[key] = curr

            if len(self.map) > self.capacity:
                self.map.remove(self.tail.key)
                self.tail.prev.next = None
                self.tail = self.tail.prev


                
        else:
            self.map[key].val = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)