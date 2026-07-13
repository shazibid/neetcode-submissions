class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d = {}
        # i want the letter to be the key, count to be value
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                count = d[i] + 1
                d[i] = count
            
        for i in t:
            if i not in d:
                return False
            else:
                count = d[i] - 1
                d[i] = count
                if count < 0:
                    return False
            
        return True

            