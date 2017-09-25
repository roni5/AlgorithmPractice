# Palindrome?
def is_palindrome(s):

    i = 0
    j = len(s) - 1

    while i < j:

        while i < j and not s[i].isalnum():
            i += 1

        while i < j and not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True

print(is_palindrome("Never odd or even!!!!"))

# First N prime numbers
def n_prime_numbers(n):

    for number in range(1, n + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number)

n_prime_numbers(13)

# Given a string(for e.g.,abc) and an array of strings(s1,s2,....sn) -&gt;
# return an array of boolean values based on if a string s1 can be made from the characters of string(abc)
# Permutation!


def perms(word):
    stack = list(word)
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            print('--',w)
            for i in range(len(w) + 1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

print(perms("abc"))

def arrayPerms(word, arr):
    permutations = perms(word)
    result =[]

    for item in arr:
        if item in permutations:
            result.append(True)
        else:
            result.append(False)
    return result

print(arrayPerms("abc", ['bac','aaa','asdd','cab']))


def get_permutations(string):
    # base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = \
        get_permutations(all_chars_except_last)

    # put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_of_all_chars_except_last in \
            permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = permutation_of_all_chars_except_last[:position] + \
                          last_char + permutation_of_all_chars_except_last[position:]
            permutations.add(permutation)

    return permutations

# Remove duplicates in array
def remove_Dup_Array(arr):
    start = 0
    seen = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] not in seen:
            seen.append(arr[i])
    return seen

dup_arr = [1,1,1,2,3,4,4,5,5,6,7]

print("--Remove dup array--", remove_Dup_Array(dup_arr))