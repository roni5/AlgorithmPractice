def smallestWindow(nums):
    left, right = 0, 0
    maxVal, minVal = -float('inf'), float("inf")
    n = len(nums)

    for i in range(n):
        maxVal = max(maxVal, nums[i])
        if nums[i] < maxVal:
            left = i
    
    for j in range(n - 1, -1, -1):
        minVal = min(minVal, nums[j])
        if nums[j] > minVal:
            right = j
    
    return (min(left, right), max(left, right))

nums1 = [1,2,3]
nums2 = [1,4,3,2,5]
nums3 = [2,1,5,3,4,2]

print(smallestWindow(nums1))
print(smallestWindow(nums2))
print(smallestWindow(nums3))