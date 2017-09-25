# 217
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
def containsDuplicate(arr):
    seen = {}
    for number in arr:
        if number not in seen:
            seen[number] = 1
        else:
            return True
    return False

def containsDuplicate(arr):
    return len(arr) > len(set(arr))

