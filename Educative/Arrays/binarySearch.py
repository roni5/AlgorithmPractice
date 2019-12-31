def binarySearch_rec(array, key, low, high):
    if low > high:
        return -1
    
    mid = low + ((high - low) // 2)

    if array[mid] == key:
        return mid
    elif key < a[mid]:
        return binarySearch_rec(array, key, low, mid -1)
    else:
        return binarySearch_rec(array, key, mid + 1, high)

def binarySearch(array, key):

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1