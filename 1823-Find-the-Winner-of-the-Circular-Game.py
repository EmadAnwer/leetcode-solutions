class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        class Node:
            def __init__(self, val=None, next=None):
                self.val = val
                self.next = next

        head = Node(1)
        cur = head
        for i in range(2, n + 1):
            cur.next = Node(i)
            cur = cur.next
        cur.next = head 

        while cur.next != cur:
            for _ in range(k - 1):
                cur = cur.next
            cur.next = cur.next.next
        
        return cur.val