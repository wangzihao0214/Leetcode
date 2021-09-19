# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        flag = 1
        while len(queue) != 0:
            result_temp = []
            queue_temp = []
            while len(queue) != 0:
                node = queue.pop(0)
                result_temp.append(node.val)
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue = queue_temp
            if flag:
                result.append(result_temp)
            else:
                result.append(result_temp[::-1])
            flag = not flag

        return result