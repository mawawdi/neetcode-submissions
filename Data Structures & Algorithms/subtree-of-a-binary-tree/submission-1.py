# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        def check(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
            if n1 is None and n2 is None:
                return True
            if n1 is None or n2 is None or n1.val != n2.val:
                return False
            return check(n1.left, n2.left) and check(n1.right, n2.right)
        
        def walk(node):
            if node is None:
                return False

            return check(node, subRoot) or walk(node.left) or walk(node.right)
        
        return walk(root)
