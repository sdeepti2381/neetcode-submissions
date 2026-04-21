class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for x in strs:
            sorted_x = "".join(sorted(x))
            if sorted_x in anagrams:
                anagrams[sorted_x].append(x)
            else:
                anagrams[sorted_x] = [x]
        

        return list(anagrams.values())


