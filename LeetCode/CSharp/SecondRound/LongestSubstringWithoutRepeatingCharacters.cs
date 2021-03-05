namespace LeetCode.CSharp.SecondRound
{
    public class LongestSubstringWithoutRepeatingCharacters
    {
         public int LengthOfLongestSubstring(string s)
         {
             if (s.Length == 0) return 0;
             if (s.Length == 1 || string.IsNullOrWhiteSpace(s)) return 1;

             int maxLen = 0;
             int start = 0;

             int[] indexes = new int[128];
             for(int i = 0; i < indexes.Length; i++)
             {
                 indexes[i] = -1;
             }

             for (int i = 0; i < s.Length; i++)
             {
                 if (indexes[(int) s[i]] >= start)
                    start = indexes[(int) s[i]] + 1;
                indexes[(int) s[i]] = i;
                maxLen = Math.Max(maxLen, i - start + 1);
             }

             return maxLen;
         }
    }
}