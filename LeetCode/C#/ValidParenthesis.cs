public class Solution {
    public bool IsValid(string s) {
        
        if(s.Length == 0) return true;
        if(s.Length < 2) return false;
        
        var dict = new Dictionary<char, char>() {
            { '(' , ')'},
            { '[' , ']'},
            { '{' , '}'}
        };

        var stack = new Stack<char>();

        for(int i = 0; i < s.Length; i++)
        {
            if(dict.ContainsKey(s[i]))
            {
                stack.Push(dict[s[i]]);
            }
            else
            {   
                if(stack.Count == 0 || s[i] != stack.Pop()) return false;
            }
        }

        if(stack.Count != 0) return false;

        return true;
    }
}