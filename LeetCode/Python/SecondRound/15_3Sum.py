def threeSum(self, nums: List[int]) -> List[List[int]]:

    if len(nums) < 3:
        return []
    
    ans = []
    nums.sort()

    for i in range(len(nums) - 2):

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:

            threeSum = nums[i] + nums[left] + nums[right]

            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                ans.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
                
        return ans