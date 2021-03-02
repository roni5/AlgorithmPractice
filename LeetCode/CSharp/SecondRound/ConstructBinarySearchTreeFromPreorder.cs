namespace LeetCode.CSharp.SecondRound
{
    public class ConstructBinarySearchTreeFromPreorder
    {
        public TreeNode BstFromPreorder(int[] preorder)
        {
            int n = preorder.Length;
            var st = new Stack<TreeNode>();
            var pointer = new TreeNode();
            var root = new TreeNode(preorder[0]);
            pointer = root;
            int i = 1;

            while (i < n)
            {
                if (preorder[i] < pointer.val)
                {
                    var newNode = new TreeNode(preorder[i++]);
                    pointer.left = newNode;
                    st.Push(pointer);
                    pointer = newNode;
                }
                else
                {
                    int parentVal = st.Count == 0 ? int.MaxValue : st.Peek().val;
                    if (preorder[i] > pointer.val && preorder[i] < parentVal)
                    {
                        var newNode = new TreeNode(preorder[i++]);
                        pointer.right = newNode;
                        pointer = newNode;
                    }
                    else
                    {
                        pointer = st.Pop();
                    }
                }
            }

            return root;
        }
    }
}