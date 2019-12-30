def isAlienSorted(words, order):
    map = [0 for x in range(26)]

    for i, c in enumerate(order):
        map[ord(c) - ord('a')] = i
    
    for i in range(1, len(words)):
        if compare(word[i - 1], word[i], map) > 0 :
            return False
    return True

def compare(word1, word2, map):
    i = 0
    j = 0
    compare_val = 0

    while i < len(word1) and j < len(word2) and compare_val == 0:
        compare_val = map[ord(word1[i]) - ord('a')] - map[ord(word2[j])- ord('a')]
        i += 1
        j += 1
    
    if compare_val == 0:
        return len(word1) - len(word2)
    else:
        return compare_val
