def inorderSuccessor(self, node: 'Node') -> 'Node':

    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    else:
        while node.parent and node.val > node.parent.val:
            node = node.parent
        return node.parent if node.parent else None
        