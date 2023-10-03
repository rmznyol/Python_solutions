# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        max_until = nums[0]
        for num in nums[1:]:
            max_until = max(max_until + num, num)
            global_max = max(max_until,global_max)
        return global_max    

#########################################