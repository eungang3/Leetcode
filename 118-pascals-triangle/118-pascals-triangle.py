class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        result = []

        while i < numRows:
            if i == 0:
                result.append([1])
                i += 1 

            else:
                current = [1]
                prev = result[i - 1]
                for j in range(len(prev)):
                    if j + 1 < len(prev):
                        current.append(prev[j] + prev[j + 1])
                current.append(1)
                result.append(current)
                i += 1

        return result