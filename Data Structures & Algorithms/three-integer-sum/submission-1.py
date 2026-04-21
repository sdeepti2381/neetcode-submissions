class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        triplets = []

        for idx, val in enumerate(nums):
            compliment = 0 - val
            i = idx + 1
            j = len(nums) - 1
            
            while i < j:
                if ((nums[i] + nums[j]) == compliment):
                    if ([val, nums[i], nums[j]] not in triplets):
                        triplets.append([val, nums[i], nums[j]])
                    i += 1
                    j -= 1

                elif((nums[i] + nums[j]) < compliment):
                    i += 1
                
                elif((nums[i] + nums[j]) > compliment):
                    j -= 1
        
        return triplets
            
            


                

