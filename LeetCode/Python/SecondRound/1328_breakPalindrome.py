def breakPalindrome(self, palindrome: str) -> str:

    if len(palindrome) == 0 or len(palindrome) == 1:
        return ""
    
    start = 0
    end = len(palindrome) - 1
    newPal = list(palindrome)
    
    while start < end:
        if newPal[start] != "a":
            newPal[start] = "a"
            return "".join(newPal)
        start += 1
        end -= 1
        
    newPal[-1] = "b"
    
    return "".join(newPal)