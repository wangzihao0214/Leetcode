# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and not root2:
                return False
            if not root1 and root2:
                return False
            if root1.val != root2.val:
                return False
            return compare(root1.left, root2.left) and compare(root1.right, root2.right)

        def compare_all(root1, root2):
            if not root1:
                return False
            return compare(root1, root2) or compare_all(root1.left, root2) or compare_all(root1.right, root2)

        return compare_all(root, subRoot)
