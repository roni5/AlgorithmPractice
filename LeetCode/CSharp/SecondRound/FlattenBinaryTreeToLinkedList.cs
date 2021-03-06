namespace LeetCode.CSharp.SecondRound
{
    public class FlattenBinaryTreeToLinkedList
    {
        public void Flatten(TreeNode root)
        {
            if (root == null) return;

            TreeNode node = root;

            while (node != null)
            {
                if (node.left != null)
                {
                    TreeNode rightmost = node.left;
                    while (rightmost.next != null)
                    {
                        rightmost = rightmost.next;
                    }

                    rightmost.right = node.right;
                    node.right = node.left;
                    node.left = null;
                }

                node = node.right;
            }
        }
    }
}