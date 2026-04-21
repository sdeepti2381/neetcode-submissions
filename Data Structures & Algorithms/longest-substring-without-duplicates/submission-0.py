class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subsetString = set()
        maxLength = 0

        l,r = 0, 0

        while r < len(s):
            while s[r] in subsetString:
                subsetString.remove(s[l])
                l += 1
            subsetString.add(s[r]) # [p,w]
            maxLength = max(maxLength, r - l + 1) #2
            r += 1 #2
        
        return maxLength

        