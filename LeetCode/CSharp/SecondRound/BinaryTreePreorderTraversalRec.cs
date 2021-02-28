namespace LeetCode.CSharp.SecondRound
{
    public class BinaryTreePreorderTraversalRec
    {
        public IList<int> PreorderTraversal(TreeNode root) {
        
        List<int> ans = new List<int>();
        PreOrder(root, ans);
        return ans;
        
    }
    
    private void PreOrder(TreeNode root, List<int> ans)
    {
        if (root == null) return;
        
        ans.Add(root.val);
        PreOrder(root.left, ans);
        PreOrder(root.right, ans);
    }
    }
}