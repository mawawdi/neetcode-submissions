class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = cur_max = cur_min = nums[0]

        for num in nums[1:]:
            candidates = (num, num * cur_max, num * cur_min)
            cur_max = max(candidates)
            cur_min = min(candidates)
            best = max(best, cur_max)

        return best