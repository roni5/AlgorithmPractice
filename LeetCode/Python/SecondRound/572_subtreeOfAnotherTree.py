# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

# Example 1:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.

def isSubtree(s,t):
    if s is None:
        return False
    
    return treesAreEqual(s, t) or isSubtree(s.left, t) or isSubtree(s.right, t)

def treesAreEqual(s,t):
    if s is None and t is None:
        return True
    if s is None or t is None:
        return False
    if s.val != t.val:
        return False
    return s.val == t.val and treesAreEqual(s.left, t.left) and treesAreEqual(s.right, t.right)