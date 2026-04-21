class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]
        right = [1] * len(nums)

        result = []

        for i in range(len(nums)):
            left.append(nums[i] * left[-1])

        for i in range(len(nums) - 2, -1, -1):
            right[i] = (nums[i + 1] * right[i + 1])
        
        j = 0
        while j < len(nums):
            result.append(left[j] * right[j])
            j += 1
        
        return result




        