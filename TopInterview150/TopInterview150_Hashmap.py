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