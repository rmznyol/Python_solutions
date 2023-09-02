# N-th Tribonacci Number

from functools import lru_cache
class Solution:
    
    @lru_cache(maxsize = 20)
    def tribonacci(self, n: int) -> int:
        base = {0:0,1:1,2:1}
        if n in base:
            return base[n]
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    
    # def tribonacci(self, n: int, lookup = {0:0,1:1,2:1}) -> int:
    #     print(n,lookup,id(lookup))
    #     if n in lookup:
    #         return lookup[n]
    #     lookup[n] = self.tribonacci(n-1,lookup) + self.tribonacci(n-2,lookup) + self.tribonacci(n-3,lookup)
    #     return lookup[n]

######################################################################

######################################################################

######################################################################

######################################################################