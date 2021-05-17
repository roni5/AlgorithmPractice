def removeDuplicateLetters(self, s: str) -> str:

    lastIndex = defaultdict()
    for idx, letter in enumerate(s):
        lastIndex[letter] = idx
    
    seen = set()
    stack = []

    for idx, letter in enumerate(s):
        if letter not in seen:
            while stack and stack[-1] > letter and idx < lastIndex[stack[-1]]:
                seen.discard(stack.pop())
            seen.add(letter)
            stack.append(letter)
    
    return "".join(stack)
    