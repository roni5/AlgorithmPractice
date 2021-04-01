 def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
     if not root:
         return None
    
     if root.val == p.val or root.val == q.val:
         return root
     
     left = self.lowestCommonAncestor(root.left, p, q)
     right = self.lowestCommonAncestor(root.right, p, q)

     if not left:
         return right
        
     if not right:
         return left
        
     return root