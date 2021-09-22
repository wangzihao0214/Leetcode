# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:   
        def visit(root):
            if not root:
                return [0, float('-inf')]

            sum_left, max_left = visit(root.left)
            sum_left = max(sum_left, 0)

            sum_right, max_right = visit(root.right)
            sum_right = max(sum_right, 0)

            sum_all = sum_left + sum_right + root.val
            maximum = max(sum_all, max_left, max_right)
            sum_sub = max(sum_left, sum_right) + root.val
            
            return [sum_sub, maximum]
        
        return visit(root)[1]