def findHeight(root):
  if root is None:
    return 0
  else:
    return 1 + max(findHeight(root.left), findHeight(root.right)) 