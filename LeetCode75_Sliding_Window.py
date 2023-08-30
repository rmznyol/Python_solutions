############################################## 
# 1493. Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        mx = 0
        used0 = False
        last_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if used0:
                    left = last_zero + 1
                else:
                    used0 = True
                last_zero = i 
            mx = i - left if i - left > mx else mx 
        return mx  
