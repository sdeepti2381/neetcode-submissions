class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for idx, x in enumerate(numbers):
            compliment = target - x
            l = idx + 1
            r = len(numbers) - 1
            while l <= r:
                mid = (l + r)//2
                if numbers[mid] == compliment:
                    return [idx + 1, mid + 1]
                elif numbers[mid] < compliment:
                    l = mid + 1
                elif numbers[mid] > compliment:
                    r = mid - 1
            

        