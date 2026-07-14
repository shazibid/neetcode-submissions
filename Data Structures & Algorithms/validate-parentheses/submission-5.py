class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        mapping = {'}':'{', ')':'(', ']':'['}

        ## first case
        if s[0] not in mapping.values():
            return False

        for i in s:
            if i in mapping.values():
                arr.append(i)

            elif i in mapping.keys() and len(arr) > 0 and mapping[i] == arr.pop():
                continue
            else:
                return False
            

        return len(arr) == 0
                
