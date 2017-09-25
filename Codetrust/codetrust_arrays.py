# BINARY SEARCH

arr = [1, 2, 3, 4, 5, 6, 7, 8]

def rec_binary_search(a, value, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == value:
        return mid
    elif value < a[mid]:
        return rec_binary_search(arr, value, low, mid - 1)
    else:
        return rec_binary_search(arr, value, mid + 1, high)


def binary_search(a, value):
    return rec_binary_search(a, value, 0, len(a) - 1)


print("--binary search recursion-",binary_search(arr, 10))

def binary_search_iter(a, value):
    if value < a[0] or value > a[len(a)-1]:
        return -1

    low = 0
    high = len(a) - 1

    while low <= high:
        mid = (low + high) // 2
        if a[mid] == value:
            return mid
        elif value < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print("--binary iter--",binary_search_iter(arr, 8))

def binary(a, value):
    if value < a[0] or value > a[len(a)-1]:
        return -1

    low = 0
    high = len(a) - 1

    while low <=  high:
        mid = (low + high) //2
        if a[mid] == value:
            return mid
        elif value < a[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1

# Rotate array in place (positive for right / negative for left)

def rotate_array(arr, n):
    arr_len = len(arr)
    n = n % arr_len
    if n < 0:
        n += arr_len

    arr = reverse_array(arr, 0, arr_len - 1)
    arr = reverse_array(arr, 0, n - 1)
    arr = reverse_array(arr, n, arr_len - 1)

    return arr

def reverse_array(arr, begin, end):
    while begin < end:
        temp = arr[begin]
        arr[begin] = arr[end]
        arr[end] = temp
        begin += 1
        end -= 1
    return arr

print("---rotate array by -2**", rotate_array(arr, -9))
print("---rotate array by 4**", rotate_array(arr, 4))

# Find low and high index of occurence of a key in array

def findlowhigh(arr, key):
    low = findlow(arr, key)
    high = findhigh(arr, key)
    return (low, high)

def findlow(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if arr[low] == key:
        return low

    return -1

def findhigh(arr,key):
    low = 0
    high = len(arr) - 1


    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if arr[high] == key:
        return high

    return -1
arr2 = [1, 2, 3, 4, 4, 4, 4, 4,  5, 6, 7, 7]
print("--low and high --", findlowhigh(arr2, 4))

# Find smallest common value in sorted arrays

def findSmallestCommon(arr1, arr2, arr3):
    i = 0
    j = 0
    k = 0

    while i < len(arr1) and j < len(arr2) and k < len(arr3):

        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            return arr[i]

        if arr1[i] < arr2[j] and arr1[i] < arr3[k]:
            i += 1
        elif arr2[j] < arr1[i] and arr2[j] < arr3[k]:
            j += 1
        elif arr3[k] < arr2[j] and arr3[k] < arr1[i]:
            k += 1

    return -1

