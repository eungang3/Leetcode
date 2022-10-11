class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        
        list_a = list(a)
        list_b = list(b)
        
        result = ''
        
        while list_a or list_b or carry:
            if list_a:
                carry += int(list_a.pop())
                
            if list_b:
                carry += int(list_b.pop())
                
            result += str(carry % 2)
            carry //= 2
        
        return result[::-1]
            