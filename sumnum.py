def sumToOne(num):
    if num < 10:
        return num

    result = 0

    while num > 10:
        result += num % 10
        num = int(num / 10)

    result += num

    temp = 0
    temp += result % 10
    temp += int(result / 10)

    return temp


print(sumToOne(900293))


def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    while (first <= last):
        mid = (first + last) // 2
        if item_list[mid] == item:
            return True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


print(binary_search([1, 2, 3, 5, 8], 10))
print(binary_search([1, 2, 3, 5, 8], 5))


def fact(n):
    if n == 2:
        return 2
    return n * fact(n - 1)


print(fact(5))


def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(8))


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    elif r == 1:
        return 1
    return gcd(b, r)


print(gcd(4, 10))


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def remove(self):
        return self.items.pop()


s = Stack()
s.add(1)
s.add(2)
print(s.peek())


class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self, item):
        return len(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())


def balance_check(user_str):
    openning = set("({[")
    closing = set(")}]")
    stack = []
    match = {('(', ')'), ('[', ']'), ('{', '}')}

    for letter in user_str:
        if len(stack) == 0 and letter in closing:
            return False
        if letter in openning:
            stack.append(letter)
        elif letter in closing:
            last_open = stack.pop()
            if (last_open, letter) not in match:
                return False
    return len(stack) == 0

print(balance_check("adsad[asdads]ad{adsad}(adssad)"))
print(balance_check("assad[adsads{asdad}adsdsa]ad()"))
print(balance_check("assad[adsads{]sdad}adsdsaad()"))


def maxSubArray(ls):
    if len(ls) == 0:
        raise Exception("Array empty")  # should be non-empty

    runSum = maxSum = ls[0]
    i = 0
    start = finish = 0

    for j in range(1, len(ls)):
        if ls[j] > (runSum + ls[j]):
            runSum = ls[j]
            i = j
        else:
            runSum += ls[j]

        if runSum > maxSum:
            maxSum = runSum
            start = i
            finish = j

    print("maxSum =>", maxSum)
    print("start =>", start, "; finish =>", finish)


maxSubArray([-2, 11, -4, 13, -5, 2])
maxSubArray([-15, 29, -36, 3, -22, 11, 19, -5])

def compress_string(user_str):
    last_char = user_str[0]
    repeated = 1
    compressed_string = ""

    for i in range(1, len(user_str)):
        if user_str[i] == last_char:
            repeated += 1
        else:
            compressed_string += last_char + str(repeated)
            repeated = 1
            last_char = user_str[i]
        if i == len(user_str) - 1:
            compressed_string += last_char + str(repeated)

    return compressed_string

print(compress_string("ABBCCCDDDDab11;s"))

def sentence_reverse(sentence):
    words = sentence.split(" ")
    reverse = []
    for i in range(len(words)-1 , -1, -1):
        reverse.append(words[i])

    return " ".join(reverse)

print(sentence_reverse("This is the best"))

def sentence_reverse2(sentence):
    words = []
    length = len(sentence)
    i = 0

    while i < length:
        if sentence[i] is not " ":
            start = i
            while i < length and sentence[i] is not " ":
                i += 1
            words.insert(0,sentence[start:i])
        i += 1

    return " ".join(words)

print(sentence_reverse2("This is the best"))

s = "abc"
print(s[:1])

def lengthof(s):
    seen = set()
    length = 0
    cache = []
    for letter in s:
        if letter not in seen:
            length += 1
            seen.add(letter)
        else:
            cache.append(length)
            length = 1
    return max(cache)

print(lengthof("abcdefabczzzbb"))