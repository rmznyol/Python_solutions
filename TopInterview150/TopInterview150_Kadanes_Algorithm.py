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
# 918. Maximum Sum Circular Subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = global_max = max_ending = global_min = min_ending = nums[0]
        for num in nums[1:]:
            max_ending = max(num, num + max_ending)
            min_ending = min(num, num + min_ending)
            global_max = max(max_ending,global_max)
            global_min = min(min_ending,global_min)
            total += num
        return max(global_max, total - global_min) if total != global_min else global_max
