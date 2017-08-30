def primeTest(num):

    if num == 1 or num == 2:
        return True

    for i in range (2, num):
        if (num % i == 0):
            return False

    return True


print(primeTest(21))