class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for x in strs:
            sorted_x = "".join(sorted(x))
            anagrams[sorted_x].append(x)
        
        return list(anagrams.values())


