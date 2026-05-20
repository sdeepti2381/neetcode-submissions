class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def combinationPath(curr: List[int], currSum, index):
            if index >= len(nums):
                return
            if currSum == target:
                result.append(curr.copy())
                return
            if currSum > target:
                return 
            for i in range(index, len(nums)):
                num = nums[i]
                curr.append(num)
                currSum += num
                combinationPath(curr, currSum, i)
                curr.pop()
                currSum -= num
            return

        combinationPath([], 0, 0)

        return result



            

