class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        charRemoved1 = 0
        charRemoved2 = 0

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                while s[i] != s[j] and i <= j:
                    j -= 1
                    charRemoved1 += 1

        i = 0
        j = len(s) - 1
        
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                while s[i] != s[j] and i <= j:
                    i += 1
                    charRemoved2 += 1
        
        print(charRemoved1)
        print(charRemoved2)
        
        return ((charRemoved1 <= 1) or (charRemoved2 <= 1))





        
        