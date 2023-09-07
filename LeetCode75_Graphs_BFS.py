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