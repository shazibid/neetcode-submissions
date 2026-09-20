class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicty = {}

        for i in range(len(s)):
            dicty[s[i]] = dicty.get(s[i], 0) + 1
        
        print(dicty)
        
        for i in range(len(t)):
            if t[i] not in dicty:
                return False
            
            dicty[t[i]] -= 1
            
            if dicty[t[i]] < 0:
                return False
        
        print(dicty)
        
        for i in dicty:
            if dicty[i] != 0:
                return False
        
        return True