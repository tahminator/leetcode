class Solution:
    def climbStairs(self, n: int) -> int:
        # n + 1 spots
        dp = [0 for _ in range(n + 2)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 2):
            dp[i] = dp[i - 1] + dp[i - 2]

        print(dp)
        return dp[n + 1]

print(Solution().climbStairs(5))
