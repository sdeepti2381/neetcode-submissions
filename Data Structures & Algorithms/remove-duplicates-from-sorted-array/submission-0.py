class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        j = 0
        seen = set()

        while i < len(nums) and j < len(nums):    
            if nums[j] not in seen:
                nums[i] = nums[j]
                seen.add(nums[j])
                i += 1
                j += 1
            else:
                j += 1
        
        return len(seen)


            


        

        