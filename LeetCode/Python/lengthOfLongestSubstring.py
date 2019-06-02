class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = 0
        length = len(s)
        i = 0
        j = 0
        mySet = set()

        while i < length and j < length:
            if s[i] not in mySet:
                mySet.add(s[i])
                i += 1
                ans = max(ans, i - j)
            else:
                mySet.remove(s[j])
                j += 1
                
        return ans