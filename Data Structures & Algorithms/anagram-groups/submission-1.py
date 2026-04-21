class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(mnlogn) time complexity
        # anagramGroups = []
        # anagramMap = {}

        # for i, n in enumerate(strs):
        #     sorted_n = ''.join(sorted(n))
        #     if sorted_n in anagramMap.keys():
        #         anagramMap[sorted_n].append(n)
        #     else:
        #         anagramMap[sorted_n] = [n]

        # return anagramMap.values()

        # O(mn) time complexity
        res = defaultdict(list)
        for string in strs:
            characterCount = [0]*26
            for c in string:
                characterCount[ord(c)-ord("a")] += 1
            res[tuple(characterCount)].append(string)
        
        return res.values()






        


