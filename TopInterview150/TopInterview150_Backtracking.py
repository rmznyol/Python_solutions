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