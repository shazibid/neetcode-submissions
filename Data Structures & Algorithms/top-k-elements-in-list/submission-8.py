class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counting = {}

        for i in nums:
            if i not in counting:
                counting[i] = 1
            else:
                counting[i] += 1
        
        frq = [[] for _ in range(len(nums) + 1)]

        for i, val in counting.items():
            frq[val].append(i)
        
        res = []

        for i in range(len(frq) - 1, 0, -1):
            for val in frq[i]:
                res.append(val)
                if len(res) == k:
                    return res
        


