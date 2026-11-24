class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = [0] * (len(nums) - k + 1)
        l = 0
        for i in range(0, k):
            heapq.heappush_max(heap, (nums[i], i))

        for r in range(k - 1, len(nums)):
            heapq.heappush_max(heap, (nums[r], r))
            while heap and heap[0][1] < l:
                heapq.heappop_max(heap)
            res[l] = heap[0][0]
            l += 1
        return res