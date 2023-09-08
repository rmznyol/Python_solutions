# 338. Counting Bits

class Solution:
    def count1(self,i: int) -> int:
        s = str(bin(i))[2:]
        return sum([int(i) for i in s])
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.count1(i))
        return result
############################################################
# 136. Single Number

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        for num in nums:
            if 1 == c.get(num):
                return num
        return nums[0]
############################################################
#1318. Minimum Flips to Make a OR b Equal to c

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a = bin(a)[-1:1:-1]
        bin_b = bin(b)[-1:1:-1]
        bin_c = bin(c)[-1:1:-1]
        last_place = max(len(bin_a),len(bin_c),len(bin_b))
        bin_a = bin_a + '0'* (last_place - len(bin_a))
        bin_b = bin_b + '0'* (last_place - len(bin_b))
        bin_c = bin_c + '0'* (last_place - len(bin_c))

        i = 0
        count = 0

        for i in range(last_place):
            if bin_c[i] == '0' and '1' in [bin_a[i],bin_b[i]]:
                count += 1
                if bin_a[i] == '1' and bin_b[i] == '1':
                    count += 1
            elif bin_c[i] == '1' and bin_a[i] == '0' and bin_b[i] == '0':
                count += 1
        return count