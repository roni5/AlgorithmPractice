public class Solution {
    public bool IsPalindrome(ListNode head) {
        
        ListNode fast = head;
        ListNode mid = head;

        while(fast != null && fast.next != null)
        {
            fast = fast.next.next;
            mid = mid.next;
        }

        ListNode preHead = null;
        while(mid != null)
        {
            ListNode next = mid.next;
            mid.next = preHead;
            preHead = mid;
            mid = next;
        }

        while(preHead != null)
        {
            if(preHead.val != head.val) return false;
            preHead = preHead.next;
            head = head.next;
        }

        return true;

    }
}