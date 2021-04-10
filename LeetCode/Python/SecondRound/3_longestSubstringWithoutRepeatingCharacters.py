def lengthOfLongestSubstring(self, s: str) -> int:

    start = 0
    end = 0
    seen = set()
    maxLen = 0

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            maxLen = max(maxLen, len(seen))
            end += 1
        else:
            seen.remove(s[start])
            start += 1
    
    return maxLen
