class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for i in strs:
            word = sorted(i)
            if tuple(word) not in hm:
                hm[tuple(word)] = []
            
            hm[tuple(word)].append(i)
        
        return list(hm.values())
