class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #looking for fastest way to get to the end of array
        #min(min sum to n + n, min sum to n - 1 + n-1)

        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = cost[0]

        for i in range(2, len(dp)):
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])

        dp2 = [0] * (len(cost) + 1)
        dp2[1] = 0
        dp2[2] = cost[1]

        for i in range(3, len(dp2)):
            dp2[i] = min(cost[i - 1] + dp2[i - 1], cost[i - 2] + dp2[i - 2])

        print(dp, dp2)

        return min(dp2[-1], dp[-1])

            

