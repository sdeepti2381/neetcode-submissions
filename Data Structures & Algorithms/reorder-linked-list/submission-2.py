
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the midpoint 
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        # reverse the second half 
        curr = slow.next
        slow.next = None
    
        prev = None 
        while curr:
            tmp, curr.next, prev = curr.next, prev, curr
            curr = tmp
        
        # merge the lists 
        l,r = head, prev
        while r:
            tmp1, tmp2 = l.next, r.next
            l.next, r.next = r, tmp1
            l, r = tmp1, tmp2
