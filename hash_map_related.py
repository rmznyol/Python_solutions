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

  ########################################################################
#1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        sum_dict = {}
        for num in nums:
            if sum_dict.get(num):
                sum_dict[num][1] += 1
            else:
                sum_dict[num] = [True, 1]
        result = 0
        for num in nums:
            if sum_dict[num][1]:
                sum_dict[num][1] -= 1
                if sum_dict.get(k-num) and sum_dict[k-num][1]:
                    result += 1
                    sum_dict[k-num][1] -= 1
        return result