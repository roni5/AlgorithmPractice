def isPalindrome(self, head):
    fast = slow = head
    # find the mid node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse the second half
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    # compare the first and second half nodes
    while node: # while node and head:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next
        
        while head:
            compare_head = stack.pop()
            if head.val != compare_head.val:
                return False
            head = head.next
        
        return True