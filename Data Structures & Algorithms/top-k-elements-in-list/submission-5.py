class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for x in nums:
            count[x] += 1
        
        # sort count in descending order of occurences
        sorted_items = sorted(count.items(), key=lambda item: item[1], reverse=True)

        result = []
        i = 0
        while i < len(sorted_items) and i < k:
            result.append(sorted_items[i][0])
            i += 1
        
        return result
        
      