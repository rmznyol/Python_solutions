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
# 714. Best Time to Buy and Sell Stock with Transaction Fee
    
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0
        # hold = profit you made until i-1 by being in hold state at i-1 
        # free = profit you made until i-1 by being in sold state at i-1
        for i in range(1, n):
            hold, free = max(hold, free - prices[i]), max(free, hold + prices[i] - fee)
        return free

######################################################################
# 72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word2), len(word1)
        if not m: return n
        if not n: return m
        dp = [[i + j if i == 0 or j == 0 else 0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
        # for row in dp:
        #     print(row)
        return dp[m][n]
        # def rec(word1, word2):
        #     if word1 == word2:
        #         return 0
        #     if word1 == '': return len(word2)
        #     if word2 == '': return len(word1)
        #     if word1[-1] == word2[-1]:
        #         return rec(word1[:-1],word2[:-1])
        #     return min([rec(word1[:-1],word2[:-1]), rec(word1,word2[:-1]), rec(word1[:-1],word2)]) + 1
        # return rec(word1,word2)