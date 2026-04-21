class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestSeq = 0
        for x in nums:
            sequence = set()
            sequence.add(x)
            while (x + 1) in nums:
                sequence.add(x + 1)
                x += 1
            if len(sequence) > longestSeq:
                longestSeq = len(sequence)
        
        return longestSeq


    