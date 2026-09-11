class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i, j in points:
            d = (i ** 2) + (j ** 2)
            minheap.append([d, i, j])
        
        heapq.heapify(minheap)
        res = []

        while k > 0:
            d, a, b = heapq.heappop(minheap)
            res.append([a, b])
            k -= 1
        
        
        return res