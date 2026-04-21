class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        k = m
        j = 0
        while j < n:
            i = k
            nums1[i] = nums2[j]
            while (i >= 1) and (nums1[i - 1] > nums1[i]):
                temp = nums1[i]
                nums1[i] = nums1[i - 1]
                nums1[i - 1] = temp
                i -= 1
            j += 1
            k += 1