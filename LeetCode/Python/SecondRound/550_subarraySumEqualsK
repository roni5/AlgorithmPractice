def subarraySum(self, nums: List[int], k: int) -> int:

    map = {0:1}
    counter = 0
    currentSum = 0

    for num in nums:
        currentSum += num
        if currentSum - k in map:
            counter += map[currentSum - k]
        map[currentSum] = map.get(currentSum, 0) + 1

    return counter