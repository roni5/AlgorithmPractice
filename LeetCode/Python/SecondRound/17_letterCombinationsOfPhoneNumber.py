def letterCombinations(self, digits: str) -> List[str]:
        
    ans = []
    if len(digits) == 0:
        return ans
    
    digitMap = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "qprs",
        "8" : "tuv",
        "9" : "wxyz"
    }

    self.backtrack(ans, digits, digitMap, "", 0)

def backtrack(self, ans, digits, digitMap, curStr, i):

    if len(curStr) == len(digits):
        ans.append(curStr)
        return
    
    for c in digitMap[digits[i]]:
        self.backtrack(ans, digits, digitMap, curStr + c, i + 1)