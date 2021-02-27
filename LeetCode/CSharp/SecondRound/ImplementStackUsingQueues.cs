namespace LeetCode.CSharp.SecondRound
{
    public class ImplementStackUsingQueues
    {
        private Queue<int> _queue;

    /** Initialize your data structure here. */
        public MyStack() {
            _queue = new Queue<int>();
        }

        public void Push(int x)
        {
            var temp = new Queue<int>();
            temp.Enqueue(x);

            while (_queue.Any())
            {
                temp.Enqueue(_queue.Dequeue());
            }

            _queue = temp;
        }

        public int Pop()
        {
            return _queue.Dequeue();
        }

        public int Top() 
        {
            return _queue.Peek();     
        }
    
    /** Returns whether the stack is empty. */
        public bool Empty() 
        {
            return !_queue.Any();
        }
    }
}