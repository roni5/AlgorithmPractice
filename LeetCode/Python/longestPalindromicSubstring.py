def longestPalindrome(self, s: str) -> str:

    if len(s) == 0:
        return s

    start = 0
    length = len(s)
    maxLength = 0
    table = [[False for x in range(length)] for x in range(length)]

    for i in range(length):
        table[i][i] = True
        start = i
        maxLength = 1
    
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            table[i][i+1] = True
            start = i
            maxLength = 2
    
    j = 0
    for k in range(3, length + 1):
        for i in range(length - k + 1):
            j = i + k - 1
            if(s[i] == s[j] and table[i+1][j-1] == True):
                table[i][j] = True
               
                if k > maxLength:
                    start = i
                    maxLength = k

    return s[start: start + maxLength]
    
class Solution(object):
    startIdx = 0
    maxLen = 1
    def longestPalindrome(self, s):

        for i in range(len(s)):
            self.expandAroundCenter(i - 1, i + 1,s)
            self.expandAroundCenter(i, i + 1,s)

        return s[self.startIdx:self.startIdx + self.maxLen]
    
    
    def expandAroundCenter(self,left, right,s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            currentLen = right - left + 1
            if(currentLen > self.maxLen):
                self.maxLen = currentLen
                self.startIdx = left
            left -= 1
            right += 1
