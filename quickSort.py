import random

def sort(nums):
    start = 0
    end = len(nums) - 1
    quickSort(nums, start, end)
    return nums

def quickSort(nums, start, end):
    if start >= end:
        return nums
    
    randomPivot = random.randint(start, end + 1)
    randomPivot = partition(nums, start, end, randomPivot)
    quickSort(nums, start, randomPivot -1)
    quickSort(nums, randomPivot + 1, end)

def partition(nums, start, end, pivot):
    
    nums[end], nums[pivot] = nums[pivot], nums[end]

    j = start
    for i in range(start, end):
        if nums[i] < nums[end]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    nums[end], nums[j] = nums[j], nums[end]

    return j


print(sort([3,3,1,2,5,0,3,10,9]))