public class Solution {
    public int RomanToInt(string s) {
        int answer = 0;
        var dict = new Dictionary<char,int>()
        {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        for(int i = 0; i < s.Length; i++)
        {
            answer += dict[s[i]];
            answer -= Check(s, i, dict);   
        }

        return answer;

    }

    public int Check(string s, int i, Dictionaty<char, int> dict)
    {
        if(i != 0)
        {
            if(dict[s[i - 1]] < dict[s[i]]) return dict[s[i - 1]] * 2;
        }

        return 0;
    }
}