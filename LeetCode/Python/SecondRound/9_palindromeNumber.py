# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome(n):
    if n == 0:
        return True
    if n < 0:
        return False
    if n % 10 == 0:
        return False
    
    reversedNum = 0
    originalNum = n

    while x > 0:
        reversedNum *= 10
        reversedNum += x % 10
        x = x // 10
    
    if reversedNum == originalNum:
        return True
    else:
        return False