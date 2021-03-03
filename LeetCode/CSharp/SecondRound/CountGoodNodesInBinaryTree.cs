namespace LeetCode.CSharp.SecondRound
{
    public class CountGoodNodesInBinaryTree
    {
         public int GoodNodes(TreeNode root)
         {
             return CountGoodNodes(root, int.MinValue);
         }

         private int CountGoodNodes(TreeNode root, int maxValSoFar)
         {
             if (root == null) return 0;
             int isThisGood = root.val >= maxValSoFar ? 1 : 0;
             int left = CountGoodNodes(root.left, Math.Max(maxValSoFar, root.val));
             int right = CountGoodNodes(root.right, Math.Max(maxValSoFar, root.val));
             return isThisGood + left + right;
         }
    }
}