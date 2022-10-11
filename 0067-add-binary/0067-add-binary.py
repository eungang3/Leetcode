class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())

            if b:
                carry += int(b.pop())

            # carry가 0이면 0을 result에 추가
            # carry가 1이면 1을 result에 추가
            # carry가 2면 0을 result에 추가
            result += str(carry % 2)

            # carry가 0이면 carry는 0이 됨
            # carry가 1이면 carry는 0이 됨
            # carry가 2면 carry는 1이 됨
            carry //= 2

        return result[::-1]      
