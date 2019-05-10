# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

def firstUniqChar(self, s: str) -> int:
    count = collections.Counter(s)

    idx = 0
    for letter in s:
        if count[letter] == 1:
            return idx
        else:
            idx += 1

    return -1