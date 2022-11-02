class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set(['0000'])
        queue = collections.deque([('0000', 0)])
        
        while queue:
            string, steps = queue.popleft()
            
            if string in deadends:
                continue
                
            if string == target:
                return steps
            
            for i in range(4):
                digit = string[i]
                
                for move in [-1, 1]:
                    new_digit = (int(digit) + move) % 10
                    new_string = string[:i] + str(new_digit) + string[i+1:]
                    
                    if not new_string in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps + 1))
                        
        return -1