# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(digits):
            if digits == '':
                return []
            if digits in letters:
                return list(letters[digits])
            to_be_returned = []
            for combination in backtrack(digits[:-1]):
                for char in letters[digits[-1]]:
                    to_be_returned.append(combination + char)
            return to_be_returned
        return backtrack(digits)
####################################################
# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol=[]
        def backtrack(remain,comb,nex):
			# solution found
            if remain==0:
                sol.append(comb.copy())
            else:
				# iterate through all possible candidates
                for i in range(nex,n+1):
					# add candidate
                    comb.append(i)
					#backtrack
                    backtrack(remain-1,comb,i+1)
					# remove candidate
                    comb.pop()
            
        backtrack(k,[],1)
        return sol

####################################################
# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        contained = {}
        def backtrack(perm, contained):
            if len(perm) == len(nums):
                res.append(perm)
            else:
                for num in nums:
                    if num not in contained:
                        contained.add(num)
                        backtrack(perm + [num],contained)
                        contained.remove(num)
                        
        backtrack([],set())
        return res
####################################################
# 39. Combination Sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        outcome = []
        def backtrack(path, sum_until, starting_index):
            if sum_until == target:
                outcome.append(path.copy())
            else:
                for i in range(starting_index,n):
                    if sum_until + candidates[i] <= target:
                        path.append(candidates[i])
                        backtrack(path,sum_until + candidates[i],i)
                        path.pop()
        backtrack([],0,0)
        return outcome