/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB) {
        ListNode curA = headA;
        ListNode curB = headB;
        int lenA = 0;
        int lenB = 0;

        while(curA != null)
        {
            lenA += 1;
            curA = curA.next;
        }

        while(curB != null)
        {
            lenB += 1;
            curB = curB.next;
        }

        curA = headA;
        curB = headB;

        if(lenA > lenB)
        {
            for(int i = 0; i < lenA - lenB; i++)
            {
                curA = curA.next;
            }
        }

        if(lenB > lenA)
        {
            for(int i = 0; i < lenB - lenA; i++)
            {
                curB = curB.next;
            }
        }

        while(curA != curB)
        {
            curA = curA.next;
            curB = curB.next;
        }

        return curA;
    }
}