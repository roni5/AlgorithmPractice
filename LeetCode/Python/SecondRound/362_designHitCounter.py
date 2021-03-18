class HitCounter:

    def __init__(self) -> None:

        self.time = [[0,0] for x in range(300)]
    
    def hit(self, timestamp):

        index = (timestamp - 1) % 300
        if self.time[index][0] != timestamp:
            self.time[index][0] = timestamp
            self.time[index][1] = 1
        else:
            self.time[index][1] += 1
    
    def getHits(self, timestamp):
        
        count = 0
        for i in range(len(self.time)):
            if self.time[i][0] > timestamp - 300:
                count += self.time[i][1]
        
        return count