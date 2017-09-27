def selectionSort(arr):

    for slot in range(len(arr)-1 , 0, -1):
        positionMax = 0
        for location in range(0, slot + 1):
            if arr[location] > arr[positionMax]:
                positionMax = location
        temp = arr[slot]
        arr[slot] = arr[positionMax]
        arr[positionMax] = temp

    return arr

print(selectionSort([10,3,100,3,4,1,9,22]))
print(selectionSort([10,3,9,1,4,3,2,11]))