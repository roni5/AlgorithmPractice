namespace LeetCode.CSharp.SecondRound
{
    public class SearchInABinaryTreeIterative
    {
        public TreeNode SearchBST(TreeNode root, int val) 
        {
            if (root == null) return null;

            while (root != null)
            {
                if (root.val == val) return root;
                else if (val > root.val) root = root.right;
                else root = root.left;
            }

            return null;
        }
    }
}