namespace LeetCode.CSharp.SecondRound
{
    public class InsertingIntoBinarySearchTreeRec
    {
        public TreeNode InsertIntoBST(TreeNode root, int val)
        {
            if (root == null) return new TreeNode(val);
            return Insert(root, val);
        }

        private TreeNode Insert(TreeNode root, int val)
        {
            TreeNode newNode;
            if (root == null)
            {
                newNode = new TreeNode(val);
                return newNode;
            }
            else if (val < root.val)
                root.left = Insert(root.left, val);
            else
                root.right = Insert(root.right, val);
            
            return root;
        }
    }
}