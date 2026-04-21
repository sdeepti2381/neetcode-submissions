class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appeared = set()

        for x in nums:
            if x in appeared:
                return True
            appeared.add(x)
        return False 