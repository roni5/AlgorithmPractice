def longestConsecutive(self, nums: List[int]) -> int:

    numSet = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in numSet:
            currentNum = num
            currentSequence = 1

            while currentNum + 1 in numSet:
                currentNum += 1
                currentSequence += 1
            
            longest = max(longest, currentSequence)
    
    return longest