class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #one approach is to make a dictionary of key being the num, val being the count, then sort based on val (count)
            #naive f u

        freq = [[] for i in range(len(nums) + 1)] # the for loop makes the size of the array as big as the input
        count = 0
        d = {}

        #for each index in freq, its is the count of the value in nums, store the list of values that appear that many times in frq
        for i in nums:
            d[i] = d.get(i, 0) + 1
        
        for i, value in d.items():
            freq[value].append(i)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


