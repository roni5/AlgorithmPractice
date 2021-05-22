class Solution:
    ans = 0
    
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.getLongestPath(root)

        return self.ans

    def getLongestPath(self, root):

        if not root:
            return 0

        left = self.getLongestPath(root.left)
        right = self.getLongestPath(root.right)

        if root.left and root.left.val == root.val:
            left += 1
        else:
            left = 0
        
        if root.right and root.right.val == root.val:
            right += 1
        else:
            right = 0

        self.ans = max(self.ans, left + right)
        return max(left, right)