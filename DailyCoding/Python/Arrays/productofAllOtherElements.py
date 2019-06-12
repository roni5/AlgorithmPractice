def productOfAllOtherElements(nums):
    L = [1 for x in nums]
    R = [1 for x in nums]
    ans = [1 for x in nums]

    L[0] = 1
    for i in range(1, len(nums)):
        L[i] = L[i - 1] * nums[i - 1]
    
    R[len(nums) - 1] = 1
    for i in range(len(nums) - 2, -1, -1):
        R[i] = R[i + 1] * nums[i + 1]
    
    for i in range(len(nums)):
        ans[i] = L[i] * R[i]
    
    return ans

nums = [3,2,1]
print(productOfAllOtherElements(nums))
