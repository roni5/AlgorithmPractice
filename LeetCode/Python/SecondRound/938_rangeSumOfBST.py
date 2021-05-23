def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

    ans = 0

    if not root:
        return ans
    
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            if low <= node.val <= high:
                ans += node.val
            if low < node.val:
                stack.append(node.left)
            if high > node.val:
                stack.append(node.right)
    
    return ans

    O(n), O(n)