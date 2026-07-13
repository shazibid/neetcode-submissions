class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for i in strs:
            string += str(len(i)) + "#" + i
        
        return string


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        # understand when to use while vs for
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j]) #these range strings are your bestie

            start = j + 1
            end = j + 1 + length

            strs.append(s[start:end])

            i = end




        return strs

        #hardest part is figuring out positioning to iterate
                


