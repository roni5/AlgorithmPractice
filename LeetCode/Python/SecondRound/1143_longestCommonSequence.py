def longestCommonSubsequence(self, text1: str, text2: str) -> int:

    if len(text1) == 0 or len(text2) == 0:
        return 0
    
    dp = [[0 for x in range(len(text1) + 1)] for x in range(len(text2) + 1)]

    for t2Row in range(1, len(text2) + 1):
        for t1Col in range(1, len(text1) + 1):
            if text1[t1Col - 1] == text2[t2Row - 1]:
                dp[t2Row][t1Col] = 1 + dp[t2Row - 1][t1Col - 1]
            else:
                dp[t2Row][t1Col] = max(dp[t2Row - 1][t1Col], dp[t2Row][t1Col - 1])
    
    return dp[len(text2)][len(text1)]
    