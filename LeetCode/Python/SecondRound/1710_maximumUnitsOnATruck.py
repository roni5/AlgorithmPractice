def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

    boxTypes.sort(key=lambda x: -x[1])

    totalUnit = 0
    for boxNum, unit in boxTypes:
        if truckSize <= boxNum:
            totalUnit += truckSize * unit
            break
        totalUnit += boxNum * unit
        truckSize -= boxNum
    
    return totalUnit