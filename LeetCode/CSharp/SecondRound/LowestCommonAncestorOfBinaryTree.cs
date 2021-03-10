namespace LeetCode.CSharp.SecondRound
{
    public class LowestCommonAncestorOfBinaryTree
    {
        public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q)
        {
            var pathToP = new List<TreeNode>();
            var pathToQ = new List<TreeNode>();

            if (!GetPath(root, pathToP, p.val) || !GetPath(root, pathToQ, q.val))
                return null;
            
            int minLength = Math.Min(pathToP.Count, pathToQ.Count);

            int i = 0;
            while (i < minLength)
            {
                if (pathToP[i].val == pathToQ[i].val)
                    i++;
                else
                    break;
            }

            return pathToP[i - 1];

        }

        private bool GetPath(TreeNode root, List<TreeNode> path, int val)
        {
            if (root == null)
                return false;
            
            path.Add(root);
            if (root.val == val)
                return true;
            
            if (GetPath(root.left, path, val) || GetPath(root.right, path, val))
                return true;
            
            path.RemoveAt(path.Count - 1);
            return false;
        }
    }
}