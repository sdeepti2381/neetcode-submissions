class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        i = 0
        while i < len(nums):
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k and k > i:
                temp = nums[j] + nums[k]
                if temp == target:
                    res.append([nums[i], nums[j], nums[k]])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                    while k > i and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif temp < target:
                    j += 1
                elif temp > target:
                    k -= 1
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return res

        