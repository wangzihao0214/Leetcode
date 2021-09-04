# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        
        node = head
        while node.next:
            length += 1
            node = node.next
        if length == 1:
            return None
            
        remove_index = length - n
        
        if remove_index == 0:
            head = head.next
        else:
            node = head
            for i in range(remove_index - 1):
                node = node.next

            node.next = node.next.next
        
        return head