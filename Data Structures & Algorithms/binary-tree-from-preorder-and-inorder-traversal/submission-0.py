# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {val:idx for idx,val in enumerate(inorder)}
        pre_idx = 0

        def build(l, r):
            nonlocal pre_idx
            if l > r:
                return None
            
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)

            root.left = build(l, in_map[root_val] - 1)
            root.right = build(in_map[root_val] + 1, r)
            return root

        return build(0, len(inorder) - 1)