namespace LeetCode.CSharp.SecondRound
{
    public class DesignLinkedList
    {
        public class MyLinkedList {
    
            public int Length;
            public Node Head;
            public Node Tail;
            
            public class Node
            {
                public int Value;
                public Node Next;
                
                public Node(int val)
                {
                    Value = val;
                    //Next = null;
                }
            }
            /** Initialize your data structure here. */
            public MyLinkedList() {
                Length = 0;
                Head = null;
                Tail = null;
            }
            
            /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
            public int Get(int index) {
                if (Head == null || index >= Length)
                    return -1;
                if (index == Length -1)
                    return Tail.Value;
                
                Node curr = Head;
                for (int i = 0; i < index; i++)
                {
                    curr = curr.Next;
                }
                
                return curr.Value;
                
            }
            
            /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
            public void AddAtHead(int val) {
                Node newNode = new Node(val);
                newNode.Next = Head;
                Head = newNode;
                
                if (Tail == null)
                {
                    Tail = newNode;
                }
                
                Length++;
            }
            
            /** Append a node of value val to the last element of the linked list. */
            public void AddAtTail(int val) {
                
                if (Tail == null)
                {
                    AddAtHead(val);
                    return;
                }
                
                Node newNode = new Node(val);
                Tail.Next = newNode;
                Tail = newNode;
                Length++;
                
            }
            
            /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
            public void AddAtIndex(int index, int val) {
            
                if (index == Length)
                {
                    AddAtTail(val);
                    return;
                }
                if (index == 0)
                {
                    AddAtHead(val);
                    return;
                }
                if (index < 0 || index > Length) return;
                
                Node cur = Head;
                for (int i = 0; i < index - 1; i++)
                {
                    cur = cur.Next;
                }
                
                Node newNode = new Node(val);
                Node next = cur.Next;
                cur.Next = newNode;
                cur.Next.Next = next;
                Length++;
                
                
            }
            
            /** Delete the index-th node in the linked list, if the index is valid. */
            public void DeleteAtIndex(int index) {
            
                if (index < 0 || index >= Length) return;
                if (index == 0)
                {
                    Head = Head.Next;
                    if(Length == 1) Tail = null;
                }
                else
                {
                    Node cur = Head;
                    for (int i = 0; i < index - 1; i++)
                    {
                        cur = cur.Next;
                    }
                    Node nodeToRemove = cur.Next;
                    cur.Next = nodeToRemove.Next;
                    if (nodeToRemove == Tail) Tail = cur;
                    
                }
                
                Length--;
            }
        }
    }
}