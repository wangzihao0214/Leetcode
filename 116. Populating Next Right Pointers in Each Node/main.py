"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        s = [root]
        while len(s) != 0:
            target = s.pop()
            if target.left and target.right:
                target.left.next = target.right
                if target.next:
                    target.right.next = target.next.left
                s.append(target.left)
                s.append(target.right)
        return root
        