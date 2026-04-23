class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = defaultdict(int)
        frequencies = [[] for i in range(0,len(nums))]

        for x in nums:
            count[x] += 1 # or count[x] = count.get(x, 0) + 1
        
        for key, val in count.items():
            frequencies[val - 1].append(key)
        print(frequencies)
        
        res = []
        i = len(frequencies) - 1
        while i >= 0:
            j = 0
            while j < len(frequencies[i]):
                res.append(frequencies[i][j])
                if len(res) == k:
                    return res
                j += 1
            i -= 1
        
        return res
        






        
      