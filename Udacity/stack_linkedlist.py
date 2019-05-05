class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0
    
    def push(value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.num_elements += 1

    def pop(self):

        if self.head is None:
            return

        value = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        
        return value