public class Solution {
    public bool IsAnagram(string s, string t) {

        Dictionary<char, int> dict1 = new Dictionary<char,int>();

        foreach(var ch in s){
            if(!dict1.ContainsKey(ch)) dict1.Add(ch, 1);
            else dict1[ch] += 1;
        }
        foreach(var ch in t){
            if(!dict1.ContainsKey(ch)) return false;
            else dict1[ch] -= 1;
        }

        foreach(KeyValuePair<char,int> pair in dict1) {
            if(pair.Value != 0){
                return false;
            }
        }

        return true;

        
    }
}