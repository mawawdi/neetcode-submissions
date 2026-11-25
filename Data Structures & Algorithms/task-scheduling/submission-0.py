class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord('A')] += 1
        heap = [f for f in freq if f > 0]
        heapq.heapify_max(heap)
        total = 0

        while heap:
            popped = []
            for _ in range(n + 1):
                if not heap:
                    break
                p = heapq.heappop_max(heap)
                popped.append(p)

            for f in popped:
                if f > 1:
                    heapq.heappush_max(heap, f - 1)
                    
            total += n + 1 if heap else len(popped)
            
        return total