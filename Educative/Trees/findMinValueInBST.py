def findMin(root):
    if root is None:
        return None
    
    while root.left is not None:
        root = root.left

    return root.val
    