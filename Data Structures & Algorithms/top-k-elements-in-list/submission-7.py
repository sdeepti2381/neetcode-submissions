class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)

        for x in nums:
            count[x] += 1
        
        frequencies = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            frequencies[value].append(key)
        
        result = []
        i = len(frequencies) - 1
        while i > 0:
            for x in frequencies[i]:
                result.append(x)
                if len(result) == k:
                    return result
                
            i -= 1
        
        return result


        
      