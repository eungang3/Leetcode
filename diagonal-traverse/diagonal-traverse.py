class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        row, column = 0, 0
        row_length, column_length = len(matrix), len(matrix[0])
        direction = 1
            
        while row < row_length and column < column_length:
            result.append(matrix[row][column])
            
            new_row = row + (-1 if direction else 1)
            new_column = column + (1 if direction else -1)
            
            if new_row < 0 or new_row == row_length or new_column < 0 or new_column == column_length:
                if direction:
                    row += (column == column_length - 1)
                    column += (column < column_length - 1)
                else:
                    column += (row == row_length - 1)
                    row += (row < row_length - 1)
                    
                direction = 1 - direction
                
            else:
                row = new_row
                column = new_column
                
        return result