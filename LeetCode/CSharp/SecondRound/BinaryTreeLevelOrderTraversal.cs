namespace LeetCode.CSharp.SecondRound
{
    public class BinaryTreeLevelOrderTraversal
    {
        public IList<IList<int>> LevelOrder(TreeNode root) {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        List<IList<int>> ans = new List<IList<int>>();
        
        if(root != null)
            queue.Enqueue(root);
        
        while(queue.Count != 0)
        {
            int size = queue.Count;
            List<int> temp = new List<int>();
            
            for(int i = 0; i < size; i++)
            {
                TreeNode cur = queue.Dequeue();
                temp.Add(cur.val);
                if (cur.left != null)
                {
                    queue.Enqueue(cur.left);
                }
                if (cur.right != null)
                {
                    queue.Enqueue(cur.right);
                }
            }
            
            ans.Add(temp);
            
        }
        
        return ans;
    }
    }
}