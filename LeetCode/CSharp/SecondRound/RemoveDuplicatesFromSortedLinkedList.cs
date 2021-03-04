namespace LeetCode.CSharp.SecondRound
{
    public class RemoveDuplicatesFromSortedLinkedList
    {
        public ListNode DeleteDuplicates(ListNode head)
        {
            if (head == null || head.next == null)
            {
                return head;
            }

            ListNode dummy = head;

            while (head != null && head.next != null)
            {
                if (head.val == head.next.val)
                    head.next = head.next.next;
                else
                    head = head.next;
            }

            return dummy;
        }
    }
}