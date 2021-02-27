namespace LeetCode.CSharp.SecondRound
{
    public class AddStrings
    {
        public string AddStrings(string num1, string num2)
        {
            var map = new Dictionary<char, int>
            {
                {'0', 0},
                {'1', 1}, 
                {'2', 2}, 
                {'3', 3}, 
                {'4', 4}, 
                {'5', 5}, 
                {'6', 6}, 
                {'7', 7}, 
                {'8', 8}, 
                {'9', 9}, 
            };

            int carry = 0;
            int p1 = num1.Length;
            int p2 = num2.Length;
            var sb = new StringBuilder();

            while (p1 >= 0 || p2 >= 0)
            {
                int a = p1 >= 0 ? map[num1[p1]] : 0;
                int b = p2 >= 0 ? map[num2[p2]] : 0;
                int val = (a + b + carry) % 10;
                carry = (a + b + carry) / 10;
                sb.Insert(0, val);
                p1--;
                p2--;
            }

            if (carry != 0)
                sb.Insert(0, val);
            
            return sb.ToString();
        }
    }
}