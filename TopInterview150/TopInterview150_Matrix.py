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
#54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        k = 0
        output = []
        while len(output) < m*n:
        # 0 + k - > j - 1 - k on fixed kth row k <= n // 2 
            for i in range(k, n-k):
                output.append(matrix[k][i]) 
        # 0 + k - > j - 1 - k on fixed n-1-k column
            for j in range(k+1, m-k):
                output.append(matrix[j][n-1-k])
            if k < m - 1 - k:
                for i in range(n-1-k -1, k-1, -1):
                    output.append(matrix[m-1-k][i])
            if k < n - 1 - k:
                for j in range(m-1-k -1, k, -1):
                    output.append(matrix[j][k])
            k += 1
        return output 
################################################################
# 48. Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #(x, y)->(y, -x)
        #(i, -j) + ((n-1)/2,)
        n = len(matrix)
        for row in range(n//2):
            temp = matrix[n-1-row]
            matrix[n - row - 1] = matrix[row]
            matrix[row] = temp
        for row in range(n):
            for column in range(row):
                temp = matrix[column][row]
                matrix[column][row] = matrix[row][column]
                matrix[row][column] = temp
        return matrix