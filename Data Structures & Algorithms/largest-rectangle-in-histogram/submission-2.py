class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            max_area = max(max_area, h)
            idx = i
            while stack and stack[-1][1] > h:
                top_i, top_h = stack.pop()
                max_area = max(max_area, top_h * (i - top_i))
                idx = top_i
            stack.append((idx, h))
        
        for top_i, top_h in stack:
            max_area = max(max_area, top_h * (len(heights) - top_i))
        
        return max_area