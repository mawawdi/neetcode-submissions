# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        invalid = False
        def dfs(node):
            nonlocal invalid
            if not node:
                return 0
            l = dfs(node.left)
            if l == -1:
                return -1
            r = dfs(node.right)
            if r == -1:
                return -1
            diff = abs(l - r)
            if diff > 1:
                invalid = True
                return -1
            return 1 + max(l, r)

        dfs(root)

        return not invalid