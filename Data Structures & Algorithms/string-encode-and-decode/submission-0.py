class Solution:

    def encode(self, strs: List[str]) -> str:
        coder = ""
        for s in strs:
            size = len(s)
            coder += (str(size) + "#" + s)
        return coder

#---------------------------------------------------
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            j += 1

            word = s[j:j + length]

            words.append(word)

            i = j + length
    
        return words
            
