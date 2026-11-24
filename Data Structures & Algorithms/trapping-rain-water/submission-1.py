class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        l_max, r_max = height[0], height[n - 1]

        total = 0
        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                total += max(0, l_max - height[l])
            else:
                r -= 1
                r_max = max(r_max, height[r])
                total += max(0, r_max - height[r])
        return total