# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def construct(pointer, left, right):
            value = preorder[pointer]
            root = TreeNode(value)
            index = dic[value]
            for i in range(pointer + 1, n):
                value_next = preorder[i]
                index_next = dic[value_next]
                if left <= index_next <= right:
                    if not root.left and index_next < index:
                        root.left = construct(i, left, index - 1)
                    if not root.right and index_next > index:
                        root.right = construct(i, index + 1, right)
                    if root.left and root.right:
                        break
            return root
                    
        n = len(preorder)
        dic = {}
        for i in range(n):
            dic[inorder[i]] = i
            
        return construct(0, 0, n - 1)
