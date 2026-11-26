"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        q = deque([node])
        map = {}
        map[node] = Node(node.val)

        while q:
            popped = q.popleft()
            if popped not in map:
                map[popped] = Node(popped.val)

            for neighbor in popped.neighbors:
                if neighbor not in map:
                    map[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                map[popped].neighbors.append(map[neighbor])
        
        return map[node]
