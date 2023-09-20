# 36. Valid Sudoku

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            counter = defaultdict(int)
            for column in range(9):
                check = row[column]
                if check != ".":
                    counter[check]+=1
                    if counter[check] > 1:
                        return False 
        for column in range(9):
            counter = defaultdict(int)
            for row in board:    
                check = row[column]
                if check != ".":
                    counter[check]+=1
                    if counter[check] > 1:
                        return False 
        for row in [0,3,6]:
            for column in [0,3,6]:
                counter = defaultdict(int)
                for subrow in board[row:row+3]:
                    for check in subrow[column:column+3]:
                        if check != ".":
                            counter[check]+=1
                            if counter[check] > 1:
                                return False 

        return True
################################################################