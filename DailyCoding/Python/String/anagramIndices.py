def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]
        print(f'{char} deleted')

def anagramIndices(word, s):
    ans = []
    freq = {}

    for char in word:
        freq[char] = freq.get(char, 0) + 1
    
    for char in s[:len(word)]:
        freq[char] = freq.get(char, 0) - 1
        del_if_zero(freq, char)
    
    if not freq:
        ans.append(0)

    for i in range(len(word), len(s)):
        start_ch = s[i - len(word)]
        end_ch = s[i]
        
        freq[start_ch] = freq.get(start_ch, 0) + 1
        del_if_zero(freq, start_ch)

        freq[end_ch] = freq.get(end_ch, 0) - 1
        del_if_zero(freq, end_ch)

        if len(freq) == 0:
            idx = i - len(word) + 1
            ans.append(idx)

    return ans

print(anagramIndices("ab","bbxaba"))