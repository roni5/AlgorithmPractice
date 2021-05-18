def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

    ans = [0] * len(temperatures)
    stack = []

    for idx, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            last = stack.pop()
            ans[last] = idx - last
        stack.append(idx)
    
    return ans