#1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        result = ''
        for i in range(min([l1,l2])):
            result += (word1[i] + word2[i])
        if l1 < l2:
            result += word2[l1:]
        else:
            result += word1[l2:]
        return result
#####################################################
# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]
#####################################################
# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        result = []
        for candy in candies:
            result.append((candy + extraCandies) >= m)
        return result
#####################################################
# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0;
        for i in range(len(flowerbed)) :
            if ((i == 0 or flowerbed[i - 1] == 0) and flowerbed[i] == 0
                    and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1;
                count+=1;
        return count >= n; 
#####################################################
# 345. Reverse Vowels of a String

from collections import deque
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_record = deque()
        vowels = {char:i for i,char in enumerate('aeiouAEIOU')}
        for char in s:
            if vowels.get(char) != None:
                vowel_record.append(char)
        result = ''
        for char in s:
            result += char if vowels.get(char) == None else vowel_record.pop()
        return result
#####################################################
# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        word = ''
        for char in s + ' ':
            if char != ' ':
                word += char
            else:
                if word != '':
                    result = word + ' ' + result 
                word = ''
        return result[:-1]
#####################################################
# 238. Product of Array Except Self

from itertools import accumulate
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = list(accumulate([1]+nums[:-1], lambda x,y : x*y))
        right = list(accumulate([1]+nums[:0:-1], lambda x,y : x*y))[::-1]
        return [left[i]*right[i] for i in range(n)]
#####################################################
# 334. Increasing Triplet Subsequence

from itertools import accumulate
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        left = list(accumulate(nums[:-2],min))
        right = list(accumulate(nums[-1:1:-1],max))
        for i in range(1,n-1):
            if left[i-1] < nums[i] and nums[i] < right[n-2-i]:
                return True
        return False
#####################################################
# 443. String Compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0 # where we enter the chars
        n = len(chars)
        i = 0
        while i < n:
            group_char = chars[i]
            j = 0
            group_count = 0
            while i+j < n and chars[i+j] == group_char:
                j += 1
                group_count += 1
            chars[index] = group_char
            if group_count > 1:
                for k,num in enumerate(str(group_count)):
                    chars[index+k+1] = num
                index += len(str(group_count))
            index += 1
            i += group_count
        chars = chars[:index]
        return len(chars)