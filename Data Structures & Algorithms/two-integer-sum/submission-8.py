class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        pairs = {}

        for i, x in enumerate(nums):
            if (target - x) in pairs.keys():
                return [pairs.get(target - x), i]
            else:
                pairs[x] = i
