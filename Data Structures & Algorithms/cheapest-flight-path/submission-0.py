class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, weight in flights:
            adj[u].append((v, weight))

        # dist[node][flights_used] = min cost to reach node using exact flights_used edges
        dist = [[float('inf')] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        pq = [(0, src, 0)]  # (cost, node, flights_used)

        while pq:
            curr_dist, curr_node, flights_used = heapq.heappop(pq)

            if curr_node == dst:
                return curr_dist
            if flights_used > k or curr_dist > dist[curr_node][flights_used]:
                continue

            next_flights = flights_used + 1
            for neighbor, weight in adj[curr_node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor][next_flights]:
                    dist[neighbor][next_flights] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor, next_flights))

        return -1