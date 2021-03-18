def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = self.getKth(groupPrev, k)
        if not kth:
            break

        groupNext = kth.next

        prev = kth.next
        curr = groupPrev.next
        while curr != groupNext:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        nextNode = groupPrev.next
        groupPrev.next = kth
        groupPrev = nextNode
    
    return dummy.next
    

def getKth(self, head, k):

    while head and k > 0:
        head = head.next
        k -= 1
    
    return head