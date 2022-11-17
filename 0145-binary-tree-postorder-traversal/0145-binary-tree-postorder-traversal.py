# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root_node):
            if not root_node:
                return []
            
            left_nodes = postorder(root_node.left) if root_node.left else []
            right_nodes = postorder(root_node.right) if root_node.right else []
            
            return left_nodes + right_nodes + [root_node.val]
            
        return postorder(root)