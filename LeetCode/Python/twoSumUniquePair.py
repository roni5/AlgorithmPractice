def uniquePairs(nums, target):
    num_set = set()
    seen = set()
    count = 0

    for num in nums:
        lookFor = target - num
        if lookFor in num_set and num not in seen:
            count += 1
            seen.add(lookFor)
            seen.add(num)
        elif num not in num_set:
            num_set.add(num)
    
    return count

print(uniquePairs([1, 5,1,5], 47))