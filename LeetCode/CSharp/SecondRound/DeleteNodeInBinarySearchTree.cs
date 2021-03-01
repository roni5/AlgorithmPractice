namespace LeetCode.CSharp.SecondRound
{
    public class DeleteNodeInBinarySearchTree
    {
        public TreeNode DeleteNode(TreeNode root, int key)
        {
        
            if (root == null) return null;
            
            // delete from the right subtree
            if (key > root.val) root.right = DeleteNode(root.right, key);
            // delete from the left subtree
            else if (key < root.val) root.left = DeleteNode(root.left, key);
            else
            {
                // the node is a leaf
                if (root.left == null && root.right == null)
                    root = null;
                // the node is not a leaf and has a right child
                else if (root.right != null)
                {
                    root.val = Successor(root);
                    root.right = DeleteNode(root.right, root.val);
                }
                // the node is not a leaf, has no right child, and has a left child
                else
                {
                    root.val = Predecessor(root);
                    root.left = DeleteNode(root.left, root.val);
                }
                
            }
            
            return root;
            
    }
            
            /*
        One step right and then always left
        */
        private int Successor(TreeNode root) {
            root = root.right;
            while (root.left != null) root = root.left;
            return root.val;
        }

        /*
        One step left and then always right
        */
        private int Predecessor(TreeNode root) {
            root = root.left;
            while (root.right != null) root = root.right;
            return root.val;
        }
    }
}