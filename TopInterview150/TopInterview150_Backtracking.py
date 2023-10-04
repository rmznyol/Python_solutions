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
        res = []
        def backtrack(combo, start):
            if len(combo) == k:
                res.append(combo[:])
            else:
                for i in range(start,n+1):
                    backtrack(combo + [i],i+1)
        backtrack([],1)

        return res

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
####################################################
# 52. N-Queens II

class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        def next_block(i,j):
            return [i-1 if i else None, j+1 if (j and j < n-1) else None]
        
        def backtrack(combo,no_access):
            nonlocal res
            if len(combo) == n:
                res += 1 
            else:
                cannot_go = set(no[i] for no in no_access for i in range(2) if no[i] != None)
                cannot_go.update(combo)
                no_access = [next_block(*block) for block in no_access]
                for i in range(n):
                    if i not in cannot_go:
                        combo.append(i)
                        backtrack(combo, no_access + [[i-1 if i-1 >= 0 else None, i+1 if i+1 <= n-1 else None]])
                        combo.pop()
        
        backtrack([],[])
        
        return res
####################################################
# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = set()
        def backtrack(path):
            if len(path) == 2*n:
                output.add(path)
            else:
                backtrack('(' + path + ')')
                for i in range(len(path)):
                    backtrack(path[:i]+'()'+ path[i:])
        backtrack('')
        return output
####################################################
# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, l = len(board), len(board[0]), len(word)
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        

        def is_safe(row,col,index,path):
            return 0 <= row < m and 0 <= col < n and word[index] == board[row][col] and (row,col) not in path

        def backtrack(row,col,path,word_index):
            if word_index == l-1:
                return True
            for drow, dcol in dirs:
                n_row, n_col = row + drow, col + dcol
                if is_safe(n_row,n_col, word_index + 1,path):
                    path.add((n_row, n_col))
                    if backtrack(n_row, n_col, path,word_index+1):
                        return True
                    path.remove((n_row, n_col))
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row,col,set([(row,col)]),0):
                    return True
        return False
        