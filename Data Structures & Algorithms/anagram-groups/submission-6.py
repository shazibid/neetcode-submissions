class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for i in strs:
            word = sorted(i)

            if tuple(word) not in words:
                words[tuple(word)] = []
            
            words[tuple(word)].append(i)
        
        return list(words.values())
