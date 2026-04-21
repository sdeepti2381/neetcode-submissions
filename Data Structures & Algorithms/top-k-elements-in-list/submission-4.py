class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for x in nums:
            count[x] = count.get(x, 0) + 1

        for number, occurences in count.items():
            frequencies[occurences].append(number)   
        

        result = []
        i = len(frequencies) - 1
        while i > 0:
            j = len(frequencies[i]) - 1
            while j >= 0:
                result.append(frequencies[i][j])
                if len(result) == k:
                    return result
                j = j - 1
            i = i - 1
    



        

        