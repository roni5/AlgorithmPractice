def minRemoveToMakeValid(self, s: str) -> str:

    s = self.delete_paren(s, "(", ")")
    s = self.delete_paren(s[::-1], ")", "(")

    return s[::-1]

def delete_paren(self, s, opening, closing):
    open = 0
    sb = []

    for ch in s:
        if ch == opening:
            open += 1
        if ch == closing:
            if open == 0:
                continue
            open -= 1
        sb.append(ch)
    
    return "".join(sb)