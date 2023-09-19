# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for i in s:
            if i.isalnum():
                clean += i.lower() 
        return clean == clean[::-1]

############################################################

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
############################################################
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
############################################################
# 167. Two Sum II - Input Array Is Sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        right = n - 1
        left = 0
        while True:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum > target:
                right -= 1 
            else:
                left += 1
############################################################
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
############################################################
# 15. 3Sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_dict = {}
        for index in range(len(nums)):
            nums_dict[nums[index]] = index
        results = {}
        l = len(nums)
        if l<3:
            return results
        for i in range(l-2):
            for j in range(i+1,l-1):
                index = nums_dict.get(-nums[i]-nums[j])
                if index!= None and index>j:
                    temp = sorted([nums[i],nums[j],nums[index]])
                    results[(tuple(temp))] = True
        return list(results.keys())
