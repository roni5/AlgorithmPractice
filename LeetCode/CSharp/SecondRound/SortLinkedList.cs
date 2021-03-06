namespace LeetCode.CSharp.SecondRound
{
    public class SortLinkedList
    {
        public ListNode SortList(ListNode head) 
        {
            
            if (head == null || head.next == null) return head;
            
            var leftHalf = head;
            var rightHalf = FindMiddle(head);
            
            leftHalf = SortList(leftHalf);
            rightHalf = SortList(rightHalf);
            
            return Merge(leftHalf, rightHalf);
            
        }
    
        private ListNode FindMiddle(ListNode head)
        {
            var slow = head;
            var fast = head;
            
            while (fast.next != null && fast.next.next != null)
            {
                slow = slow.next;
                fast = fast.next.next;
            }
            
            var returnHead = slow.next;
            slow.next = null;
            
            return returnHead;
        }
        
        private ListNode Merge(ListNode left, ListNode right)
        {
            ListNode newList = null;
            ListNode returnHead = null;
            
            if (left.val < right.val)
            {
                newList = left;
                returnHead = left;
                left = left.next;
            }
            else
            {
                newList = right;
                returnHead = right;
                right = right.next;
            }
            
            while (left != null && right != null)
            {
                if (left.val < right.val)
                {
                    newList.next = left;
                    newList = newList.next;
                    left = left.next;
                }
                else
                {
                    newList.next = right;
                    newList = newList.next;
                    right = right.next;
                }
            }
            
            while (left != null)
            {
                newList.next = left;
                newList = newList.next;
                left = left.next;
            }
            while (right != null)
            {
                newList.next = right;
                newList = newList.next;
                right = right.next;
            }
            
            return returnHead;
        }
    }
}