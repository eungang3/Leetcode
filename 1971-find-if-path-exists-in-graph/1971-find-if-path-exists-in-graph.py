from collections import defaultdict

def validPath(n, edges, destination, source):
    neighbors = defaultdict(list)
    # 기본값이 빈 리스트인 딕셔너리 생성

    for node1, node2 in edges:
        neighbors[node1].append(node2)
        neighbors[node2].append(node1)

    def dfs(current_node, end, visited):
        if current_node == end:
            return True 
        
        if current_node in visited:
            return False 

        for node in neighbors[current_node]:
            if dfs(node, end, visited):
                return True 

        return False 

    visited = set()
    return dfs(source, destination, visited)
