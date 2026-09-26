class Solution:
    def climbStairs(self, n: int) -> int:
        #say n = 10; 1 + 1 + ... + 1 = 10, or 1 + 1 + ... + 2 = 10; all the possible combinations of 1 U 2 that adds to n
        #how many ways to get to 8 and how many times it would take to get to 9
        #nth step

        #solve for dp of n
            #= some combination of smaller n values
            #dp of n-1 + n-2
        
        #bottom up dp, or top down
        #memoization

        dp = [0 for i in range(n + 1)]

        if n > 0:
            dp[1] = 1
        if n > 1:
            dp[2] = 2

        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]