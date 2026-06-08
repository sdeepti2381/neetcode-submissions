class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count each element's occurences 
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        frequencies = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            frequencies[freq].append(num)
        

        res = []

        for i in range(len(frequencies) - 1, 0, -1):
            for j in range(len(frequencies[i])):
                res.append(frequencies[i][j])
                if len(res) == k:
                    return res
        
        return res
        



        


        