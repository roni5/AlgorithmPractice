def oneAway(s1, s2):
    frequncy_table = {}

    # If length difference is more than one, automatically False
    if abs(len(s1) - len(s2)) > 1:
        return False

    for letter in s1:
        if letter not in frequncy_table:
            frequncy_table[letter] = 1
        else:
            frequncy_table[letter] += 1

    for letter in s2:
        if letter in frequncy_table:
            frequncy_table[letter] -= 1
        else:  # if the letter is not present in s1, assign -1
            frequncy_table[letter] = -1

    count = 0
    for key, value in frequncy_table.items():
        if count > 1:
            return False
        if value == 1:
            count += 1

    return True

print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bae"))
print(oneAway("pale", "calv"))
print(oneAway("pale", "al"))
