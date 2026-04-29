# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = [-root.val]
        queue = deque()
        if root.left: queue.append(root.left)
        if root.right: queue.append(root.right)

        while len(queue) > 0:
            node = queue.popleft()
            if not node:
                continue
            if len(heap) < k:
                heapq.heappush(heap, -node.val)
            elif node.val < -heap[0]:
                heapq.heappush(heap, -node.val)
                if len(heap) > k:
                    heapq.heappop(heap)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        
        return -heap[0]



        



