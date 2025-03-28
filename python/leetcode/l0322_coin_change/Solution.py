from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float("inf")]
        self.backtrack(coins, 0, 0, amount, res)
        return res[0] if res[0] != float("inf") else -1

    def backtrack(self, coins, currAmount, currCoins, amount, res):
        if currAmount > amount:
            return

        if currAmount == amount:
            res[0] = min(res[0], currCoins)
            return

        for coin in coins:
            self.backtrack(coins, currAmount + coin, currCoins + 1, amount, res)

# print(Solution().coinChange([1,2,5], 11))
