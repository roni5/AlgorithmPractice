def findAncestors(root, k):
    
    if root is None:
        return None
    
    anscestors = []
    current = root

    while current is not None:
        if k < current.val:
            anscestors.append(current.val)
            current = current.left
        elif k > current.val:
            ancestors.append(current.val)
            current = current.right
        else: # when they are equal, it reached the node we are finding
            return anscestors
        
    return None