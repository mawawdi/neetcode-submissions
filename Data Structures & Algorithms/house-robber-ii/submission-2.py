class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def rob(start, end):
            prev2 = nums[start]
            prev1 = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                prev1, prev2 = max(nums[i] + prev2, prev1), prev1
        
            return prev1
        
        return max(rob(0, n - 1), rob(1, n))