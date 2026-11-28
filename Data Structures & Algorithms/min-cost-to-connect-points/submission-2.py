class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        visited = set()
        min_heap = [(0, 0, None)]
        mst_edges = []
        total_cost = 0

        while min_heap and len(visited) < len(points):
            weight, u, parent = heapq.heappop(min_heap)

            if u in visited:
                continue
            visited.add(u)
            total_cost += weight
            if parent is not None:
                mst_edges.append((parent, u, weight))
            for v in range(len(points)):
                if u == v:
                    continue
                edge_weight = manhattan(points[u], points[v])
                if v not in visited:
                    heapq.heappush(min_heap, (edge_weight, v, u))
        
        return total_cost
            
