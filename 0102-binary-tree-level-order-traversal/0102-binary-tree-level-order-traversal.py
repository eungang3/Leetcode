# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            levelLength = len(queue)
            levelNodes = []
            
            for i in range(levelLength):
                currentNode = queue.popleft()
                levelNodes.append(currentNode.val)
                
                if currentNode.left:
                    queue.append(currentNode.left)
                    
                if currentNode.right:
                    queue.append(currentNode.right)
                    
            result.append(levelNodes)
            
        return result
