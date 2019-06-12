def findKthMax(root,k):
  tree = []
  inOrderTraverse(root, tree)
  if ((len(tree)-k) >=0):
    return tree[-k]
  return None

#Helper recursive function to traverse the tree inorder
def inOrderTraverse(node,tree):
  if node != None:
    inOrderTraverse(node.leftChild,tree)
    tree.append(node.val)
    inOrderTraverse(node.rightChild,tree)