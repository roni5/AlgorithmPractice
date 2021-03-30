def maxSlidingWindow(nums, k):

    output = []
    queue = deque()
    left = 0
    right = 0

    while right < len(nums):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        
        queue.append(right)

        if left > queue[0]:
            queue.popleft()
        
        if right + 1 >= k:
            output.append(nums[queue[0]])
            left += 1
        
        right += 1

    return output