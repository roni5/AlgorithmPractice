public int LengthOfLongestSubstring(string s) {

    if(s.Length == 0) return 0;

    int length = s.Length;
    int i = 0;
    int j = 0;
    int answer = 0;
    var mySet = new HashSet<char>();

    while(i < length && j < length) {
        if(!mySet.Contains(s[i])){
            mySet.Add(s[i]);
            i += 1;
            answer = Math.Max(answer, i - j);
        } else {
            mySet.Remove(s[j]);
            j += 1;
        }
    }

    return answer;

}