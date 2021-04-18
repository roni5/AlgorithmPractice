 def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if not wordsDict:
            return 0
        
        idx1 = -1
        idx2 = -1
        minDistance = len(wordsDict)
        
        for i, letter in enumerate(wordsDict):
            if letter == word1:
                idx1 = i
            elif letter == word2:
                idx2 = i
            
            if idx1 != -1 and idx2 != -1:
                minDistance = min(minDistance, abs(idx1 - idx2))
        
        return minDistance