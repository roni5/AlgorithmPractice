from CrackingCoding.chapter2.LinkedList import LinkedList

def remove_dups(linkedlist):
    if linkedlist.head is None:
        return 'List empty'
    else:
        current = linkedlist.head
        seen = set([current.value])
        while current.next:
            if current.next.value in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.value)
                current = current.next
        return linkedlist

ll = LinkedList()
ll.generate(20, 0, 5)
print(ll)
remove_dups(ll)
print(ll)