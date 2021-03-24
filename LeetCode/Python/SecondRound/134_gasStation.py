def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

    total = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
    
    if total < 0:
        return -1
    else:
        tank = 0
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        
        return start