# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, id(node), node))
        
        heapq.heapify(heap)
        
        while heap:
            value, _, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))
            
        return dummy.next
                



        
        