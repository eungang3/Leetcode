class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        result = ''
        
        while carry or a or b:
            if a:
                carry += int(a.pop())
                
            if b:
                carry += int(b.pop())
                
            result += str(carry % 2)
            carry //= 2    
                
        return result[::-1]
                