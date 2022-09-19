class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        row_length, column_length = len(matrix), len(matrix[0])
        
        # matrix의 요소를 한 번에 하나씩 검사하는 인덱스 
        row, column = 0, 0
        
        # 대각선 방향을 알려주는 플래그
        # 1이면 올라가는 대각선 ↗︎, 0이면 내려가는 대각선 ↙︎
        direction = 1
        
        result = []
        
        # matrix의 요소를 한 번에 하나씩 검사하는 while 루프
        while row < row_length and column < column_length:
            
            # 현재 요소 result에 추가
            result.append(matrix[row][column])
            
            # direction 방향을 보고 다음 칸 가정하기
            # 올라가는 경우 [i, j] -> [i - 1, j + 1] 
            # 내려가는 경우 [i, j] -> [i + 1, j - 1] 
            new_row = row + (-1 if direction == 1 else 1)
            new_column = column + (1 if direction == 1 else -1)
            
            # 가정한 다음 칸이 매트릭스 바깥인 경우 새 대각선의 시작점 찾기
            if new_row < 0 or new_row == row_length or new_column < 0 or new_column == column_length:
                
                # 올라가는 대각선이었다면
                if direction:
                    # 끝머리의 오른쪽 요소가 매트리스 안에 있으면 다음 시작점은 오른쪽 [i, j + 1] 
                    # 끝머리의 오른쪽 요소가 매트리스 바깥인 경우 다음 시작점은 아랫칸 [i + 1, j]
                    row += (column == column_length - 1)
                    column += (column < column_length - 1)
                
                # 내려가는 대각선이었다면
                else:
                    # 끝머리의 아랫쪽 요소가 매트리스 안에 있으면 다음 시작점은 아랫칸[i + 1, j]
                    # 끝머리의 아랫쪽 요소가 매트리스 바깥인 경우 다음 시작점은 오른쪽[i, j + 1]
                    column += (row == row_length - 1)
                    row += (row < row_length - 1)
                    
                # 방향 뒤집기
                direction = 1 - direction     

            # 다음 칸이 매트릭스 안쪽인 경우 가정한 다음칸을 다음칸으로 만들기    
            else:
                row = new_row
                column = new_column
                        
        return result