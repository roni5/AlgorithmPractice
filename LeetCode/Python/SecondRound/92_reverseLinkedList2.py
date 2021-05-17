def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

    if not head:
        return head
    if left == right:
        return head
    
    prev = None
    cur = head

    while left > 1:
        prev = cur
        cur = cur.next
        left -= 1
        right -= 1
    
    connection = prev
    tail = cur

    while right > 0:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        right -= 1
    
    if connection:
        connection.next = prev
    else:
        head = prev
    
    tail.next = cur

    return head
