# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(val = 0)
        current = res
        r = 0

        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            nodes_sum = l1_val + l2_val + r

            current.next = ListNode(val = nodes_sum % 10)

            r = nodes_sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            current = current.next
        
        if r != 0:
            current.next = ListNode(val = r)

        return res.next
