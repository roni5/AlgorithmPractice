namespace LeetCode.CSharp.SecondRound
{
    public class BoundaryOfBinaryTree
    {
        public IList<int> BoundaryOfBinaryTree(TreeNode root) 
        {
        
            List<int> leftBoundary = new List<int>();
            List<int> rightBoundary = new List<int>();
            List<int> leaves = new List<int>();
            this.PreOrder(root, leftBoundary, rightBoundary, leaves, 0);
            leftBoundary.AddRange(leaves);
            leftBoundary.AddRange(rightBoundary);
            return leftBoundary;
        
        }
    
        private void PreOrder(TreeNode node, List<int> leftBoundary, List<int> rightBoundary, List<int> leaves, int flag)
        {
            if (node == null) return;
            if (this.IsRightBoundary(flag))
                rightBoundary.Insert(0,node.val);
            else if (this.IsLeftBoundary(flag) || this.IsRoot(flag))
                leftBoundary.Add(node.val);
            else if (this.IsLeaf(node))
                leaves.Add(node.val);
            
            this.PreOrder(node.left, leftBoundary, rightBoundary, leaves, this.LeftChildFlag(node, flag));
            this.PreOrder(node.right, leftBoundary, rightBoundary, leaves, this.RightChildFlag(node, flag));
        }
        
        private bool IsLeaf(TreeNode node)
        {
            return (node.left == null && node.right == null);
        }
        
        private bool IsRightBoundary(int flag)
        {
            return (flag == 2);
        }
        
        private bool IsLeftBoundary(int flag)
        {
            return (flag == 1);
        }
        
        private bool IsRoot(int flag)
        {
            return (flag == 0);
        }
        
        private int LeftChildFlag(TreeNode node, int flag)
        {
            if (this.IsLeftBoundary(flag) || this.IsRoot(flag))
                return 1;
            else if (this.IsRightBoundary(flag) && node.right == null)
                return 2;
            else 
                return 3;
        }
        
        private int RightChildFlag(TreeNode node, int flag)
        {
            if (this.IsRightBoundary(flag) || this.IsRoot(flag))
                return 2;
            else if (this.IsLeftBoundary(flag) && node.left == null)
                return 1;
            else 
                return 3;
        }
    }
}