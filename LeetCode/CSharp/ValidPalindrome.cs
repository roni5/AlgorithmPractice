public class Solution {
    public bool IsPalindrome(string s) {
        int start = 0;
        int end = s.Length - 1;
        
        while(start < end)
        {
            while(start < end && !char.IsLetterOrDigit(s[end]))
            {
                end -= 1;
            }
            
            while(start< end && !char.IsLetterOrDigit(s[start]))
            {
                start += 1;
            }
            
            if(char.ToLower(s[start]) != char.ToLower(s[end])) return false;
            
            start += 1;
            end -= 1;
        }
        
        return true;
    }
}