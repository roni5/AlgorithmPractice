def modifyString(self, s: str) -> str:

    if len(s) == 1 and s == "?":
        return "a"
    
    options = "abc"
    s = list(s)

    for i in range(len(s)):
        if s[i] == "?":
            for char in options:
                if i == 0 and s[i + 1] != char:
                    s[i] = char
                    break
                elif i == len(s) - 1 and s[i - 1] != char:
                    s[i] = char
                    break
                elif (i > 0 and i < len(s) - 1) and s[i - 1] != char and s[i + 1] != char:
                    s[i] = char
                    break
    
    return "".join(s)