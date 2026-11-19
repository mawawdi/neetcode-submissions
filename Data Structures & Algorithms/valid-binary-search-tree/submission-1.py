# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = float('-inf')

        def in_order(node):
            nonlocal last
            if not node:
                return True
            
            if in_order(node.left) == False:
                return False
            if node.val <= last:
                return False
            last = node.val

            return in_order(node.right)
        
        return in_order(root)
        