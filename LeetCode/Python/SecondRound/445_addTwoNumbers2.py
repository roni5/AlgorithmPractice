def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

    l1 = self.reverse(l1)
    l2 = self.reverse(l2)

    head = None
    carry = 0

    while l1 or l2:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0

        carry, val = divmod(l1Val + l2Val + carry, 10)

        curr = ListNode(val)
        curr.next = head
        head = curr

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    if carry > 0:
        curr = ListNode(carry)
        curr.next = head
        head = curr
    
    return head


def reverse(self, head):
    pre = None
    current = head

    while current:
        next = current.next
        current.next = pre
        pre = current
        current = next
    
    return pre