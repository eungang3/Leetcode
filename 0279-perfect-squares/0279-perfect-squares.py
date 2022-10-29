class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        
        queue = collections.deque([n])
        depth = 0
        
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                current = queue.popleft()
                base = 1
                
                while base * base <= current:
                    rest = current - base * base
                    if rest == 0:
                        return depth
                    queue.append(rest)
                    base += 1
                
        return depth