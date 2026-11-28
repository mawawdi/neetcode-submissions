class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        best = float('inf')
        l = r = 0
        curr_sum = 0

        while r < n:
            curr_sum += nums[r]
            while curr_sum >= target:
                best = min(best, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            r += 1
        
        return best if best != float('inf') else 0