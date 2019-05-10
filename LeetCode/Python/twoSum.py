def twoSum(self, nums: List[int], target: int) -> List[int]:
    dict = {}

    for idx, num in enumerate(nums):
        diff = target - num
        if dict.get(diff) is not None:
            return [dict.get(diff), idx]
        dict[num] = idx