from CrackingCoding.chapter2.LinkedList import LinkedList


def remove_dups(linkedlist):
    if linkedlist.head is None:
        return 'LinkedList empty'
    current =linkedlist.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            print(seen)
            current = current.next
    return linkedlist


linkedlist = LinkedList()
linkedlist.generate(20, 0, 4)
print(linkedlist)
linkedlist = remove_dups(linkedlist)
print(linkedlist)
