# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        temp = ListNode(101)
        temp.next = head
        pre = temp
        cur = head
    
        while cur:
            flag = 0
            while cur.next and cur.val == cur.next.val:
                flag = 1
                cur.next = cur.next.next
            nxt = cur.next
            if flag:
                pre.next = nxt
            else:
                pre = cur
            cur = nxt
        
        return temp.next