class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cur_max = [0] * n # cur_max[i]: max product of a subarray ending at i
        cur_min = [0] * n # cur_min[i]: min product of a subarray ending at i

        cur_max[0] = cur_min[0] = nums[0]

        for i in range(1, n):
            cur_max[i] = max(nums[i], nums[i] * cur_max[i - 1], nums[i] * cur_min[i - 1])
            cur_min[i] = min(nums[i], nums[i] * cur_max[i - 1], nums[i] * cur_min[i - 1])
        
        return max(cur_max)