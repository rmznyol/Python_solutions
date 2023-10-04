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