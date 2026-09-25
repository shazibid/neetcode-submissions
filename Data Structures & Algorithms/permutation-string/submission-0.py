class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #strictly look at the letters in the window of size s1 in s2, if all characters appear then yes

        #could hit sorted and check against
        l = 0
        r = len(s1)
        string = s2[l:r]
        s12 = "".join(sorted(s1))

        while r <= len(s2):
            string2 = "".join(sorted(string))

            if string2 == s12:
                return True
            
            string = string[1:]
            if r < len(s2):
                string += s2[r]
            r += 1
        return False


