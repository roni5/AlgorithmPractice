# 461
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    binary = bin(x ^ y)
    count = 0
    for letter in binary:
        if letter == "1":
            count += 1
    return count
