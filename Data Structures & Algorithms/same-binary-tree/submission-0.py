# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(n1, n2):
            if n1 is None and n2 is None:
                return True
            elif (n1 is None and n2 is not None) or (n1 is not None and n2 is None):
                return False
            if n1.val != n2.val:
                return False
            
            return check(n1.left, n2.left) and check(n1.right, n2.right)
        
        return check(p, q)