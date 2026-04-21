class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while(l < r):
            currSum = numbers[l] + numbers[r]

            if currSum == target:
                return [l + 1, r + 1]
            elif currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
        
        return [l, r]


        # while i < len(numbers):
        #     val = target - numbers[i]
        #     j = i + 1
        #     k = len(numbers) - 1

        #     while j <= k:
        #         mid = (j + k) // 2
        #         if numbers[mid] == val:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < val:
        #             j += 1
        #         elif numbers[mid] > val:
        #             k -= 1
        #     i += 1



        
        

        