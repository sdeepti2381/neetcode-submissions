class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count = dict()
        
        for x in s:
            if x not in count:
                count[x] = 1
            else:
                count[x] += 1
        
        for y in t:
            if y not in count:
                return False
            else:
                count[y] -= 1
        
        for value in count.values():
            if value != 0:
                return False
        
        return True


        