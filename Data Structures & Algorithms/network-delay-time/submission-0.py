class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for src, dst, weight in times:
            adj[src].append((dst, weight))
        
        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > dist[curr_node]:
                continue
            for neighbor, weight in adj[curr_node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        furthest = max([d for _, d in dist.items()])

        return furthest if furthest != float('inf') else -1