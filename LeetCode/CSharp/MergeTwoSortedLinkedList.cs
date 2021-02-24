/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null) return l2;
        if(l2 == null) return l1;
        
        ListNode dummy1 = new ListNode(0);
        ListNode dummy = dummy1;
        
        while(l1 != null && l2 != null) {
            if(l1.val < l2.val){
                dummy.next = l1;
                l1 = l1.next;
            }else{
                dummy.next = l2;
                l2 = l2.next;
            }
            
            dummy = dummy.next;
        }
        
        if(l1 == null) dummy.next = l2;
        if(l2 == null) dummy.next = l1;
        
        return dummy1.next;
    }
}