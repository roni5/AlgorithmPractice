#O(n) in-place reverse string
def reverseString(s:List[str]) -> None:
    last_idx = len(s) - 1
    for idx in range(len(s) // 2):
        temp = s[idx]
        s[idx] = s[last_idx]
        s[last_idx] = temp
        last_idx -= 1
    



