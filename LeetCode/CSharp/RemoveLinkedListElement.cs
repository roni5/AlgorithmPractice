/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode RemoveElements(ListNode head, int val) {
        if(head == null) return null;
        
        ListNode dummy = head;

        while(dummy.next != null)
        {
            if(dummy.next.val == val) dummy.next = dummy.next.next;
            else dummy = dummy.next;
        }

        if(head.val == val) head = head.next;

        return head;
    }
}