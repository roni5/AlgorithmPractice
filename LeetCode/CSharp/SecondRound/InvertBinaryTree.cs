namespace LeetCode.CSharp.SecondRound
{
    public class InvertBinaryTree
    {
        public TreeNode InvertTree(TreeNode root)
        {
            if (root == null) return root;

            TreeNode temp = root.right;
            root.right = root.left;
            root.left = temp;

            InvertTree(root.left);
            InvertTree(root.right);

            return root;
        }
    }
}