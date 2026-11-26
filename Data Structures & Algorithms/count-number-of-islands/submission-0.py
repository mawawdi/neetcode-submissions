class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            if i < 0 or i >= m:
                return
            if j < 0 or j >= n:
                return
            if grid[i][j] == "0":
                return
            else:
                grid[i][j] = "0" # mark it 0 so it doesnt get revisited
            dfs(i + 1, j) # bottom
            dfs(i - 1, j) # top
            dfs(i, j + 1) # right
            dfs(i, j - 1) # left
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        
        return count