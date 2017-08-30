from CrackingCoding.chapter2.LinkedList import *

def kth_last(linkedlist, n):
    left_pointer = linkedlist.head
    right_pointer = linkedlist.head

    for i in range(n):
        if right_pointer.next is None:
            return 'Too Short'
        else:
            right_pointer = right_pointer.next

    while right_pointer:
        left_pointer = left_pointer.next
        right_pointer = right_pointer.next

    return left_pointer.value

ll = LinkedList()
ll.generate(20, 0, 50)
print(ll)
print(kth_last(ll, 19))
