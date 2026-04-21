class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = dict()
        i = 0
        while i < len(nums):
            complement = target - nums[i]
            if complement in numbers.keys():
                return [numbers[complement], i]
            numbers[nums[i]] = i
            i += 1



            


    
        