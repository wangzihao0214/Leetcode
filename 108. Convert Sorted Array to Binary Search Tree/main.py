# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left, right):
                index = (right + left) // 2
                root = TreeNode(nums[index])
                if left == right:
                    return root
                if left > right:
                    return None
                root.left = construct(left, index - 1)
                root.right = construct(index + 1, right)
                return root
        
        n = len(nums)
        return construct(0, n - 1)