def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    if not l1:
        return l2
    if not l2:
        return l1
    
    preHead = ListNode()
    added = preHead
    carry = 0

    while l1 or l2:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0
        sumVal = l1Val + l2Val + carry
        carry, val = divmod(sumVal, 10)

        added.next = ListNode(val)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        added = added.next
    
    if carry > 0:
        added.next = ListNode(carry)
    
    return preHead.next