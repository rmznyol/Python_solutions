######################################################################
# 55. Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums[:-1]):
            if num == 0:
                j = 0
                while nums[i-j] <= j:
                    j += 1
                    if j > i:
                        return False
        return True
######################################################################
