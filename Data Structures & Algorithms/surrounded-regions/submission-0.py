class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        starts = deque()

        for r in range(m):
            if board[r][0] == "O":
                starts.append((r, 0))
            if board[r][n - 1] == "O":
                starts.append((r, n - 1))
        
        for c in range(n):
            if board[0][c] == "O":
                starts.append((0, c))
            if board[m - 1][c] == "O":
                starts.append((m - 1, c))

        visited = set()
        while starts:
            r, c = starts.popleft()
            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and board[nr][nc] == "O"
                    and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    starts.append((nr, nc))
        
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if board[r][c] == "O" and (r, c) not in visited:
                    board[r][c] = "X"
