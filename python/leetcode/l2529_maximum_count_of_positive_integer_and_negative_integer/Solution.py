from typing import List

"""
We can use binary search twice: once to find the positive and once
to find the negative.

If it were guaranteed there would be one and only one 0, we could've 
just searched for that 0 and then calculate the `pos` and `neg` as needed.
Something to keep in mind, if a similar problem ever comes up.
"""

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] <= 0:
                l = m + 1
            else:
                r = m - 1

        pos = len(nums) - l

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] >= 0:
                r = m - 1
            else:
                l = m + 1

        neg = r + 1

        return max(pos, neg)


print(Solution().maximumCount([-2,-1,-1,1,2,3]))

# print(Solution().maximumCount([5,20,66,1314]))
