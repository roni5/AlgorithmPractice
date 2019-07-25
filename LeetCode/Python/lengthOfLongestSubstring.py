class Solution:
    def lengthOfLongestSubstring(self, s):
        
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

    def lengthOfLongestSubstring2(self, s):
        dict = {}
        windowStart = 0
        maxLen = 0

        for i, letter in enumerate(s):

            if letter in dict and dict[letter] >= windowStart:
                windowStart = dict[letter] + 1
            
            dict[letter] = i
            maxLen = max(maxLen, i - windowStart + 1)
        
        return maxLen

