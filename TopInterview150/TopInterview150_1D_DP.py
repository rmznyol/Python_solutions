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
        