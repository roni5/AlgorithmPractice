class Solution {
    public List<string> Permutations(string s) {
        var result = new List<string>();
        Permutations("", s, result);
        return result;
    }

    private void Permutations(string prefix, string suffix, List<string> result) {

        //Base case
        if(suffix.Length == 0) {
            result.Add(prefix);
        }

        for(int i = 0; i < suffix.Length; i++) {
            Permutations(prefix + suffix[i], siffix.Substring(0, i) + suffix.Substring(i + 1, suffix.Length - i));
        }

    }

}