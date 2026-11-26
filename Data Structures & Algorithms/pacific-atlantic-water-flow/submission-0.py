class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        reaches_pacific = set({(0, 0)})
        reaches_atlantic = set({(m - 1, n - 1)})

        q = deque([(0, 0)])

        for c in range(n - 1):
            reaches_pacific.add((0, c + 1))
            q.append((0, c + 1))
        for r in range(m - 1):
            reaches_pacific.add((r + 1, 0))
            q.append((r + 1, 0))
        
        
        while q:
            r, c = q.popleft()
            curr = heights[r][c]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= curr and (nr, nc) not in reaches_pacific:
                    reaches_pacific.add((nr, nc))
                    q.append((nr, nc))
        
        q = deque([(m - 1, n - 1)])

        for c in range(0, n - 1):
            reaches_atlantic.add((m - 1, c))
            q.append((m - 1, c))
        for r in range(0, m - 1):
            reaches_atlantic.add((r, n - 1))
            q.append((r, n - 1))

        while q:
            r, c = q.popleft()
            curr = heights[r][c]
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= curr and (nr, nc) not in reaches_atlantic:
                    reaches_atlantic.add((nr, nc))
                    q.append((nr, nc))
        
        return [list(cell) for cell in reaches_pacific & reaches_atlantic]