class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedS = ""
        i = 0

        while (i < len(word1) and i < len(word2)):
            mergedS += word1[i]
            mergedS += word2[i]
            i += 1

        if i < len(word2):
            mergedS += word2[i:]
        
        if i < len(word1):
            mergedS += word1[i:]
        
        return mergedS
        
