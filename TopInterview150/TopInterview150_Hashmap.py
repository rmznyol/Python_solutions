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