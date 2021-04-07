def breakPalindrome(self, palindrome: str) -> str:

    if len(palindrome) == 0 or len(palindrome) == 1:
        return None
    
    start = 0
    end = len(palindrome) - 1
    newPal = list(palindrome)

    for idx, letter in enumerate(newPal):
        if letter != 'a':
            newPal[idx] = 'a'
            return "".join(newPal)
        start += 1
        end -= 1
    
    newPal[-1] = 'b'
    return "".join(newPal)