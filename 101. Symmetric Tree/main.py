# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def compare(left, right):
            if not left and right:
                return False
            if left and not right:
                return False
            if not left and not right:
                return True
            return left.val == right.val and compare(left.left, right.right) and compare(left.right, right.left)

        return compare(root, root)

#         def compare(left, right):
#             if left.val != right.val:
#                 return False
#             if left.left and right.right:
#                 if not compare(left.left, right.right):
#                     return False
#             elif not left.left and not right.right:
#                 pass
#             else:
#                 return False
#             if left.right and right.left:
#                 if not compare(left.right, right.left):
#                     return False
#             elif not left.right and not right.left:
#                 pass
#             else:
#                 return False
#             return True

#         return compare(root, root)
