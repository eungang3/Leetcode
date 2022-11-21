# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
                
            else:
                popped = stack.pop()
                root = popped.right
                
        return result