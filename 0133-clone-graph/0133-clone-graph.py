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
        
        def add_node(node):
            if id(node) in mapping:
                return
            
            mapping[id(node)] = Node(val = node.val, neighbors = [])
            
            for original_node in node.neighbors:
                add_node(original_node)
        
        def add_neighbors(node):
            if node in rebuilt:
                return
            
            for original_node in node.neighbors:
                mapping[id(node)].neighbors.append(mapping[id(original_node)])
                
            rebuilt.add(node)
            
            for original_node in node.neighbors:
                add_neighbors(original_node)
        
        if node:
            add_node(node)
            add_neighbors(node)
            return mapping[id(node)]
        
        else:
            return None