def insertionSort(arr):

    for i in range(1, len(arr)):

        currentValue = arr[i]
        position = i

        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position-1]
            position -= 1

        arr[position] = currentValue

    return arr

print(insertionSort([10,3,9,1,4,3,2,11]))

def bubbleSort(arr):

    for i in range(len(arr) - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubbleSort([10,3,9,1,4,3,2,11]))

def selectionSort(arr):

    for i in range(len(arr) - 1, 0, -1):
        maxPosition = 0
        for j in range(0, i + 1):
            if arr[j] > arr[maxPosition]:
                maxPosition = j

        arr[i], arr[maxPosition] = arr[maxPosition], arr[i]

    return arr
print(selectionSort([10,3,9,1,4,3,2,11]))

def insertionSort2(arr):

    for i in range(1, len(arr)):
        position = i
        currentValue = arr[i]

        while position > 0 and arr[position - 1] > currentValue:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = currentValue

    return arr
print(insertionSort2([10,3,9,1,4,3,2,11]))