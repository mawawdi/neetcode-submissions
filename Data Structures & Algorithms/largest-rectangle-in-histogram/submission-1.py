class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            max_area = max(max_area, h)
            idx = i
            while stack and stack[-1][0] > h:
                top_h, top_i = stack[-1]
                max_area = max(max_area, top_h * (i - top_i))
                idx = top_i
                stack.pop()
            stack.append((h, idx))
        
        for top_h, top_i in stack:
            max_area = max(max_area, top_h * (len(heights) - top_i))
        
        return max_area