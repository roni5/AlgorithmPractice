def findCelebrity(self, n: int) -> int:

    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    
    if self.isCelebrity(candidate, n):
        return candidate
    
    return -1

def isCelebrity(self, candidate, n):
    
    for i in range(n):
        if i == candidate:
            continue
        if knows(candidate, i) or not knows(i, candidate):
            return False
    
    return True