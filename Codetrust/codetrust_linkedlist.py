import random

class Node(object):
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

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

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

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

    def generate(self, number, min_value, max_value):
        self.head = self.tail = None
        for i in range(number):
            self.add(random.randint(min_value,max_value))
        return self

class DoubleLinkedList(LinkedList):
    def add(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self.tail

linkedlist = LinkedList()
linkedlist.generate(10, 1, 20)
print(linkedlist)

def reverse_linked_list(head):
    if head is None or head.next is None:
        return head


    list_to_do = head.next
    reversed_list = head
    reversed_list.next = None

    while list_to_do:
        temp = list_to_do
        list_to_do = list_to_do.next

        temp.next = reversed_list
        reversed_list = temp

    return reversed_list

print(reverse_linked_list(linkedlist.head))

