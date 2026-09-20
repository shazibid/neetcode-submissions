class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make the dict key the ordered string, the items as the array of strings
        
        dicty = {}
        for i in strs:
            s = "".join(sorted(i))
            if s not in dicty:
                dicty[s] = []

            dicty[s].append(i)    
        
        res = []
        for i in dicty.values():
            res.append(i)

        return res 