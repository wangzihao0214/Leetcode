# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = 0
        right = 0
        
        temp = head
        
        while temp:
            right += 1
            temp = temp.next
        
        if right % 2 != 0:
            left = (right + 1) // 2
        else:
            left = right // 2 + 1
        
        result = head
        for i in range(left - 1):
            result = result.next
        return result