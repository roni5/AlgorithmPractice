def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(s) < 2:
            return False
        
        stack = []
        dic = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        for ch in s:
            if ch in dic:
                stack.append(dic[ch])
            else:
                if len(stack) == 0 or ch != stack.pop():
                    return False
        
        return True if len(stack) == 0 else False