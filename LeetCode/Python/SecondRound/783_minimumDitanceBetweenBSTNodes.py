class Solution:
    
    minDif = float("inf")
    preVal = float("-inf")
    
    def minDiffInBST(self, root: TreeNode) -> int:

        if not root:
            return

        self.minDiffInBST(root.left)
        self.minDiff = min(self.minDif, root.val - self.preVal)
        self.preVal = root.val
        self.minDiffInBST(root.right)

        return self.minDif