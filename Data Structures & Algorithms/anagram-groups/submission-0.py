class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = []
        anagramMap = {}

        for i, n in enumerate(strs):
            sorted_n = ''.join(sorted(n))
            if sorted_n in anagramMap.keys():
                anagramMap[sorted_n].append(n)
            else:
                anagramMap[sorted_n] = [n]

        return anagramMap.values()


        


