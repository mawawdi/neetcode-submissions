class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = sorted(s for s, _ in flowers)
        ends = sorted(e for _, e in flowers)
        
        res = [0] * len(people)
        n = len(flowers)
        i = j = 0

        for p, idx in sorted((p, i) for i, p in enumerate(people)):
            while i < n and starts[i] <= p:
                i += 1
            while j < n and ends[j] < p:
                j += 1
            
            res[idx] = i - j
        
        return res