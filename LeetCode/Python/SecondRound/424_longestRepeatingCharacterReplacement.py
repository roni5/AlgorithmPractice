import collections
def characterReplacement(self, s: str, k: int) -> int:

    maxLen = 0
    start = 0
    freq = collections.defaultdict(int)
    maxCharCount = 0

    for end in range(len(s)):
        freq[s[end]] += 1
        maxCharCount = max(maxCharCount, freq[s[end]])

        while (end - start + 1) - maxCharCount > k: #out of operations
            freq[s[start]] -= 1
            start += 1
        
        maxLen = max(maxLen, end - start + 1)

    return maxLen