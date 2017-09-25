# Maximum continous sum
def largest_cont_sum(arr):
    if len(arr) == 0:
        raise "Array can't be empty"
    else:
        currentSum = maxSum = arr[0]
        marker = start = end = 0

        for i in range(1, len(arr)):
            if arr[i] > (currentSum + arr[i]):
                currentSum = arr[i]
                marker = i
            else:
                currentSum += arr[i]

            if currentSum > maxSum:
                maxSum = currentSum
                start = marker
                end = i

        return maxSum, start, end
print("largestConSum:", largest_cont_sum([-2, 1, 2, 3, -5, 5, 20]))
print("largestConSum:", largest_cont_sum([-1, -29, -36, -3, -22, -11, -19, -5]))

# Reverse words in sentence
def rev_sen(s):
    start = i = 0
    length = len(s)
    output = []

    while i < length:
        if s[i].isalnum():
            start = i
            while i < length and s[i].isalnum():
                i += 1
            output.insert(0, s[start:i])
        i += 1
    return " ".join(output)

print(rev_sen(" Hello    World"))

binary = bin(6)
count = 0

for letter in binary:
    if letter == "1":
        count += 1
print(count)



