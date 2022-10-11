class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = 0
        int_b = 0

        for i in range(len(a)):
            power = len(a) - i - 1
            int_a += (2 ** power) * int(a[i])

        for j in range(len(b)):
            power = len(b) - j - 1
            int_b += (2 ** power) * int(b[j])

        total = int_a + int_b
        result = ''

        while(total > 0):
            result += str(total % 2)
            total = total // 2
        
        if result == "":
            return "0"
            
        return result[::-1]