# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def visit(root):
            if root.left:
                visit(root.left)
            result.append(root.val)
            if root.right:
                visit(root.right)
        
        result = []
        visit(root)
        
        n = len(result)
        for i in range(n - 1):
            if result[i] >= result[i + 1]:
                return False
        
        return True
        