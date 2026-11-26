class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        best = 0

        def dfs(i, j):
            if i < 0 or i >= m:
                return 0
            if j < 0 or j >= n:
                return 0
            if grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
            b = dfs(i + 1, j)
            t = dfs(i - 1, j)
            r = dfs(i, j + 1)
            l = dfs(i, j - 1)
            return 1 + b + t + r + l
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    best = max(best, area)
        
        return best
        