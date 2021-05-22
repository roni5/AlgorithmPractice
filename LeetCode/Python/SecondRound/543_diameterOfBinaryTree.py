class Solution:
    
    ans = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.getDiameter(root)

        return self.ans

    def getDiameter(self, root):

        if not root:
            return 0
        
        left = self.getDiameter(root.left)
        right = self.getDiameter(root.right)

        self.ans = max(self.ans, left + right)

        return max(left, right) + 1