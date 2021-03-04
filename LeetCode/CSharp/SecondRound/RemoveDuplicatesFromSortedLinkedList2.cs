namespace LeetCode.CSharp.SecondRound
{
    public class RemoveDuplicatesFromSortedLinkedList2
    {
         public ListNode DeleteDuplicates(ListNode head)
         {
             var sentinel = new ListNode(0);
             sentinel.next = head;

             var pred = sentinel;

             while (head != null && head.next != null)
             {
                 if (head.next != null && head.val == head.next.val)
                 {
                     while (head.next != null && head.val == head.next.val)
                     {
                         head = head.next;
                     }

                     pred.next = head.next;
                 }
                 else
                 {
                     pred = pred.next;
                 }

                 head = head.next;
             }

             return sentinel.next;
         }
    }
}