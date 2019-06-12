def nodesAtDistanceK(root, k):
    ans = []
    findK(root, k, ans)
    return ans

def findK(root, k , ans):
    if root is None:
        return
    if k == 0:
        ans.appned(root.val)
    else:
        findK(root.left, k - 1, ans)
        findK(root.right,k - 1, ans)

