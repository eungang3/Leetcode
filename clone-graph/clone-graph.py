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
        
        # neighbor도 복사한 노드의 모음
        rebuilt = set()
        
        def dfs_copy(node):
            if id(node) in mapping:
                return
            
            # 현재 노드의 deep copy 생성, neighbors는 빈 값으로 둠 
            mapping[id(node)] = Node(val=node.val, neighbors=[])
            
            for original_neighbor in node.neighbors:
                # 현재 노드의 이웃 노드의 deep copy 생성
                dfs_copy(original_neighbor)
        
        def dfs_rebuild_neighbor(node):
            if node in rebuilt:
                return
            
            for original_neighbor in node.neighbors:
                # mapping에 있는 deep copy된 노드의 neighbors에 deep copy된 이웃 노드 추가 
                mapping[id(node)].neighbors.append(mapping[id(original_neighbor)])
            
            rebuilt.add(node)
            
            for original_neighbor in node.neighbors:
                dfs_rebuild_neighbor(original_neighbor)
        
        if node:
            # 1) 노드 값 먼저 복사
            dfs_copy(node)
			
            # 2) 노드 neighbors 추가
            dfs_rebuild_neighbor(node)
			
            return mapping[id(node)]
        
        else:
            return None