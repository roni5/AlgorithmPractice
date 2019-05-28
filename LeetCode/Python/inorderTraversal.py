def inorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    self.helper(root, res)
    return res

def helper(self, root, res):
    if root is not None:
        if root.left is not None:
            self.helper(root.left, res)
        
        res.append(root.val)

        if root.right is not None:
            self.helper(root.right, res)

def inorderTraversal_iter(self, root):

    res = []
    stack = []
    curr = root
        
    while curr is not None or len(stack) != 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    
    return res