class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush_max(heap, (dist, x, y))
            if len(heap) > k:
                heapq.heappop_max(heap)
        return [(x, y) for _, x, y in heap]