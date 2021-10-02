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
        
        layer_cur = []
        traverse = []
        num = []
        
        layer_cur.append(root)
        while len(layer_cur):
            layer_nxt = []
            count = 0
            while len(layer_cur):
                target = layer_cur.pop(0)
                count += 1
                traverse.append(target)
                if target.left:
                    layer_nxt.append(target.left)
                if target.right:
                    layer_nxt.append(target.right)
            num.append(count)
            layer_cur = layer_nxt
        
        pointer = 0
        for n in num:
            for i in range(n - 1):
                traverse[pointer].next = traverse[pointer + 1]
                pointer += 1
            pointer += 1
        return traverse[0]
            