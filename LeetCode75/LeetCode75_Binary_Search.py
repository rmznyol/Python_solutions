# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 0
        hi = n 
        while lo < hi:
            mid = (lo+hi)//2
            g = guess(mid)
            if g == 0:
                return mid
            elif g > 0:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
###############################################################
#2300. Successful Pairs of Spells and Potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def search(spell,sorted_potions, success):
            lo = 0
            l = len(sorted_potions)
            hi = l - 1
            while lo <= hi:
                mid = (lo + hi)//2
                spelled_potion = spell * sorted_potions[mid]
                #print(mid, spelled_potion)
                if spelled_potion == success:
                    while mid - 1 >= 0 and sorted_potions[mid-1] == sorted_potions[mid]:
                        mid -= 1 
                    return l - mid
                elif spelled_potion > success:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return l - lo 
            #O(nlogn) + O(nlogn)
            #as opposed to O(n^2)
        sorted_potions = sorted(potions)
        results = []
        calculated = {}
        for spell in spells:
            if spell not in calculated:
                number_of_potions = search(spell, sorted_potions,success)
                calculated[spell] = number_of_potions
            results.append(calculated[spell])
        return results
###############################################################
# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0 
        hi = len(nums) - 1
        nums.append(float('-inf'))
        if hi == 0: return 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid+1]:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
###############################################################
# 875. Koko Eating Bananas

class Solution:
    def time_to_eat_all(self, k, piles):
        total = 0
        for pile in piles:
            total += pile // k
            total = total if pile % k == 0 else total + 1
        return total 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            time_in_mid = self.time_to_eat_all(mid,piles)
            if time_in_mid > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo