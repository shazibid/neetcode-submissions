class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProf = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                prof = prices[r] - prices[l]
                maxProf = max(maxProf, prof)

                r += 1
        
        return maxProf
            
