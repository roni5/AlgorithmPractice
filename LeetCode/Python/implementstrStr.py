# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

def strStr(self, haystack: str, needle: str) -> int:

    if len(needle) == 0 or haystack == needle:
        return 0

    window = len(needle)
    for i in range(len(haystack) - window + 1):
        if haystack[i: i + window] == needle:
            return i
    
    return -1