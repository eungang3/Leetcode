class Solution:
    def bfs(self, grid, i, j):
        # 큐에 현재 i, j 튜플 추가
        queue = deque([(i, j)])
        row_length, column_length = len(grid), len(grid[0])
        while queue:
            row, col = queue.popleft()
            # 우측, 아랫쪽, 좌측, 윗쪽 방향 
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            
            # 네 방향에 1이 있는지 모두 체크함
            for direction in directions:
                new_i, new_j = row + direction[0], col + direction[1]
                # 한 칸 이동했는데 거기가 그리드 안쪽이고 1이면
                if (0 <= new_i < row_length) and (0 <= new_j < column_length) and grid[new_i][new_j] == '1':
                    # 이동한 곳을 0으로 바꿈
                    grid[new_i][new_j] = 0
                    # 큐에 이동한 지점 추가
                    queue.append((new_i, new_j))
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # 현재 요소가 1이면 서치 시작
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
        return count