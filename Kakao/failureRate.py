def failureRate(stages, n):
    answer = []
    players = len(stages)
    fail = {}

    for stage in stages:
        if stage <= 5:
            if stage not in fail:
                fail[stage] = [0,0,0]
                fail[stage][0] = 1
            else:
                fail[stage][0] += 1

    for stage in range(1, n + 1):
        if stage not in fail:
            fail[stage] = [0,0,0]
        else:
            if stage <= 1:
                fail[stage][1] = players
            else:
                fail[stage][1] = fail[stage - 1][1] - fail[stage - 1][0]

            try:
                fail[stage][2] = fail[stage][0] / fail[stage][1]
            except: 
                fail[stage][2] = 0

    for i in sorted(fail.items(), key = lambda kv: (kv[1][2], kv[1]), reverse = True):
        answer.append(i[0])

    return answer

print(failureRate([1,3,5,6,3,2,2], 5))
    
