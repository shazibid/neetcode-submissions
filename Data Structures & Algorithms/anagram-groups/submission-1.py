class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #im looking at an array of sets + count
        #print([data.values])
        data = {}

        for i in strs:
            # i need the count of every letter im every word and then to check that existence in the set
            # key = letters, value = array of words
            word = sorted(i)
            if tuple(word) not in data: #converts word into an array
                data[tuple(word)] = [] # need to make an array first
            data[tuple(word)].append(i)
        
        return list(data.values())