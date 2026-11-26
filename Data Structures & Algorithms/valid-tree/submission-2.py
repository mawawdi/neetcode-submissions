class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        q = deque([0])
        visited = set()

        while q:
            curr = q.popleft()
            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        
        return len(visited) == n