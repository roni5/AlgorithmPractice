def maxDepth(self, root: TreeNode) -> int:

    if root in None:
        return 0

    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right) + 1

