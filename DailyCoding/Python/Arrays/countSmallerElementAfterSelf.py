import bisect
def smallerCounts(nums):
    result = []
    seen = []
    print(f'input is {nums}')
    for num in nums[::-1]:
        position = bisect.bisect_left(seen, num)
        print(f'position for {num} = {position}')
        result.append(position)
        bisect.insort(seen, num)
    
    return list(reversed(result))

nums = [3,4,9,6,1]

print(smallerCounts(nums))
