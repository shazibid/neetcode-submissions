class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #brute force: iterate by minimum # of bananas eaten per hr, check if it can be done within h
        #bs: \

        def time2eat(piles, m):
            summy = 0
            for i in piles:
                summy += math.ceil(i / m)
            return summy

        if len(piles) > h:
            return -1

        k = max(piles)

        l = 1
        r = k

        while l <= r:
            m = l + ((r - l) // 2)

            if time2eat(piles, m) > h:
                l = m + 1
            elif time2eat(piles, m) <= h:
                r = m - 1
                minPossible = m
        
        return minPossible            