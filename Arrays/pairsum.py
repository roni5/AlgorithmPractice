


def pairSum (array, value):
    answer = []
    for i in range(len(array)):
        if i == len(array) - 1:
            break
        if array[i] + array[i+1] == value:
            if [array[i], array[i+1]] not in answer:
                answer.append([array[i], array[i+1]])

    print(len(answer))
    print(answer)


pairSum([1,3,2,2,2,2,2,2,2,10,3,1], 4)

