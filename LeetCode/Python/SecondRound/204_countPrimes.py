def countPrimes(self, n: int) -> int:

    if n < 2:
        return 0

    table = [True for x in range(n)]
    table[0] = False
    table[1] = False

    count = 0
    for i in range(2, len(table)):
        if table[i]:
            count += 1
            for j in range(i * 2, len(table), i):
                if table[j]:
                    table[j] = False
    
    return count

