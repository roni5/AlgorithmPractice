from collections import Counter

def isPermuOfPalindrome(s):

    s = s.lower().replace(" ", "")
    counter = Counter()
    for letter in s:
        counter[letter] += 1

    if len(s) % 2 == 0:
        for letter in counter:
            if counter[letter] % 2 != 0:
                return False
        return True
    else:
        odd_count = 0
        for letter in counter:
            if counter[letter] % 2 != 0:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True

print(isPermuOfPalindrome("Tact Coa"))