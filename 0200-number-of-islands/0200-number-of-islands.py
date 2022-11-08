class Solution:
    def findLand(self, grid, i, j):
        stack = [(i, j)]
        visited = set()
        
        while stack:
            i,j = stack.pop()
        
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            for direction in directions:
                new_i = direction[0] + i
                new_j = direction[1] + j

                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                    grid[new_i][new_j] = '0'
                    stack.append((new_i, new_j))
                    visited.add((new_i, new_j))
            
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    count += 1
                    self.findLand(grid, i, j)
                    
        return count 