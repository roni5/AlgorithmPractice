def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

    horizontalCuts.sort()
    verticalCuts.sort()

    horizontalCuts = [0] + horizontalCuts
    verticalCuts = [0] + verticalCuts

    horizontalCuts.append(h)
    verticalCuts.append(w)

    maxHeight = 0
    maxWidth = 0

    for i in range(1, len(horizontalCuts)):
        maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1])
    
    for i in range(1, len(verticalCuts)):
        maxWidth = max(maxWidth, verticalCuts[i]- verticalCuts[i - 1])
    
    return maxHeight * maxWidth % 100000007

