class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #using a min heap
        if len(stones) == 1:
            return stones[0]
        #1. convert to negative and build minheap -- converting to negative makes a maxheap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones) #pop root
            second = heapq.heappop(stones) #pop root again, automatically reorders
            if first < second:
                heapq.heappush(stones, (first - second))
            
        if stones:
            return abs(stones[0])
        else:
            return 0
            