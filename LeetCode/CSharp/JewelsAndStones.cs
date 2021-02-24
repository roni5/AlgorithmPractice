public class Solution {
    public int NumJewelsInStones(string J, string S) {
        int ans = 0;
        var jewel = new HashSet<char>();

        for(int i = 0; i < J.Length; i++)
        {
            jewel.Add(J[i]);
        }

        for(int i = 0; i < S.Length; i++)
        {
            if(jewel.Contains(S[i])) ans++;
        }
        
        return ans;
    }
}