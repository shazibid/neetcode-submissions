class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} 
        #trick is to sort the letters!!

        for i in strs:
            word = sorted(i)

            #everything from this point forwards is a miss
            if tuple(word) not in anagrams:
                anagrams[tuple(word)] = []
           
            anagrams[tuple(word)].append(i)    

        return list(anagrams.values())

        #why tuple??