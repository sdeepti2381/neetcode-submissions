# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        totalNodes = 0
        curr = head
        while curr:
            totalNodes += 1
            curr = curr.next
        
        prevIdx = totalNodes - n
        if prevIdx == 0:
            head = head.next
            return head
        
        idx = 0
        curr = head
        while curr:
            idx += 1
            if idx == prevIdx:
                curr.next = curr.next.next
                return head
            curr = curr.next







        