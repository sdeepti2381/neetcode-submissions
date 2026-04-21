class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            target = 0 - nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    if [nums[i], nums[j], nums[k]] not in triplets:
                        triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                if nums[j] + nums[k] > target:
                    k -= 1
                if nums[j] + nums[k] < target:
                    j += 1
        
        return triplets
                
                    

