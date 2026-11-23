# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # A[v] = max path sum in subtree v that ends at v
        # B[v] = max path sum in subtree v that cannot extend upwards (uses both children left and right of v, or stays inside a subtree of subtree v)

        best = float('-inf')
        def dfs(node):
            nonlocal best
            if node is None:
                return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            best = max(best, l + r + node.val)

            return node.val + max(l, r)
        
        dfs(root)

        return best