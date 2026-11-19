class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = -1

        i, j = 0, len(heights) - 1

        while i < j:
            a, b = heights[i], heights[j]
            best = max(best, min(a, b) * (j - i))
            if a < b:
                i += 1
            else:
                j -= 1

        return best