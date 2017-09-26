# 125
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s) - 1

    while i <= j:

        while i <= j and not s[i].isalnum():
            i += 1

        while i <= j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True