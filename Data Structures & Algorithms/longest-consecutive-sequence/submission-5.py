class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longestSequence = 0
        uniqueNums = set(nums)

        for x in nums:
            k = 1
            if x - 1 not in uniqueNums:
                while x + 1 in uniqueNums:
                    k += 1
                    x += 1
                if k > longestSequence:
                    longestSequence = k
        
        return longestSequence

        




    