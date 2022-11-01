class Solution:
    def isValid(self, s: str) -> bool:
        couples = {
            ')' : '(',
            ']' : '[',
            '}' : '{' 
        }
        stack = []
        
        for parenthesis in s:
            if parenthesis in couples:
                if [couples[parenthesis]] != stack[-1:]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(parenthesis)
                
        return not stack