class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newnums = []
        for i in nums:
            newnums.append(-1 * i)

        heapq.heapify(newnums)

        while k > 0:
            res = heapq.heappop(newnums)
            k -= 1
        
        return res * -1

        