# 20
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    openning = ["(", "{", "["]
    closing = [")", "}", "]"]
    stack = []
    match = {('(', ')'), ('{', '}'), ('[', ']')}

    if s[0] in closing or len(s) == 1:
        return False

    for letter in s:
        if letter in openning:
            stack.append(letter)
        elif letter in closing:
            if len(stack) == 0 or (stack.pop(), letter) not in match:
                return False

    return len(stack) == 0
