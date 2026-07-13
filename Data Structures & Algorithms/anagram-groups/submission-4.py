class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            word = sorted(i)

            if tuple(word) not in d:
                d[tuple(word)] = []
            d[tuple(word)].append(i)
        
        return list(d.values())