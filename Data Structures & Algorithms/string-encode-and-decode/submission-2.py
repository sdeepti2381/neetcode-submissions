class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = []
        for string in strs:
            encoded = []
            encoded.append(str(len(string)))
            encoded.append("#")
            encoded.append(string)
            encoded_strings.append("".join(encoded))
        
        return "".join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            decodedString = s[j + 1: j + word_length + 1]
            i = j + word_length + 1
            decodedStrings.append(decodedString)
        
        return decodedStrings




