namespace LeetCode.CSharp.SecondRound
{
    public class AddTwoNumbers
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            var p1 = l1;
            var p2 = l2;
            ListNode ans = new ListNode();
            ListNode pre = ans;
            int carry = 0;

            while (p1 != null || p2 != null)
            {
                int p1Val = p1 == null ? 0 : p1.val;
                int p2Val = p2 == null ? 0 : p2.val;

                int sum = p1Val + p2Val + carry;
                carry = sum / 10;
                var newNode = new ListNode(sum % 10);
                pre.next = newNode;

                p1 = p1 == null ? null : p1.next;
                p2 = p2 == null ? null : p2.next;
                pre = pre.next;
            }

            if (carry > 0)
                pre.next = new ListNode(carry);

            return ans.next;
        }
    }
}