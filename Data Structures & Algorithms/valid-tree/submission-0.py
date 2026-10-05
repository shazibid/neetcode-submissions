class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)] #create adjancency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)

            for neighbors in adj[node]:
                if neighbors == parent:
                    continue
                if not dfs(neighbors, node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n
