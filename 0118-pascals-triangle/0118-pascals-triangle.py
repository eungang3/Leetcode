class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        
        for i in range(2, numRows):
            new_row = [1]
            last_row = result[-1]
            
            for j in range(len(last_row) - 1):
                new_row.append(last_row[j] + last_row[j + 1])
            
            new_row.append(1)
            result.append(new_row)
            
        return result[:numRows]