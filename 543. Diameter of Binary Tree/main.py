# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def visit(root):
            if not root:
                return 0
            
            left = visit(root.left)
            right = visit(root.right)
            d = left + right
            if d > self.result:
                self.result = d
            return max(left, right) + 1
        
        self.result = 0
        visit(root)
        return self.result