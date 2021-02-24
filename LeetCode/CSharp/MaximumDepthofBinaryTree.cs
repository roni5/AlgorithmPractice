public class Solution {
    public int MaxDepth(TreeNode root) {

        if(root == null) return 0;

        int leftHeight = MaxDepth(root.left);
        int rightHeight = MaxDepth(root.right);
        return Math.Max(leftHeight, rightHeight) + 1;
    }
}