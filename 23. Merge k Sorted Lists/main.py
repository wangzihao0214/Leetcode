# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        result = ListNode()
        temp = result
        
        all_none = True
        num_none = 0
        for i in range(n):
            if lists[i]:
                all_none = False
            else:
                num_none += 1
                
        if all_none:
            return None
        
        num_empty = 0
        while num_empty < n - num_none - 1:
            min_val = 10 ** 4
            for i in range(n):
                if lists[i]:
                    if lists[i].val < min_val:
                        min_val = lists[i].val
                        pos = i
            temp.next = ListNode(min_val)
            temp = temp.next
            lists[pos] = lists[pos].next
            if not lists[pos]:
                num_empty += 1
        
        i = 0
        while not lists[i]:
            i += 1
        temp.next = lists[i]
        
        return result.next