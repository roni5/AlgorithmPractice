def minCost(self, s: str, cost: List[int]) -> int:
    minCost = 0
    groupCost = 0
    groupMax = 0

    for i in range(len(s)):
        if i > 0 and s[i] != s[i - 1]:
            minCost += groupCost - groupMax
            groupCost = 0
            groupMax = 0

        groupCost += cost[i]
        groupMax = max(groupMax, cost[i])
    
    #for the last remaining chars
    minCost += groupCost - groupMax

    return minCost