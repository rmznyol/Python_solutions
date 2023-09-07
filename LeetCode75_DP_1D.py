# N-th Tribonacci Number

from functools import lru_cache
class Solution:
    
    @lru_cache(maxsize = 20)
    def tribonacci(self, n: int) -> int:
        base = {0:0,1:1,2:1}
        if n in base:
            return base[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    
    # def tribonacci(self, n: int, lookup = {0:0,1:1,2:1}) -> int:
    #     print(n,lookup,id(lookup))
    #     if n in lookup:
    #         return lookup[n]
    #     lookup[n] = self.tribonacci(n-1,lookup) + self.tribonacci(n-2,lookup) + self.tribonacci(n-3,lookup)
    #     return lookup[n]

######################################################################
#746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1:
            return 0
        cost_from = cost[-2:]
        for current_cost in cost[-3::-1]:
            cost_from_current_cost = current_cost + min(cost_from)
            cost_from = [cost_from_current_cost,cost_from[0]]
        return min(cost_from)
######################################################################
#198. House Robber

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
######################################################################
# 790. Domino and Tromino Tiling

class Solution:
    def numTilings(self, n: int) -> int:
        dp = [2 for _ in range(n+1)]
        dp[:2] = [0,1,2]
        rolling_sum = 1
        prev, tail = 2, 0
        for i in range(3,n+1):
            rolling_sum += dp[i-1] + dp[i-3]
            dp[i] += rolling_sum
        return dp[n] % (10**9 + 7)

