from CrackingCoding.chapter2.LinkedList import *

def kth_last(linkedlist, k):
    left_pointer = linkedlist.head
    right_pointer = linkedlist.head
    for i in range(k):
        if right_pointer is None:
            return 'List too short'
        right_pointer = right_pointer.next

    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer

ll = LinkedList()
ll.generate(10, 0, 20)
print(ll)
print(kth_last(ll, 2))
