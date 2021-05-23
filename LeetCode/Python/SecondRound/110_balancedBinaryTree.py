def isBalanced(self, root: TreeNode) -> bool:

    return self.checkBalance(root)[1]

def checkBalance(self, root):

    if not root:
        return (0, True)
    
    leftHeight, leftBalanced = self.checkBalance(root.left)
    rightHeight, rightBalanced = self.checkBalance(root.right)

    return (max(leftHeight, rightHeight) + 1, leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1)


    O(n), O(n)