class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        components = 0
        visited = set()

        def bfs(node):
            nonlocal visited
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    bfs(neighbor)

        for i in range(n):
            if i not in visited:
                components += 1
                bfs(i)

        return components