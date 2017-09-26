def stringCompression(s):
    repeated = 1
    last_char = s[0]
    returnString = ""
    for i in range(1, len(s)):
        if s[i] == last_char:
            repeated += 1
        else:
            returnString += createString(last_char, repeated)
            repeated = 1
            last_char = s[i]

    # Must add the remaining string and repeated after for loop
    returnString += createString(last_char, repeated)

    return returnString

def createString(s, repeated):

    return s + str(repeated)

print(stringCompression("aabcccccaaa"))
