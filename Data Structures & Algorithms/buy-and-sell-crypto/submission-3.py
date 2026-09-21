class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprice = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l += 1
            else:
                hold = prices[r] - prices[l]
                maxprice = max(hold, maxprice)
                r += 1
        return maxprice

