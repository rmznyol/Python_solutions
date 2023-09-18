# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        for i,num in enumerate(nums):
            if num != 0:
                nums[i] = nums[non_zero_index]
                nums[non_zero_index] = num
                non_zero_index += 1
        return nums
##############################################################
# 392. Is Subsequence

from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0 
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False
##############################################################
# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        max_volume = 0
        while left <= right:
            mn = min([height[left],height[right]])
            volume = mn * (right - left)
            max_volume = volume if volume > max_volume else max_volume  
            if mn == height[left]: #if this is the case you cannot achive higher volume without sliding left pointer to left
                left += 1
            else: #if this is the case you cannot achive higher volume without sliding right pointer to right
                right -= 1
        return max_volume
##############################################################
#1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sum_dict = {}
        for num in nums:
            if sum_dict.get(num):
                sum_dict[num][1] += 1
            else:
                sum_dict[num] = [True, 1]
        result = 0
        for num in nums:
            if sum_dict[num][1]:
                sum_dict[num][1] -= 1
                if sum_dict.get(k-num) and sum_dict[k-num][1]:
                    result += 1
                    sum_dict[k-num][1] -= 1
        return result
