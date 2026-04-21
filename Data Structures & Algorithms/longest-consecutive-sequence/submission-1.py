class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        result = 0
        numbers = set(nums)
        seqmap = {}
        
        for x in nums:
            if x - 1 in numbers:
                continue
            else:
                start = x
                seqmap[start] = [start]
                while x + 1 in numbers:
                    seqmap[start].append(x + 1)
                    x += 1

        for seq in seqmap.values():
            result = max(result, len(seq))

        return result





    