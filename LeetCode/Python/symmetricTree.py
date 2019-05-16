
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)

def isMirror(self, r1, r2):
    if r1 is None and r2 is None:
        return True
    if r1 is None or r2 is None:
        return False

    return r1.val == r2.val and self.isMirror(r1.right, r2.left) and self.isMirror(r1.left, r2.right)