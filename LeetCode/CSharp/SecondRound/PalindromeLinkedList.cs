namespace LeetCode.CSharp.SecondRound
{
    public class PalindromeLinkedList
    {
        public bool IsPalindrome(ListNode head)
        {
            var slow = head;
            var fast = head;

            while (fast != null && fast.next != null)
            {
                slow = slow.next;
                fast = fast.next.next;
            }

            slow = Reverse(slow);
            while (slow != null)
            {
                if (slow.val != head.val)
                    return false;
                slow = slow.next;
                head = head.next;
            }

            return true;
        }
        private ListNode Reverse(ListNode head)
        {
            LisNode pre = null;
            ListNode next;
            ListNode cur = head;

            while (cur != null)
            {
                next = cur.next;
                cur.next = pre;
                pre = cur;
                cur = next;
            }

            return pre;
        }
    }

}