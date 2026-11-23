# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        n1, n2 = min(p.val, q.val), max(p.val, q.val)
        curr = root

        while curr:
            if n1 > curr.val:
                curr = curr.right
            elif n2 < curr.val:
                curr = curr.left
            else:
                return curr