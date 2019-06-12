public class Solution {
    public int KthSmallest(TreeNode root, int k) {
        var ans = new List<int>();
        this.Kth(root, ans);
        return ans[k - 1];
    }
    
    private void Kth(TreeNode root, List<int> ans)
    {
        if(root == null) return;
        
        this.Kth(root.left, ans);
        ans.Add(root.val);
        this.Kth(root.right, ans);
    }
}