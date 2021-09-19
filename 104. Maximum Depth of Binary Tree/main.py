# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getDepth(root):
            if root:
                return 1 + max(getDepth(root.left), getDepth(root.right))
            else:
                return 0
            
        return getDepth(root)
        