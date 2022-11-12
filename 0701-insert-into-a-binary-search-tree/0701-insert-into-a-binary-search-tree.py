# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            root = TreeNode(val)
            return root
        def recursive_insert(root_node):
            if val < root_node.val:
                if root_node.left:
                    recursive_insert(root_node.left)
                else:
                    root_node.left = TreeNode(val)
            else:
                if root_node.right:
                    recursive_insert(root_node.right)
                else:
                    root_node.right = TreeNode(val)
        
        recursive_insert(root)
        
        return root