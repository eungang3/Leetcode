from collections import deque 

class Solution:
    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        row_length = len(grid)
        column_length = len(grid[0])
        
        while queue:
            row, column = queue.popleft()
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            
            for direction in directions:
                new_i, new_j = (row + direction[0], column + direction[1])
                if (0 <= new_i < row_length) and (0 <= new_j < column_length) and grid[new_i][new_j] == '1':
                    grid[new_i][new_j] = 0
                    queue.append((new_i, new_j))
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
        return count