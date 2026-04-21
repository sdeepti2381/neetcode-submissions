class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, val in enumerate(numbers):
            compliment = target - val
            i = idx + 1
            j = len(numbers) - 1

            while i <= j:
                mid = (i + j) // 2
                if compliment == numbers[mid]:
                    return [idx + 1, mid + 1]
                elif compliment > numbers[mid]:
                    i = mid + 1
                elif compliment < numbers[mid]:
                    j = mid - 1
            
            

            
            
               

