def isAnagram(self, s: str, t: str) -> bool:
    counter1, counter2 = {}, {}

    if len(s) != len(t):
        return False

    for letter in s:
        counter1[letter] = counter1.get(letter, 0) + 1
    for letter in t:
        counter2[letter] = counter2.get(letter, 0) + 1
    
    return counter1 == counter2