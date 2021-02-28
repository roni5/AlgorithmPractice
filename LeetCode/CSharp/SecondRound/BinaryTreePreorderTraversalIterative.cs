namespace LeetCode.CSharp.SecondRound
{
    public class BinaryTreePreorderTraversalIterative
    {
        public IList<int> PreorderTraversal(TreeNode root)
        {
            List<int> ans = new List<int>();
            Stack<TreeNode> st = new Stack<TreeNode>();

            while (root != null || st.Count != 0)
            {
                if (root != null)
                {
                    ans.Add(root.val);
                    st.Push(root);
                    root = root.left;
                }
                else
                {
                    root = st.Pop();
                    root = root.right;
                }
            }

            return ans;
        }
    }
}