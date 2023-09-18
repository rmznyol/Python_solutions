#1926. Nearest Exit from Entrance in Maze

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(maze), len(maze[0])
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        queue = collections.deque([[start_row, start_col, 0]])
        while queue:
            i, j, d = queue.popleft()
            for di, dj in dirs:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and maze[ni][nj] == ".":
                    if ni == m-1 or nj == n-1 or ni == 0 or nj == 0:
                        return d + 1
                    maze[ni][nj] = "+"
                    queue.append([ni, nj, d + 1])

        return -1
####################################################################################
# 994. Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def is_safe(i,j):
            return 0 <= i < rows and 0 <= j < cols
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        # add all the bad oranges to queue and see if there are any oranges to begin with
        bad_oranges = collections.deque()
        orange_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    bad_oranges.append((i,j,0))
                elif grid[i][j] == 1:
                    neighbors = [(i+di, j+dj) for di, dj in directions if is_safe(i+di,j+dj)] 
                    no_access = [(i,j) for i,j in neighbors if grid[i][j] == 0]
                    if len(no_access) == len(neighbors):
                        # if there are inaccessible oranges, return -1 immediately
                        return -1   
                if grid[i][j] != 0: orange_count += 1
        # no oranges?, return 0
        if orange_count == 0: return 0
        max_time = -1
        for row in grid:
            print(row)
        while bad_oranges:
            i, j, t = bad_oranges.popleft()
            max_time = max(t,max_time)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if is_safe(ni,nj) and grid[ni][nj] == 1:
                     grid[ni][nj] = 2
                     bad_oranges.append((ni,nj,t+1))
        for row in grid:
            for cell in row:
                if cell == 1:  # still got a fresh orange left
                    return -1
        return max_time