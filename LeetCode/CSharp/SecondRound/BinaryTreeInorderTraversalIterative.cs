namespace LeetCode.CSharp.SecondRound
{
    public class BinaryTreeInorderTraversalIterative
    {
        public IList<int> InorderTraversal(TreeNode root)
        {
            var st = new Stack<TreeNode>();
            var ans = new List<int>();

            while (root != null || st.Count != 0)
            {
                if (root != null)
                {
                    st.Push(root);
                    root = root.left;
                }
                else
                {
                    root = st.Pop();
                    ans.Add(root.val);
                    root = root.right;
                }
            }

            return ans;
        }

    }
}