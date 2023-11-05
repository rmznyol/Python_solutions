# 383. Ransom Note

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for i in ransomNote:
            if c.get(i):
                c[i] -= 1
            else:
                return False
        return True
##########################################

# 205. Isomorphic Strings

from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        sl = len(s)
        tl = len(t)
        if sl == tl:
            for i in range(sl):
                if s_to_t.get(s[i]) == None:
                    s_to_t[s[i]] = t[i]
                elif s_to_t[s[i]] != t[i]:
                    return False
                if t_to_s.get(t[i]) == None:
                    t_to_s[t[i]] = s[i]
                elif t_to_s[t[i]] != s[i]:
                    return False
            else:
                return True
##########################################     

#290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls = s.split()
        return len(Counter(pattern)) == len(Counter(ls)) == len(Counter(zip(pattern, ls))) and len(pattern) == len(ls)
                
##########################################     

# 242. Valid Anagram
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

##########################################     

# 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection  = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if collection.get(sorted_string):
                collection[sorted_string].append(string)
            else:
                collection[sorted_string] = [string]
        return list(collection.values())
##########################################
# 1. Two Sum
   
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            cache[target - num] = i
        for j, num in enumerate(nums):
            if (num in cache) and cache[num] != j:
                return [cache[num],j]

##########################################           
# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = {}
        happy = n
        while happy != 1 and cache.get(happy) == None:
            cache[happy] = True
            happy_temp = 0 
            for char in str(happy):
                happy_temp += int(char) ** 2
            happy = happy_temp
        return True if happy == 1 else False
##########################################  

# 219. Contains Duplicate II
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {} 
        for i, num in enumerate(nums):
            if record.get(num) != None and ((i - record.get(num)) <= k):
                return True
            else:
                record[num] = i
        return False
########################################## 

# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx = 0
        nums_set = set(nums)
        for n in nums_set:
            if (n-1) not in nums_set:
                length = 1
                while (n+length) in nums_set:
                    length += 1
                mx = max(mx, length)
        
        return mx