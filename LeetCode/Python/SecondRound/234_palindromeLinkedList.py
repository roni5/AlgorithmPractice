def isPalindrome(self, head: ListNode) -> bool:

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    slow = self.reverse(slow)

    while slow:
        if slow.val != head.val:
            return False
        slow = slow.next
        head = head.next
    
    return True

def reverse(self, head):
    pre = None
    cur = head

    while cur:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    
    return pre
