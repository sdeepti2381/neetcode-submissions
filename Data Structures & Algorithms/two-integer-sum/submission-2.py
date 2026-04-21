class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numbers = dict()
        # i = 0
        # while i < len(nums):
        #     complement = target - nums[i]
        #     if complement in numbers.keys():
        #         return [numbers[complement], i]
        #     if nums[i] not in numbers.keys():
        #         numbers[nums[i]] = i
        #     i += 1
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i



            


    
        