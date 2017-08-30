import random

class Node(object):
    def __init__(self, value, nextNode=None, prev=None):
        self.value = value
        self.next = nextNode
        self.prev = prev

    def __str__(self):
        return str(self.value)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_to_begining(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.head = Node(value, self.head)
        return self.head

    def generate(self, num, minimum, maximum):
        self.head = None
        self.tail = None
        for i in range(num):
            self.add(random.randint(minimum, maximum))
        return self
