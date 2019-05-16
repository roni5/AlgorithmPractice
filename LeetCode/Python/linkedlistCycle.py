def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            if slow == slow.next:
                return True
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False