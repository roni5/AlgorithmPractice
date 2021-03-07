namespace LeetCode.CSharp.SecondRound
{
    public class BalancedBinaryTree
    {
        private class TreeInfo
        {
            public int Height { get; set; }
            public bool Balanced { get; set; }

            public BalancedBinaryTree(int height, bool balanced)
            {
                Height = height;
                Balanced = balanced;
            }

            public bool IsBalanced(TreeNode root)
            {
                return IsBalancedTree(root).Balanced;
            }

            private TreeInfo IsBalancedTree(TreeNode root)
            {
                if (root == null)
                    return new TreeInfo(-1, true);

                TreeInfo left = IsBalancedTree(root.left);
                if (!left.Balanced)
                    return new TreeInfo(-1, false);

                TreeInfo right = IsBalancedTree(root.right);
                if (!right.Balanced)
                    return new TreeInfo(-1, false);
                
                if (Math.Abs(left.Height - right.Height) < 2)
                    return new TreeInfo(Math.Max(left.Height, right.Height) + 1, true);
                
                return new TreeInfo(-1, false);
            }
        }
    }
}