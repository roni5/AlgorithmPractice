# Does string has all unique char?
def is_unique(word):
    temp = {}
    for letter in word:
        if letter in temp:
            return False
        else:
            temp[letter] = 1
    return True

print('--is unique--',is_unique('abc'))
print('--is unique--',is_unique('aba'))

# Are two string permuation of each other?
def is_permuation(str1, str2):
    if len(str1) != len(str2):
        return False
    temp = {}
    for letter in str1:
        try:
            temp[letter] += 1
        except:
            temp[letter] = 1
    for letter in str2:
        try:
            temp[letter] -= 1
        except:
            return False

    for key, value in temp.iteritems():
        if value != 0:
            return False

    return True

print('--is_permutation--', is_permuation('aaa', 'aaa'))
print('--is_permutation--', is_permuation('aba', 'baa'))
print('--is_permutation--', is_permuation('abaaaa', 'baaaa'))
print('--is_permutation--', is_permuation('12345', '54321'))
print('--is_permutation--', is_permuation('12345', '93521'))

# URLify
def urlify(str):
    return str.replace(" ", "%20")

print('--urlify--', urlify("Mr John Smith"))

#Is is a permutation of palindrome?
def is_permu_palindrome(user_str):
    input_str = user_str.lower().replace(" ","")
    frequency_table = get_frequnecy_dict(input_str)
    return check_odd_char(frequency_table, input_str)

def get_frequnecy_dict(user_str):
    frequency_table = {}
    for letter in user_str:
        try:
            frequency_table[letter] += 1
        except:
            frequency_table[letter] = 1
    return frequency_table

def check_odd_char(frequency_table, user_str):
    if len(user_str) % 2 == 0:  # if even length, each char should be in even
        for key, value in frequency_table.iteritems():
            if value % 2 != 0:
                return False
        return True
    else:  # if odd length, there should be only one odd char
        count = 0
        for key, value in frequency_table.iteritems():
            if value % 2 != 0:
                count += 1
            if count > 1:
                return False
        return True

print('--is_permu_pali--', is_permu_palindrome('Tact Coa'))

# One edit away
def one_away(str1, str2):
    lower_str1 = str1.lower()
    lower_str2 = str2.lower()
    if abs(len(lower_str1) - len(lower_str2)) > 1:
        return False
    else:
        str1_table = get_frequnecy_dict(lower_str1)
        for letter in lower_str2:
            try:
                str1_table[letter] -= 1
            except:
                str1_table[letter] = -1
        count = 0
        for key, value in str1_table.iteritems():
            if value >= 1:
                count += 1
            if count > 1:
                return False
    return True
print('--one_edit--', one_away('pale', 'ple'))
print('--one_edit--', one_away('pales', 'pale'))
print('--one_edit--', one_away('pale', 'bale'))
print('--one_edit--', one_away('pale', 'bake'))

