class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0

        while num_set:
            if len(num_set) <= best:
                break  # remaining elements cannot beat current best

            n = num_set.pop()
            left = n - 1
            right = n + 1

            while left in num_set:
                num_set.remove(left)
                left -= 1

            while right in num_set:
                num_set.remove(right)
                right += 1

            best = max(best, right - left - 1)

        return best