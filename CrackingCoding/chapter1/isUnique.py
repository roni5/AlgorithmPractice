def isUnique(s):
    if len(s) > 128:
        return False

    check = [False] * 128

    for letter in s:
        idx = ord(letter)
        if check[idx] == True:
            return False
        else:
            check[idx] = True

    return True

test = "abcdefghijklmnopqrstuvwxyzABCDEFG"
test2 = "abcddegsdfgshglk;sdflnfdlfwelkndzlknf"

print("isUnique:", isUnique(test))
print("isUnique:", isUnique(test2))