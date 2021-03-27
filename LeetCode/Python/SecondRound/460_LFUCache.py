class Node:
    def __init__(self, value, count):
        self.val = value
        self.count = count
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeKeys = dict()
        self.nodeCounts = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key: int) -> int:
        
        if key not in self.nodeKeys:
            return -1
        
        node = self.nodeKeys[key]
        del self.nodeCounts[node.count][key]
        
        node.count += 1
        self.nodeCounts[node.count][key] = node
        
        if not self.nodeCounts[self.minCount]:
            self.minCount += 1
        
        return node.val

    def put(self, key: int, value: int) -> None:
        
        if not self.capacity:
            return
        if key in self.nodeKeys:
            self.nodeKeys[key].val = value
            self.get(key)
            return
        if len(self.nodeKeys) == self.capacity:
            leastFrequent, _ = self.nodeCounts[self.minCount].popitem(last=False)
            del self.nodeKeys[leastFrequent]
        
        newNode = Node(value, 1)
        self.nodeKeys[key] = newNode
        self.nodeCounts[1][key] = newNode
        self.minCount = 1
        
        