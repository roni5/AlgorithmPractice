def sumZero(self, n: int) -> List[int]:

    if n == 0:
        return []
    if n == 1:
        return [0]

    ans = []
    if n % 2 != 0:
        ans.append(0)


    for i in range(1, (n //2 ) + 1):
        ans.append(i)
        ans.append(i * -1)

    return ans