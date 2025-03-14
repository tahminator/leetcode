from typing import List
import math

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        Binary search solution. Non-binary search solution commented below.
        """
        res = 0
        l, r = 1, max(candies)

        while l <= r:
            m = (l + r) // 2

            piles = self.helper(candies, m)

            if piles >= k:
                res = max(res, m)
                l = m + 1
            else:
                r = m - 1

        return res

    def helper(self, candies, pile_size):
        valid_piles = 0
        for candy in candies:
            valid_piles += candy // pile_size

        return valid_piles
        

# class Solution:
#     def maximumCandies(self, candies: List[int], k: int) -> int:
#         """
#         This is similar to Koko Eats Bananas, where we want to find (in this case) maximum candies we can 
#         give to each child equally. However, we can never give more than the maximum value in the list.
#
#         I'm going to start by solving it without binary search.
#         """
#
#         max_res = 0
#
#         for i in range(1, max(candies)):
#             max_res = max(max_res, self.helper(candies, i, k))
#
#         return max_res
#
#
#     def helper(self, candies, pile_size, k):
#         valid_piles = 0
#         for candy in candies:
#                 valid_piles += math.ceil(candy // pile_size) 
#
#         # print("valid piles: ", valid_piles)
#         # print("pile_size: ", pile_size)
#
#         return pile_size if valid_piles >= k else 0

