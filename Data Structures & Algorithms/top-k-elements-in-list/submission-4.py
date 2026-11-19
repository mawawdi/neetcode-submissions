class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_freq = max(count.values())
        freq = [[] for _ in range(max_freq + 1)]

        for n, c in count.items():
            freq[c].append(n)

        result = []
        
        for c in range(max_freq, 0, -1):
            if freq[c]:
                result.extend(freq[c])
                if len(result) == k:
                    return result