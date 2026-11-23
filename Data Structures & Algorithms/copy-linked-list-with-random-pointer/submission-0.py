"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        dummy = Node(0)
        current = dummy

        while head:
            if head not in old_to_new:
                old_to_new[head] = Node(head.val)
            current.next = old_to_new[head]
            current = current.next

            if head.random not in old_to_new:
                old_to_new[head.random] = Node(head.random.val)
            current.random = old_to_new[head.random]

            head = head.next

        return dummy.next