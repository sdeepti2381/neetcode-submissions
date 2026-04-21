class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = [1] * len(nums) 
        right = [1] * len(nums)

        i = 1
        while i < len(nums):
            left[i] = left[i - 1] * nums[i - 1]
            i += 1
        
        j = len(nums) - 2
        while j >= 0:
            right[j] = nums[j + 1] * right[j + 1]
            j -= 1

        result = []
        k = 0
        while k < len(nums):
            result.append(left[k] * right[k])
            k += 1
        
        return result

        

        


