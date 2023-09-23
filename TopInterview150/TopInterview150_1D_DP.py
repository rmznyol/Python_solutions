# 70. Climbing Stairs

class Solution:
    cache = {1:1, 2:2, 3:3}
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.cache[n]
############################################################
# 198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0,0]+[nums[0] for _ in nums]
        last_house_is_robbed = True
        for i, current_house in enumerate(nums[1:],3):
            if not last_house_is_robbed:
                dp[i] = dp[i - 1] + current_house
                last_house_is_robbed = True
            elif dp[i - 2] + current_house > dp[i-1]:
                dp[i] = dp[i - 2] + current_house
                last_house_is_robbed = True
            else:
                dp[i] = dp[i-1]
                last_house_is_robbed = False
        return dp[-1]
############################################################
# 139. Word Break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {word:True for word in wordDict}
        def res(s):
            if s in memo:
                return memo[s]
            for word in wordDict:
                l = len(word)
                if s[-l:] == word and res(s[:-l]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False

        return res(s)
############################################################
#322. Coin Change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = {coin:1 for coin in coins}
        def helper(amount):
            if amount in coins_set:
                return coins_set[amount]
            remaining = []
            for coin in coins:
                if amount - coin > 0:
                    curr = helper(amount - coin)
                    if curr > -1:
                        remaining.append(curr)
            if remaining:
                coins_set[amount] = 1 + min(remaining)
            else:
                coins_set[amount] = -1
            return coins_set[amount]
        return helper(amount) if amount > 0 else 0
############################################################
# 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] longest increasing subsequence ending at nums[i]
        dp = [1 for _ in nums]
        n = len(nums)
        mx = 1
        for i in range(1,n):
            longest_seqeunces = [1+ dp[i-j] for j in range(1,i+1) if nums[i] > nums[i-j]]
            dp[i] = max(longest_seqeunces) if longest_seqeunces else 1
            mx = max(dp[i],mx)
        # max(dp) = longest increasing subsequence
        return mx