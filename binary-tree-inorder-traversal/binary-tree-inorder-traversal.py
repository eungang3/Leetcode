# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
                
            else:
                popped = stack.pop()
                result.append(popped.val)
                root = popped.right
                
        return result
                