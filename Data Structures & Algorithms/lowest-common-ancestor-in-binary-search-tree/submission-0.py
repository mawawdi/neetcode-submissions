# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        n1 = p.val if p.val <= q.val else q.val # MIN
        n2 = p.val if p.val > q.val else q.val # MAX

        def traverse(node):
            if node is None:
                return None
            
            if n2 < node.val:
                return traverse(node.left)
            elif n1 > node.val:
                return traverse(node.right)
            elif n1 < node.val < n2 or n1 == node.val or n2 == node.val:
                return node
        
        return traverse(root)