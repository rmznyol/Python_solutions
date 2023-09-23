# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results = []
        n = len(nums)
        j = 0 
        while j < n:
            i = 0 
            while j+i+1 < n and nums[i+j] + 1 == nums[i+j+1]:
                i += 1 
            rng = f'{nums[j]}' if i==0 else f'{nums[j]}->{nums[i+j]}'
            j += i + 1
            results.append(rng)
        return results
#################################################
# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i:i+2] = [[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]]
            else:
                i += 1
            # print(intervals)
        return intervals 

#################################################
       