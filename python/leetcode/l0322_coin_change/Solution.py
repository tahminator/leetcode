from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]

        dp[0] = 0

        for i in range(1, len(dp)):
            for coin in coins:
                if coin > i:
                    continue

                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1


print(Solution().coinChange([1,2,5], 11))
