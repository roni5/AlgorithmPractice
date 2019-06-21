def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    dummy = ListNode(0)
    prehead = dummy

    while l1 and l2:
        if l1.val < l2.val:
            prehead.next = l1
            l1 = l1.next
        else:
            prehead.next = l2
            l2 = l2.next
        prehead = prehead.next

    if l1 is None:
        prehead.next = l2
    if l2 is None:
        prehead.next = l1
    
    return dummy.next