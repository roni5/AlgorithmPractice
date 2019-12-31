public class Tree
{
    private class Node
    {
        private int value;
        private Node leftChild;
        private Node rightChild;

        public Node(int value)
        {
            this.value = value;
        }
    }

    private Node root;

    public void Insert(int value)
    {
        if(root == null)
        {
            this.root = new Node(value);
            return;
        }
    }
}