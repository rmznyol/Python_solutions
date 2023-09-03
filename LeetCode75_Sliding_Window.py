# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = current_sum = sum(nums[:k])
        for i,num in enumerate(nums[k:]):
            current_sum += num - nums[i]
            max_sum = current_sum if current_sum > max_sum else max_sum
        return max_sum / k
##############################################
# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        vowel_count = 0
        for char in s[:k]:
            if char in vowels:
                vowel_count += 1
        max_vowel_count = vowel_count
        for i, char in enumerate(s[k:]):
            if char in vowels:
                vowel_count += 1
            if s[i] in vowels:
                vowel_count -= 1
            max_vowel_count = max([vowel_count,max_vowel_count])
        return max_vowel_count 
##############################################
# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = left = 0
        for i, num in enumerate(nums):
            if num == 0 and k == 0:
                k -= 1
                while left < n and (k < 0):
                    if nums[left] == 0:
                        k += 1
                    left += 1
            else:
                if num == 0:
                    k -= 1
                mx = max([i-left + 1,mx])
        return mx
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
    
