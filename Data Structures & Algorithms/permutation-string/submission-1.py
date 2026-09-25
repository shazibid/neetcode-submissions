class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        string = s2[l:r]
        s12 = "".join(sorted(s1))

        while r <= len(s2):
            if "".join(sorted(string)) == s12:
                return True
            
            string = string[1:]

            if r < len(s2):
                string += s2[r]

            r += 1
            

        return False