import collections

def canPermutePalindrome(self, s: str) -> bool:
    
    counter = collections.Counter(s)

    count = 0
    for letter in counter:
        count += counter[letter] % 2
    
    return count <= 1