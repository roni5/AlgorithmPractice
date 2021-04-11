def calculate(self, s: str) -> int:

    numSum = 0
    sign = 1
    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            numSum += num * sign
            i -= 1
        elif s[i] == "+":
            sign = 1
        elif s[i] == '-':
            sign = -1
        elif s[i] == "(":
            stack.append(numSum)
            stack.append(sign)
            numSum = 0
            sign = 1
        elif s[i] == ")":
            numSum *= stack.pop()
            numSum += stack.pop()
        i += 1
    return numSum