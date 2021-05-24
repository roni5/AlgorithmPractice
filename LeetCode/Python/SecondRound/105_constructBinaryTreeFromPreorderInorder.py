def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder.pop(0))
    rootIdx = inorder.index(root.val)
    root.left = self.buildTree(preorder, inorder[:rootIdx])
    root.right = self.buildTree(preorder, inorder[rootIdx + 1:])

    return root
