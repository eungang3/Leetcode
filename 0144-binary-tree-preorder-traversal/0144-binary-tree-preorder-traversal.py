# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root_node):
            if not root_node:
                return []
            
            left_nodes = postorder(root_node.left) if root_node.left else []
            right_nodes = postorder(root_node.right) if root_node.right else []
            
            return [root_node.val] + left_nodes + right_nodes
        
        return postorder(root)