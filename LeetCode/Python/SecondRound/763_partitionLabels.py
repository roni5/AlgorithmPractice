def partitionLabels(self, S: str) -> List[int]:
    
    if not S:
        return None
    
    lastIndices = self.getLastIndices(S)
    start = 0
    end = 0
    res = []

    for idx, letter in enumerate(S):
        end = max(end, lastIndices[letter])
        if idx == end:
            res.append(end - start + 1)
            start = end + 1
    
    return res
    
def getLastIndices(self, s):

    lastIndices = defaultdict()
    for idx, letter in enumerate(s):
        lastIndices[letter] = idx
    
    return lastIndices