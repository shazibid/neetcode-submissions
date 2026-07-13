class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        data = {}

        # O(n) to loop through the first string and count numbers of letters
        for i in s:
            data[i] = data.get(i, 0) + 1
        
        # O(n) again to loop through ch in t
        for i in t:
            if i in data:
                data[i] -= 1

                if data[i] < 0:
                    return False

            if i not in data:
                return False
            
        return True