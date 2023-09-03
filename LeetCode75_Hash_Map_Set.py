# 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [set(nums1),set(nums2)]
        nums = nums1 if len(nums1)>len(nums2) else nums2
        for num in nums:
            if num in answer[0] and num in answer[1]:
                answer[0].remove(num)
                answer[1].remove(num)
        return answer
####################################################
# 1207. Unique Number of Occurrences

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr).values()
        return len(c) == len(set(c))
####################################################
# 1657. Determine if Two Strings Are Close

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        c1 = Counter(Counter(word1).values())
        c2 = Counter(Counter(word2).values())
        for num,freq in c1.items():
            if c2[num] != freq:
                return False 
        return True
####################################################
# 2352. Equal Row and Column Pairs

from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        on_call = defaultdict(int)
        n = len(grid)
        for row in grid:
            on_call[tuple(row)] += 1
        count = 0
        for j in range(n):
            col = tuple(grid[i][j] for i in range(n))
            count += on_call[tuple(grid[i][j] for i in range(n))]
        return count
