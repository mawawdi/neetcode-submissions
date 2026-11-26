class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        q = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.appendleft((r, c))
        
        while q:
            r, c = q.popleft()
            if r < 0 or r >= m or c < 0 or c >= n:
                continue
            cell = grid[r][c]
            # bottom
            if r + 1 < m and grid[r + 1][c] == 2147483647:
                grid[r + 1][c] = cell + 1
                q.append((r + 1, c))
            # top
            if r - 1 >= 0 and grid[r - 1][c] == 2147483647:
                grid[r - 1][c] = cell + 1
                q.append((r - 1, c))
            # right
            if c + 1 < n and grid[r][c + 1] == 2147483647:
                grid[r][c + 1] = cell + 1
                q.append((r, c + 1))
            # left
            if c - 1 >= 0 and grid[r][c - 1] == 2147483647:
                grid[r][c - 1] = cell + 1
                q.append((r, c - 1))
        