class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        # i want the key to be the sorted string, value to be a list of the strings that align with the sorted string

        for i in strs:
            word = sorted(i)

            if tuple(word) not in data:
                data[tuple(word)] = []
            data[tuple(word)].append(i)
        
        return list(data.values())