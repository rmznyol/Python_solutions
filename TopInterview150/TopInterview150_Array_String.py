# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = 0
        i2 = 0
        if not nums1: return nums2
        if not nums2: return nums1
        while i1 < m:
            # print(nums1,i1)
            # print(nums2)
            # print(nums1[i1],nums2[i2], nums1[i1] > nums2[i2])
            if nums1[i1] > nums2[i2]:
                temp = nums1[i1]
                nums1[i1] = nums2[i2]
                nums2[i2] = temp
            while i2 < n - 1 and nums2[i2] > nums2[i2 + 1]:
                temp = nums2[i2]
                nums2[i2] = nums2[i2+1]
                nums2[i2+1] = temp
                i2 += 1
            i2 = 0
            # print(i2)
            i1 += 1
        
        nums1[m:] = nums2
######################################################################
# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        sz = len(nums)
        index = 0 

        for i in range(sz):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1 

        return index
######################################################################
# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sz = len(nums)
        index = 0

        for i in range(1,sz):
            if nums[i] != nums[i-1]:
                index += 1
                nums[index] = nums[i]
        
        return index+1
######################################################################
# 80. Remove Duplicates from Sorted Array II
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        n = len(nums)
        count = 1
        for fast in range(1,n):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow += 1
                count = 1
            elif count:
                nums[slow] = nums[fast]
                slow +=1
                count -= 1 
        return slow  
    
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
