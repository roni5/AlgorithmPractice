# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

def validPalindrome(s):
    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i] != s[j]:
            return isPalindrome(s, i + 1, j) or isPalindrome(s, i, j - 1)
        i += 1
        j -= 1
    
    return True

def isPalindrome(s, i, j):
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True