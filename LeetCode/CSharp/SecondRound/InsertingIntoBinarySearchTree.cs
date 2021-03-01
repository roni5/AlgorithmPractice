namespace LeetCode.CSharp.SecondRound
{
    public class InsertingIntoBinarySearchTree
    {
        public TreeNode InsertIntoBST(TreeNode root, int val)
        {
            TreeNode newNode = new TreeNode(val);

            if (root = null) return newNode;

            TreeNode pointer = null;
            TreeNode ans = root;

            while (root != null)
            {
                pointer = root;
                if(val == root.val) return null;
                else if(val < root.val) root = root.left;
                else root = root.right;
            }

            if (val < pointer.val) pointer.left = newNode;
            else pointer.right = newNode;

            return ans;
        }
    }
}