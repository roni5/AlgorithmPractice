# Given an arbitrary ransom note string and another string containing letters from all the magazines, 
# write a function that will return true if the ransom note can be constructed from the magazines; otherwise, 
# it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

def canConstruct(ransomNote, magazine):
    dic = dict()

    for letter in magazine:
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1
    
    for letter in ransomNote:
        if letter in dic:
            dic[letter] -= 1
            if dic[letter] < 0:
                return False
        else:
            return False
    
    return True