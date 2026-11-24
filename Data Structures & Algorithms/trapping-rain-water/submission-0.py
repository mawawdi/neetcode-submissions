class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n
        curr_max = 0

        for i in range(n):
            max_l[i] = curr_max
            curr_max = max(curr_max, height[i])

        curr_max = 0
        for i in range(n - 1, -1, -1):
            max_r[i] = curr_max
            curr_max = max(curr_max, height[i])
        
        total = 0
        for i in range(n):
            total += max(0, min(max_l[i], max_r[i]) - height[i])

        return total