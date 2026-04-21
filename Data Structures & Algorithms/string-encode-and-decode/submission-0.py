class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStringSplit = [] 

        for word in strs:
            encodedStringSplit.append(str(len(word)))
            encodedStringSplit.append("#")
            encodedStringSplit.append(word)
            
        encodedString = ''.join(encodedStringSplit)

        return encodedString

    def decode(self, s: str) -> List[str]:
        splittedString = list(s)
        decodedString = []

        i = 0
        while i < len(splittedString):
            j = i
            tempLength = []
            while splittedString[j] != "#":
                tempLength.append(splittedString[j])
                j += 1
            length = int(''.join(tempLength))
            k = 1
            word = []
            while k <= length:
                word.append(splittedString[j + k])
                k += 1
            decodedString.append(''.join(word))
            i = j + length + 1
        
        return decodedString
        







