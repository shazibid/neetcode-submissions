class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicty = {}

        for i in nums:
            dicty[i] = dicty.get(i, 0) + 1
        
        frq = [[] for i in range(len(nums) + 1)]
        
        for n, c in dicty.items():
            frq[c].append(n)
        
        res = []

        for i in range(len(frq) - 1, 0, -1):
            for j in frq[i]:
                if len(res) < k:
                    res.append(j)
        
        return res
