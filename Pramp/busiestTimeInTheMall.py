def findBusiestTime(data):
    count = 0
    currentMaxPeople = float('-inf')
    maxTime = 0

    for i in range(len(data)):
        enter = True if data[i][2] == 1 else False
        time = data[i][0]
        customerNum = data[i][1]

        if enter:
            count += customerNum
        else:
            count -= customerNum

        if i < len(data) - 1 and time == data[i + 1][0]:
            continue

        if count > currentMaxPeople:
            currentMaxPeople = count
            maxTime = time
    
    return maxTime
        


