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
    temp += int(result/10)

    return temp

print(sumToOne(9))


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