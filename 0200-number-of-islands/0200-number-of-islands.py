from collections import deque 

class Solution:
    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        n, m = len(grid), len(grid[0])
        while queue:
            row, col = queue.popleft()
            dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for move in dirs:
                row_move, col_move = (row + move[0], col + move[1])
                if (0 <= row_move < n) and (0 <= col_move < m) and grid[row_move][col_move] == '1':
                    grid[row_move][col_move] = 0
                    queue.append((row_move, col_move))
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
        return count 
    
    