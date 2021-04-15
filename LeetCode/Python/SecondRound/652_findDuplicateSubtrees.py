def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
    map = defaultdict(int)
    ans = []

    self.dfs(root, map, ans)

    return ans

def dfs(self, root, map, ans):

    if not root:
        return root

    serial = "{},{},{}".format(root.val, self.dfs(root.left, map, ans), self.dfs(root.right, map,ans))
    
    map[serial] += 1
    if map[serial] == 2:
        ans.append(root)
    
    return serial