class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def idx_to_rc(idx):
            return (idx // n, idx % n)
        
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = idx_to_rc(mid)
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1

        return False
        