class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return values who's counts >= k
        data = {}

        for i in nums:
            data[i] = data.get(i, 0) + 1
        
        # sorts dict in descending order
        data = sorted(data.items(), key=lambda item: item[1], reverse=True)

        arr = []

        i = 0

        while i < k:
            arr.append(data[i][0])
            i += 1
        
        return arr
