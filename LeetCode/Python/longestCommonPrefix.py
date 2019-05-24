# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(self, strs: List[str]) -> str:
    
    if len(strs) == 0:
        return ""

    for i in range(len(strs[0])):
        ch = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or ch != strs[j][i]:
                return strs[0][:i]

    return strs[0]