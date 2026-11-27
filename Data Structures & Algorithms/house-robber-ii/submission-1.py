class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        nums1 = [nums[i] for i in range(n - 1)]
        nums2 = [nums[i] for i in range(1, n)]

        dp1, dp2 = [0] * (n - 1), [0] * (n - 1)

        dp1[0], dp2[0] = nums1[0], nums2[0]
        dp1[1], dp2[1] = max(nums1[0], nums1[1]), max(nums2[0], nums2[1])

        for i in range(2, n-1):
            dp1[i] = max(nums1[i] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(nums2[i] + dp2[i - 2], dp2[i - 1])
        
        return max(dp1[n - 2], dp2[n - 2])