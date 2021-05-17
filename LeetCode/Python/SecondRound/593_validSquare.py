def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

    
    if self.isSame(p1,p2) or self.isSame(p1,p3) or self.isSame(p1,p4) or self.isSame(p2,p3) or self.isSame(p2,p4) or self.isSame(p3,p4):
        return False
    
    distances = set()
    distances.add(self.getDistance(p1, p2))
    distances.add(self.getDistance(p1, p3))  
    distances.add(self.getDistance(p1, p4))  
    distances.add(self.getDistance(p2, p3))  
    distances.add(self.getDistance(p2, p4))  
    distances.add(self.getDistance(p3, p4)) 
    
    return len(distances) == 2
    
def getDistance(self, p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def isSame(self, p1, p2):
    return p1[0] == p2[0] and p1[1] == p2[1]