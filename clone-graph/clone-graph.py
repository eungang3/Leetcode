"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        mapping = {}
        rebuilt = set()
        
        def dfs_copy(node):
            if id(node) in mapping:
                return
            
            mapping[id(node)] = Node(val=node.val, neighbors=[])

            for original_neighbor in node.neighbors:
                dfs_copy(original_neighbor)
        
        def dfs_rebuild_neighbor(node):
            if node in rebuilt:
                return
            
            for original_neighbor in node.neighbors:
                mapping[id(node)].neighbors.append(mapping[id(original_neighbor)])
            
            rebuilt.add(node)
            
            for original_neighbor in node.neighbors:
                dfs_rebuild_neighbor(original_neighbor)
                
        if node:
            dfs_copy(node)
            dfs_rebuild_neighbor(node)
            return mapping[id(node)]
        
        else:
            return None
            
                    
                    