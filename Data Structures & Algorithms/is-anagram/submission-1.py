class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        data = {}

        for i in s:
            data[i] = data.get(i, 0) + 1
        
        for i in t:
            if i in data:
                data[i] -= 1
                if data[i] < 0:
                    return False
            else:
                return False
        
        return True
            