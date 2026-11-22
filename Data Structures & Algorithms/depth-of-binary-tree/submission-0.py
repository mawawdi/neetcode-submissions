# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def walk(node: Optional[TreeNode], count: int):
            if node is None:
                return count
            
            return max(walk(node.left, count + 1), walk(node.right, count + 1))
        
        return walk(root, 0)