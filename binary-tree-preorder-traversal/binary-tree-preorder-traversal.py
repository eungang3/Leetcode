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
        
        while root or stack:
            if root:
                result.append(root.val)
                stack.append(root)
                root = root.left
                
            else:
                root = stack.pop()
                root = root.right
                
        return result