namespace LeetCode.CSharp.SecondRound
{
    public class SearchInABinarySearchTree
    {
        //O(log n)
        public TreeNode SearchBST(TreeNode root, int val)
        {
            if (root == null) return null;
            return SearchNode(root, val);
        }

        private TreeNode SearchNode(TreeNode root, int val)
        {
            if (root == null) return null;
            if (val < root.val) return SearchNode(root.left, val);
            else if (val > root.val) return SearchNode(root.right, val);
            else return root;
        }
    }
}