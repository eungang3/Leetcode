# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(current_node):
            if not current_node:
                return []
            left_nodes = inorder(current_node.left)
            right_nodes = inorder(current_node.right)
            
            return left_nodes + [current_node.val] + right_nodes
        
        return inorder(root)