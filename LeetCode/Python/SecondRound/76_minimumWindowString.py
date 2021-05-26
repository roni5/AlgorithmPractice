import collections
def minWindow(self, s: str, t: str) -> str:

    freq = collections.Counter(t)
    left = 0
    right = 0
    minLength = len(s)
    found = False
    charToFind = len(freq)

    i = 0
    j = 0
    while j < len(s):
        endChar = s[j]
        j += 1
        if endChar in freq:
            freq[endChar] -= 1
            if freq[endChar] == 0:
                charToFind -= 1
        
        if charToFind > 0:
            continue

        while charToFind == 0:
            startChar = s[i]
            i += 1
            if startChar in freq:
                freq[startChar] += 1
                if freq[startChar] > 0:
                    charToFind += 1
        
        if j - i < minLength:
            left = i
            right = j
            minLength = j - i
            found = True

    
    return s[left - 1 : right] if found else ""