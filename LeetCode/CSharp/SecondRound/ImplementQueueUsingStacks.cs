namespace LeetCode.CSharp.SecondRound
{
    public class ImplementQueueUsingStacks
    {
        public class MyQueue
        {
            private Stack<int> _outgoing;
            private Stack<int> _incoming;

            public MyQueue()
            {
                _incoming = new Stack<int>();
                _outgoing = new Stack<int>();
            }

            public void Push(int x)
            {
                _incoming.push(x);
                if (!_outgoing.Any()) Transfer(_incoming, _outgoing);

            }

            public int Pop()
            {
                int val = _outgoing.Pop();
                if (!_outgoing.Any()) Transfer(_incoming, _outgoing);
                return val;
            }

             /** Get the front element. */
            public int Peek() 
            {
                return outgoing.Peek();
            }

            /** Returns whether the queue is empty. */
            public bool Empty() 
            {
                return !outgoing.Any();
            }

            private void Transfer(Stack<int> incoming, Stack<int> outgoing)
            {
                while(incoming.Any())
                {
                    outgoing.Push(incoming.Pop());
                }
            }

        }
    }
}