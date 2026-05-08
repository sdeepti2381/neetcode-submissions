class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return

            if i >= len(nums) or total > target:
                return
            
            # take the current number again 
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()

            # skip the current number
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res

        
    
            
        


        