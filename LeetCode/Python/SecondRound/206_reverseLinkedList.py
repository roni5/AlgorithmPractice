def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre = None
        current = head

        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next

        return pre
