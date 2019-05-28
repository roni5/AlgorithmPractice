public class Solution {
    public int FirstUniqChar(string s) {
        var dict = new Dictionary<char, int>();
        
        foreach(char ch in s) {
            if(!dict.ContainsKey(ch)){
                dict.Add(ch, 1);
            }else {
                dict[ch] += 1;
            }
        }
        
        for(int i = 0; i < s.Length; i++){
            if(dict[s[i]] == 1) {
                return i;
            }
        }
        
        return -1;
    }
}