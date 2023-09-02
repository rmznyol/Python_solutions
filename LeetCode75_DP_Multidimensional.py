# 1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for char in text1] for char in text2]
        n = len(text1)
        m = len(text2)
        dp[0][0] = 1 if text1[0] == text2[0] else 0
        for j in range(n):
            dp[0][j] = 1 if text1[j] == text2[0] else dp[0][j-1]
        for i in range(m):
            dp[i][0] = 1 if text1[0] == text2[i] else dp[i-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if text2[i] == text1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m-1][n-1]
######################################################################