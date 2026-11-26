class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque([])
        has_fresh = False
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    has_fresh = True 
        
        if has_fresh and not q:
            return -1
        
        if not has_fresh:
            return 0


        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                # bottom
                if r + 1 < m and grid[r + 1][c] == 1:
                    grid[r + 1][c] = 2
                    q.append((r + 1, c))
                # top
                if r - 1 >= 0 and grid[r - 1][c] == 1:
                    grid[r - 1][c] = 2
                    q.append((r - 1, c))
                # right
                if c + 1 < n and grid[r][c + 1] == 1:
                    grid[r][c + 1] = 2
                    q.append((r, c + 1))
                # left
                if c - 1 >= 0 and grid[r][c - 1] == 1:
                    grid[r][c - 1] = 2
                    q.append((r, c - 1))
            time += 1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return -1
        
        return time