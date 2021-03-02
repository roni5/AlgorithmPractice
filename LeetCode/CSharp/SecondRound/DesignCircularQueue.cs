namespace LeetCode.CSharp.SecondRound
{
    public class DesignCircularQueue
    {
        public class MyCircularQueue
        {
            private int _size;
            private int _length;
            private int _head;
            private int _tail;
            private int[] _queue;
    
            public MyCircularQueue(int k) {
                _queue = new int[k];
                _size = k;
                _length = 0;
                _head = -1;
                _tail = -1;
            }
    
            public bool EnQueue(int value) {
                
                if (IsFull()) return false;
                else if (IsEmpty())
                {
                    _head = 0;
                    _tail = 0;
                }
                else
                {
                    _tail = (_tail + 1) % _size;
                }
                
                _queue[_tail] = value;
                _length++;
                
                return true;
                
            }
            
            public bool DeQueue() {
                
                if (IsEmpty()) return false;
                //_queue[_head] = null;
                
                _head = (_head + 1) % _size;
                _length--;
                
                return true;
                
            }
            
            public int Front() {
                return IsEmpty() ? -1 : _queue[_head]; 
            }
            
            public int Rear() {
                return IsEmpty() ? -1 : _queue[_tail];
            }
            
            public bool IsEmpty() {
                return _length == 0;
            }
            
            public bool IsFull() {
                return _length == _size;
            }
        }
    }
}