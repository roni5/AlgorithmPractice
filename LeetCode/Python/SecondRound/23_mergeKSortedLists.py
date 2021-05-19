def mergeKLists(self, lists: List[ListNode]) -> ListNode:

    if not lists or len(lists) == 0:
        return None
    
    return self.mergeLists(lists, 0, len(lists) - 1)

def mergeLists(self, lists, start, end):

    if start == end:
        return lists[start]
    
    mid = start (end - start) // 2
    left = self.mergeLists(lists, start, mid)
    right = self.mergeLists(lists, mid + 1, end)

    return self.merge(left, right)

def merge(self, left, right):
    res = ListNode()
    cur = res

    while left or right:
        leftVal = left.val if left else float('inf')
        rightVal = right.val is right else float('inf')
        if leftVal < rightVal:
            cur.next = left
            left = left.next
        else:
            cur.next = right
            right = right.next
        
        cur = cur.next

    return res.next