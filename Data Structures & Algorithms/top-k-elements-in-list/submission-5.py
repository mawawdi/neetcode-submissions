class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_freq = max(count.values())
        freq = [[] for i in range(max_freq + 1)]

        for n, c in count.items():
            freq[c].append(n)

        result = []
        
        for i in range(max_freq, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result