def maxScore(self, cardPoints: List[int], k: int) -> int:

    total = sum(cardPoints)
    windowSize = len(cardPoints) - k
    currSum = sum(cardPoints[:windowSize])
    minSum = currSum

    left = 0
    right = left + windowSize

    for i in range(k):
        currSum += cardPoints[right] - cardPoints[left]
        minSum = min(currSum, minSum)
        left += 1
        right += 1
    
    return total - minSum