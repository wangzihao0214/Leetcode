# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        result = temp
        flag = 0
        while l1.val >= 0 or l2.val >= 0:
            if l1.val < 0:
                x = 0
            else:
                x = l1.val
            if l2.val < 0:
                y = 0
            else:
                y = l2.val
            sum = x + y + flag
            temp.val = sum % 10
            flag = sum // 10
            if l1.next:
                l1 = l1.next
            else:
                l1 = ListNode(-1)
            if l2.next:
                l2 = l2.next
            else:
                l2 = ListNode(-1)
            if l1.val >= 0 or l2.val >= 0 or flag:
                temp.next = ListNode(0)
                temp = temp.next
        if flag:
            temp.val = 1
        return result