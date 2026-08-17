class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #could use a queue, if array grows too big you pop
        #dictionary to keep track on counts
        l = [[] for i in range(len(nums) + 1)]
        count = {}

        #build count dictionary
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        #build array l (frequencies) where count is the index of where the num is appended as a sublist
        for num, cnt in count.items():
            l[cnt].append(num)
        
        res = []
        for i in range(len(l) - 1, 0, -1):
            for num in l[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
