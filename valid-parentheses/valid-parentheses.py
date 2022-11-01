class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        couples = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        
        for character in s:
            if character in couples:
                if stack[-1:] != [couples[character]]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(character)
                
        return not stack