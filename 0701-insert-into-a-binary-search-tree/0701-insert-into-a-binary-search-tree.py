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
        
        def insert(root, val):
            new_node = TreeNode(val)
            
            if val < root.val:
                if root.left:
                    insert(root.left, val)
                else:
                    root.left = new_node
                    
            else:
                if root.right:
                    insert(root.right, val)
                    
                else:
                    root.right = new_node
            
        insert(root, val)
        return root