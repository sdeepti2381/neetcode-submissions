class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0

        while i < len(numbers):
            val = target - numbers[i]
            j = i + 1
            k = len(numbers) - 1

            while j <= k:
                mid = (j + k) // 2
                if numbers[mid] == val:
                    return [i + 1, mid + 1]
                elif numbers[mid] < val:
                    j += 1
                elif numbers[mid] > val:
                    k -= 1
            i += 1
        

        