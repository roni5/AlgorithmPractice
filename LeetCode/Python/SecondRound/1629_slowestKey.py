def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:

    longest = keysPressed[0]
    maxDuration = releaseTimes[0]

    for i in range(1, len(releaseTimes)):
        duration = releaseTimes[i] - releaseTimes[i - 1]
        if duration >= maxDuration:
            if duration == maxDuration:
                if keysPressed[i] > longest:
                    longest = keysPressed[i]
            else:
                longest = keysPressed[i]
            maxDuration = duration
    
    return longest