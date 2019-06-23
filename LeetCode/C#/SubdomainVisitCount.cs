public class Solution {
    public IList<string> SubdomainVisits(string[] cpdomains) {
        
        var answer = new List<string>();
        var count = new Dictionary<string, int>();

        foreach (string domain in cpdomains)
        {
            string[] temp = domain.Split(" ");
            int visitCount = Convert.ToInt32(temp[0]);
            string[] subDomain = temp[1].Split(".");
            int n = subDomain.Length - 1;
            string key = string.Empty;
            for(int i = n ; i >= 0; i--)
            {
                key = subDomain[i] + (i < n ? "." : "") + key;
                if(!count.ContainsKey(key)) count[key] = visitCount;
                else count[key] += visitCount;
            }
        }

        foreach(KeyValuePair<string, int> pair in count)
        {
            answer.Add($"{pair.Value} {pair.Key}");
        }

        return answer;
    }
}