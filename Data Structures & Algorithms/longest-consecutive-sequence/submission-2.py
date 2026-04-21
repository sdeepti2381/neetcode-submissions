class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longestSequence = []

        for x in nums:
            if x in longestSequence:
                continue
            sequence = [x]
            while x + 1 in nums:
                sequence.append(x + 1)
                x += 1
            if len(sequence) > len(longestSequence):
                longestSequence = sequence
        
        return len(longestSequence)

        




    