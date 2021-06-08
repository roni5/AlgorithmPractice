import collections
def longestPalindrome(self, s: str) -> int:

    res = 0
    freq = collections.Counter(s)

    for c, count in freq.items():
        res += count // 2 * 2
        if res % 2 == 0 and count % 2 == 1:
            res += 1
    
    return res