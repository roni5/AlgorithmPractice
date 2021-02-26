namespace LeetCode.CSharp.SecondRound
{
    public class ValidParentheses
    {
         public bool IsValid(string s)
         {
             var stack = new Stack<char,char>();
             var map = new Dictionary<char, char>();

             for (int i = 0; i < s.Length; i++)
             {
                if (map.ContainsKey(s[i]))
                    stack.Push(map[s[i]]);
                else
                {
                    if (stack.Count == 0 || s[i] != stack.Pop())
                        return false;
                }
             }

             return stack.Count == 0 ? true : false;

         }
    }
}