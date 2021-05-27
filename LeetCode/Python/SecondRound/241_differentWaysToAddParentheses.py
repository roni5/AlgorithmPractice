def diffWaysToCompute(self, expression: str) -> List[int]:

    res = []
    for i in range(len(expression)):
        c = expression[i]
        if c in "+-*":
            left = self.diffWaysToCompute(expression[:i])
            right = self.diffWaysToCompute(expression[i + 1:])

            for l in left:
                for r in right:
                    if c == "+":
                        res.append(l + r)
                    if c == "*":
                        res.append(l * r)
                    if c == "-":
                        res.append(l - r)
    
    if len(res) == 0:
        res.append(int(expression))
    
    return res