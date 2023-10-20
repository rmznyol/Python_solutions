# 909. Snakes and Ladders
class Solution:
    def to_position(self, k, n):
        if k > n**2: return self.to_position(n**2, n)
        counter_row = ((k-1) // n)
        row = n - 1 - counter_row
        col = (k-1) % n  if counter_row % 2 == 0 else n -1 -(k -1)% n
        return row, col  
    # def to_number(self,i,j,n):
    #     k = (n-1-i) * n
    #     k += j + 1 if (n-1-i) % 2 == 0 else n - j
    #     return k  
        
    
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        visited = [True if i == 0 else False for i in range(n ** 2)]
        queue = collections.deque([(1,0)]) # position, step
        while queue:
            curr, step = queue.popleft()
            if curr >= n ** 2:
                return step
            else:
                for next_num in range(curr + 1, min(curr+7, n**2 + 1)):
                    if not visited[next_num-1]:
                        visited[next_num-1] = True
                        position = self.to_position(next_num,n)
                        next_num = next_num if board[position[0]][position[1]] == -1 else board[position[0]][position[1]]                    
                        queue.append((next_num,step+1)) 
       
        return -1 


###############################################################