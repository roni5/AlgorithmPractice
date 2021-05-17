def swapPairs(self, head: ListNode) -> ListNode:

    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    cur = head

    while cur and cur.next:
        next = cur.next.next
        second = cur.next

        second.next = cur
        prev.next = second
        cur.next = next

        prev = cur
        cur = next
    
    return dummy.next