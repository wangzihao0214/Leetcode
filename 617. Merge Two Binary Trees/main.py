# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1, node2):
            if node1 and node2:
                return TreeNode(node1.val + node2.val)
            elif node1:
                return node1
            elif node2:
                return node2
            else:
                return None
        
        result = merge(root1, root2)
        if root1 and root2:
            result.left = self.mergeTrees(root1.left, root2.left)
            result.right = self.mergeTrees(root1.right, root2.right)
        
        return result