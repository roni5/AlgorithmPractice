def sortColors(self, nums: List[int]) -> None:

    if not nums or len(nums) == 1:
        return

    start = 0
    end = len(nums) - 1
    idx = 0

    while idx <= end:
        if nums[idx] == 0:
            nums[idx], nums[start] = nums[start], nums[idx]
            start += 1
            idx += 1
        elif nums[idx] == 2:
            nums[idx], nums[end] = nums[end], nums[idx]
            end -= 1
        else:
            idx += 1
            