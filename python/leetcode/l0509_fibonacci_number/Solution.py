class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        dp = [0, 1]

        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[-1]

    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        p1, p2 = 0, 1

        i = 2
        while i < n:
            c = p1 + p2
            p1, p2 = p2, c
            i += 1

        return p1 + p2


