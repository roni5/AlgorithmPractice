# Reverse words in a sentence

sentence = "Hello Python World"
def reverse_words_sentence(sentence):
    return_setence = []
    word = []

    for letter in sentence:
        if letter != " ":
            word.append(letter)
        else:
            temp = "".join(word)
            return_setence.insert(0, temp)
            word = []

    temp = "".join(word)
    return_setence.insert(0, temp)

    return " ".join(return_setence)

print(reverse_words_sentence(sentence))

# Palindrome in-place

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


print(is_palindrome("Never odd or even!!!!!!"))
