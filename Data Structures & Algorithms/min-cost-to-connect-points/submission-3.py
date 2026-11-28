class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (weight, node)
        total_cost = 0

        while len(visited) < n:
            weight, u = heapq.heappop(min_heap)
            if u in visited:
                continue

            visited.add(u)
            total_cost += weight
            x1, y1 = points[u]

            for v in range(n):
                if v not in visited:
                    x2, y2 = points[v]
                    heapq.heappush(min_heap, (abs(x1 - x2) + abs(y1 - y2), v))

        return total_cost