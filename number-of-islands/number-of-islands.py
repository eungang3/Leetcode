from collections import deque 

class Solution:
    def bfs(self, i, j, grid):
        queue = deque([(i, j)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while queue:
            row, column = queue.popleft()
        
            for direction in directions:
                new_i = row + direction[0]
                new_j = column + direction[1]
                
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                    grid[new_i][new_j] = 0
                    queue.append((new_i, new_j))
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(i, j, grid)
        
        return count