class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        result = []

        for idx, val in enumerate(numbers):
            compliment = target - val
            i = idx + 1
            while i < len(numbers):
                if numbers[i] == compliment:
                    return [idx + 1, i + 1]
                else:
                    i += 1
            
               

