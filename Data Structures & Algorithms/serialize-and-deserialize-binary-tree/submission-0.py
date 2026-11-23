# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        coded = []
        def dfs(rt):
            if not rt:
                coded.append("n")
                return
            coded.append(f'{rt.val}')
            dfs(rt.left)
            dfs(rt.right)
        dfs(root)
        return ",".join(coded)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = deque(data.split(','))
        def dfs(nums):
            val = nums.popleft()
            if val == 'n':
                return None
            root = TreeNode(int(val))
            root.left = dfs(nums)
            root.right = dfs(nums)
            return root
        return dfs(arr)
