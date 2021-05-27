def leastInterval(self, tasks: List[str], n: int) -> int:

    freq = [0] * 26
    for task in tasks:
        freq[ord(task) - ord('A')] += 1
    
    freq.sort()
    maxFreq = freq[-1]
    idleSlots = (maxFreq - 1) * n

    for i in range(24, -1, -1):
        idleSlots -= min(freq[i], maxFreq - 1)
    
    return idleSlots + len(tasks) if idleSlots > 0 else len(tasks)
    