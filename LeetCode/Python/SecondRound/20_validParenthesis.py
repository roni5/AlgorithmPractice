# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

def isValid(s):
    
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    
    dic = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    stack = []

    for letter in s:
        if letter in dic:
            stack.append(dic[letter])
        else:
            if len(stack) == 0 or letter != stack.pop():
                return False
    
    return True if len(stack) == 0 else False
    
