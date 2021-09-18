# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def visit(root):
            if root.left:
                visit(root.left)
            result.append(root.val)
            if root.right:
                visit(root.right)
            
        if not root:
            return None
        
        result = []
        visit(root)
        return result
        