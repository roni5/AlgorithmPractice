def longestCommonPrefix(self, strs: List[str]) -> str:

    if not strs:
        return ""

    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[: len(prefix) - 1]
            if len(prefix) == 0:
                return ""
    
    return prefix