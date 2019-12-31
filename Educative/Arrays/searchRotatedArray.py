# Search for a given number in a sorted array that has been rotated by some arbitrary number. Return -1 if the number does not exist. Assume that the array does not contain duplicates.
# Runtime Complexity #
# Logarithmic, O(logn).

# Memory Complexity #
# Logarithmic, O(logn).

def searchRoatedArray(arr, key):
    low = 0
    high = len(arr) - 1
    if low > high:
        return -1
    
    while low <= high:
        mid = low + ((high - low) // 2)

        if arr[mid] == key:
            return mid
        if arr[mid] <= arr[end] and
             arr[key] >= arr[mid] and
             arr[key] <= arr[end]:
             low = mid + 1
        elif arr[low] <= arr[mid] and
             arr[key] >= arr[low] and
             arr[key] <= arr[mid]:
             high = mid - 1
        elif arr[low] >= arr[mid]:
            high = mid - 1
        elif arr[end] <= arr[mid]:
            low = mid + 1
    
    return -1