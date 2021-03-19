def connect(self, root: 'Node') -> 'Node':
    
    if not root:
        return None
    
    queue = deque()
    queue.append(root)

    while queue:
        size = len(queue)
        prev = Node(0)
        for i in range(size):
            node = queue.popleft()
            prev.next = node
            prev = prev.next

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return root