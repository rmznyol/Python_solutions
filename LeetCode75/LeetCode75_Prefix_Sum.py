# 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = mx = 0
        for diff in gain:
            alt += diff
            mx = max([alt,mx]) if diff > 0 else mx
        return mx
##########################################
# 724. Find Pivot Index

from itertools import accumulate
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = [0] + list(accumulate(nums))
        right_sum = list(accumulate(nums[::-1]))[::-1] + [0]
        for i in range(1,len(nums)+1):
            if left_sum[i-1] == right_sum[i]:
                return i-1
        else:
            return -1
